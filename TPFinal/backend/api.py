import flask
import json

from Bio.Application import ApplicationError
from flask import request
from flask_cors import CORS, cross_origin
from flask_restful import abort

from backend.exceptions.ChainPDBDoesNotExistException import ChainPDBDoesNotExistException
from backend.exceptions.PDBDoesNotExistException import PDBDoesNotExistException
from service.PDBService import PDBService
from service.ClustalService import ClustalService
from service.BlastService import BlastService
from service.LogoService import LogoService

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["CORS_HEADERS"] = "Content-Type"
CORS(app)
pdbService = PDBService()
blastService = BlastService()
clustalService = ClustalService()
logoService = LogoService()


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return "<h1>Prueba.</p>"


def validateField(dataJson, fieldJson, value):
    value_return = dataJson[fieldJson] if str(dataJson[fieldJson]).strip() != "" and not dataJson[fieldJson] else value
    return value_return


@app.route('/pdb', methods=['POST'])
@cross_origin()
def getInfo():
    data = request.get_json()
    result = {"clustal": "", "seq": "", "id": ""}
    # si no tiene id el request directamente retorna error
    id = data["id"]
    if not id:
        abort(404, message="Error: No real id provided. Please rewrite id field.")

    result["id"] = id
    clustalw_exe = data["clustal_path"]
    if not clustalw_exe:
        abort(404, message="Error: No clustal field provided. Please specify a clustal path.")
    identity = float(validateField(data, "identity", 39.9))
    identity = identity if identity > 0 else 39.9
    num_align = data["num_align"]
    chain = data["chain"]
    e_value = float(data["e_value"])
    db = validateField(data, "db", "pdb")

    try:
        result["pdbPath"] = pdbService.getPDB(id)
        result["id"] = result["id"] + "_" + chain
        result["seq"] = pdbService.converToSequence(id, chain)
        blastService.getBlast(id,result["seq"],db,int(num_align),e_value,identity)
        result["clustal"] = clustalService.getClustal(clustalw_exe,blastService.getBaseFasta(),id)
        # result["numGraph"]=logoService.multiLogo(result["clustal"],id)
    except PDBDoesNotExistException:
        abort(404, message="Error: The id provided does not exist. Please check it and try again.")
    except ChainPDBDoesNotExistException:
        abort(404, message="Error: The chain provided does not exist. Please check it and try again.")
    except FileNotFoundError:
        abort(404, message="Error: Blast cant find homologous.")
    except ApplicationError:
        abort(404, message="Error: Clustal doest not exist on the system.")

    json_object = json.dumps(result, indent=4)
    return (json_object)


if __name__ == '__main__':
    app.run()

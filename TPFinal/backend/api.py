import flask
import json
import os
from datetime import datetime

from Bio.Application import ApplicationError
from flask import request, Response, jsonify
from flask_cors import CORS, cross_origin
from flask_restful import abort

#from backend.exceptions.ChainPDBDoesNotExistException import ChainPDBDoesNotExistException
#from backend.exceptions.PDBDoesNotExistException import PDBDoesNotExistException
#from backend.service.DSSPService import DSSPService
#from service.PDBService import PDBService
#from service.ClustalService import ClustalService
#from service.BlastService import BlastService
#from service.LogoService import LogoService
#
from TPFinal.backend.exceptions.ChainPDBDoesNotExistException import ChainPDBDoesNotExistException
#
from TPFinal.backend.exceptions.PDBDoesNotExistException import PDBDoesNotExistException
#
from TPFinal.backend.service.DSSPService import DSSPService
#
from TPFinal.backend.service.PDBService import PDBService
#
from TPFinal.backend.service.ClustalService import ClustalService
#
from TPFinal.backend.service.BlastService import BlastService
#
from TPFinal.backend.service.LogoService import LogoService



app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["CORS_HEADERS"] = "Content-Type"
CORS(app)
pdbService = PDBService()
blastService = BlastService()
clustalService = ClustalService()
logoService = LogoService()
dsspService = DSSPService()

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return "<h1>Prueba.</p>"


def validateField(dataJson, fieldJson, value):
    value_return = dataJson[fieldJson] if str(dataJson[fieldJson]).strip() != "" and not dataJson[fieldJson] else value
    return value_return


@app.route('/pdb', methods=['POST'])
@cross_origin()
def getInfo() ->Response :
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

    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    log_file = now.strftime("%d-%m-%Y_%Hh%Mm%Ss")+".txt"

    # create file to log services
    log_path = os.path.join(os.getcwd(), "log")
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    log_path = os.path.join(log_path, log_file)

    try:
        result["pdbPath"] = pdbService.getPDB(id)
        result["id"] = result["id"] + "_" + chain
        result["seq"] = pdbService.converToSequence(id, chain)
        blastService.getBlast(id,result["seq"],db,int(num_align),e_value,identity, log_path, chain)
        result["clustal"] = clustalService.getClustal(clustalw_exe,blastService.getBaseFasta(),id, log_path)
        result["dssp"] = dsspService.conservate(result["clustal"])
        result["numGraph"]=logoService.multiLogo(result["clustal"],id)
    except PDBDoesNotExistException:
        print("F pdb")
        abort(404, message="Error: The id provided does not exist. Please check it and try again.")
    except ChainPDBDoesNotExistException:
        print("f cadena")
        abort(404, message="Error: The chain provided does not exist. Please check it and try again.")
    except FileNotFoundError:
        print("f blast")
        abort(404, message="Error: Blast can not find homologous.")
    except ApplicationError:
        print("f clustal")
        abort(404, message="Error: Clustal doest not exist on the system.")

    json_object = json.dumps(result, indent=4)
    #return (json_object)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run()

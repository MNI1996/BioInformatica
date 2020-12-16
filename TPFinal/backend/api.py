import flask
import json
import os
from datetime import datetime

from Bio.Application import ApplicationError
from flask import request, Response
from flask_cors import CORS, cross_origin

from backend.exceptions.ChainPDBDoesNotExistException import ChainPDBDoesNotExistException
from backend.exceptions.NoClustalException import NoClustalException
from backend.exceptions.NoClustalPathProvidedException import NoClustalPathProvidedException
from backend.exceptions.NoHomologousException import NoHomologousException
from backend.exceptions.NoIdProvidedException import NoIdProvidedException
from backend.exceptions.PDBDoesNotExistException import PDBDoesNotExistException
from backend.service.DSSPService import DSSPService
from service.PDBService import PDBService
from service.ClustalService import ClustalService
from service.BlastService import BlastService
from service.LogoService import LogoService


"""
from TPFinal.backend.exceptions.ChainPDBDoesNotExistException import ChainPDBDoesNotExistException
from TPFinal.backend.exceptions.PDBDoesNotExistException import PDBDoesNotExistException
from TPFinal.backend.exceptions.NoClustalException import NoClustalException
from TPFinal.backend.exceptions.NoClustalPathProvidedException import NoClustalPathProvidedException
from TPFinal.backend.exceptions.NoHomologousException import NoHomologousException
from TPFinal.backend.exceptions.NoIdProvidedException import NoIdProvidedException
from TPFinal.backend.service.DSSPService import DSSPService
from TPFinal.backend.service.PDBService import PDBService
from TPFinal.backend.service.ClustalService import ClustalService
from TPFinal.backend.service.BlastService import BlastService
from TPFinal.backend.service.LogoService import LogoService
"""


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
    id = data["id"]
    if not id:
        result = {"error_code": '404', "message": NoIdProvidedException.message()}
        json_object = json.dumps(result, indent=4)
        return (json_object)
    result["id"] = id
    clustalw_exe = data["clustal_path"]
    if not clustalw_exe:
        result = {"error_code": '404', "message": NoClustalPathProvidedException.message()}
        json_object = json.dumps(result, indent=4)
        return (json_object)
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
        result = {"error_code": '404', "message": PDBDoesNotExistException.message()}
    except ChainPDBDoesNotExistException:
        result = {"error_code": '404', "message":  ChainPDBDoesNotExistException.message()}
    except FileNotFoundError:
        result = {"error_code": '404', "message": NoHomologousException.message()}
    except ApplicationError:
        result = {"error_code": '404', "message": NoClustalException.message()}
    json_object = json.dumps(result, indent=4)
    return (json_object)


if __name__ == '__main__':
    app.run()

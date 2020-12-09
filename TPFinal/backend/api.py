import flask
import json

from flask import request
from flask_cors import CORS, cross_origin

from service.PDBService import PDBService
from service.ClustalService import ClustalService
from service.BlastService import BlastService
from service.LogoService import LogoService

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["CORS_HEADERS"] = "Content-Type"
CORS(app)
pdbService=PDBService()
blastService=BlastService()
clustalService=ClustalService()
logoService=LogoService()

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return	 "<h1>Prueba.</p>"

""" el path debería ser /pdb y el json recibido tiene esta estructura
json = { 
   "clustal_path": "C:\\Program Files (x86)\\ClustalW2\\clustalw2.exe",
   "id": "1UBQ",
   "chain": "A",
   "identity": 39.9,
   "num_align": 5,
   "e_value": 0.001,
   "db": "pdb",
   "word_size": 3,
   "gapopen": 11
}
"""
def validateField(dataJson, fieldJson, value):
    value_return = ""
    value_return = dataJson[fieldJson] if str(dataJson[fieldJson]).strip()!="" and not dataJson[fieldJson] else value
    return value_return

@app.route('/pdb', methods=['POST'])
@cross_origin()
def getInfo():
    data = request.get_json()
    result={"clustal":"","seq":"","id":""}
    # si no tiene id el request directamente retorna error
    id = data["id"]
    if not id:
        return "Error: No id field provided. Please specify an id."
    result["id"] = id
    clustalw_exe = data["clustal_path"]
    if not clustalw_exe:
        return "Error: No clustal field provided. Please specify a clustal path."
    identity = float(validateField(data, "identity", 39.9))
    identity = identity if identity > 0 else 39.9
    num_align = int(validateField(data, "num_align", 5)) 
    num_align = num_align if num_align > 0 else 5
    chain = validateField(data, "chain", "A")
    e_value = float(data["e_value"])
    db = validateField(data, "db", "pdb")
    word_size = int(data["word_size"])
    gapopen = int(data["gapopen"])


    result["pdbPath"] =pdbService.getPDB(id)
    result["seq"] = pdbService.converToSequence(id)
    blastService.getBlast(id,result["seq"],db,num_align,e_value,identity)
    result["clustal"] = clustalService.getClustal(clustalw_exe,blastService.getBaseFasta(),id)
    #logoService.logoMaker(result["clustal"],id)


    json_object = json.dumps(result, indent = 4)
    return (json_object)

if __name__ == '__main__':
    app.run()

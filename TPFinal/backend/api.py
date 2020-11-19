import flask
import json
from flask import request, jsonify
from flask_cors import CORS
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.PDB import *
from biopandas.pdb import PandasPdb

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def home():
    return	 "<h1>Prueba.</p>"

# el path debería ser /pdb?id=XXXX donde XXXX representa el código de cuatro letras de la proteina
@app.route('/pdb', methods=['GET'])
def getPDB():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    #result = []#esto tiene  que ser un objeto resutl para poder pasarlo por json
    pdbl = PDBList()
    result={"fafafa":"","seq":"","id":""}

	# esto descarga el archivo pdb
    #result.append(pdbl.retrieve_pdb_file(id,pdir='./pdb', file_format ='pdb'))
    result["fafafa"] = pdbl.retrieve_pdb_file(id,pdir='./pdb', file_format ='pdb')


	# esto me devuelve tooooda la lista de los atomos de al cadena, no es posible hacerlo con SEQRES, pero se ve interesante para trabajar, lo dejo por las dudas
    #result2.append(PandasPdb().fetch_pdb(id).df['ATOM'])
	
	# convierto a la secuencia primaria
    for record in SeqIO.parse("PDB/pdb"+id+".ent", "pdb-seqres"):
        #print(record.seq)
        #result.append(str(record.seq))
        res =str(record.seq)
        result["seq"] = res

	
	# pasarlo a blast y clustal
	#...
	
	
	# crear el objeto con todo,
	# arr[0] = seq primaria
	# arr[1] = seq sec
	# arr[2] = seq terc
	# arr[3] = seq cuaternaria
	# arr[4] = secuncias conservadas

    result["id"]=id
    json_object = json.dumps(result, indent = 4)
    return (json_object)

if __name__ == '__main__':
    app.run()

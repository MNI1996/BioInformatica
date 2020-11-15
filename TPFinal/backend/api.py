import flask
from flask import request, jsonify
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.PDB import *
from biopandas.pdb import PandasPdb

app = flask.Flask(__name__)
app.config["DEBUG"] = True


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
    result = []
    pdbl = PDBList()
	
	# esto descarga el archivo pdb
    result.append(pdbl.retrieve_pdb_file(id,pdir='./pdb', file_format ='pdb'))
	
	# esto me devuelve tooooda la lista de los atomos de al cadena, no es posible hacerlo con SEQRES, pero se ve interesante para trabajar, lo dejo por las dudas
    #result2.append(PandasPdb().fetch_pdb(id).df['ATOM'])
	
	# convierto a la secuencia primaria
    for record in SeqIO.parse("PDB/pdb"+id+".ent", "pdb-seqres"):
        #print(record.seq)
        result.append(str(record.seq))

	
	# pasarlo a blast y clustal
	#...
	
	
	# crear el objeto con todo,
	# arr[0] = seq primaria
	# arr[1] = seq sec
	# arr[2] = seq terc
	# arr[3] = seq cuaternaria
	# arr[4] = secuncias conservadas

    result.append(id)
	
	
    return jsonify(result)

app.run()

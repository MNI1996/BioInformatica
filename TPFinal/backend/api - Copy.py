import flask
import json
import os
import Bio

from flask import request, jsonify
from flask_cors import CORS, cross_origin
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.PDB import *
#from biopandas.pdb import PandasPdb
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
import subprocess

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["CORS_HEADERS"] = "Content-Type"
CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return	 "<h1>Prueba.</p>"

# el path debería ser /pdb?id=XXXX donde XXXX representa el código de cuatro letras de la proteina
@app.route('/pdb', methods=['GET'])
@cross_origin()
def getPDB():
    if 'id' in request.args:
        id = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    result={"fafafa":"","seq":"","id":""}

    pdbl = PDBList()
	# esto descarga el archivo pdb
    #result.append(pdbl.retrieve_pdb_file(id,pdir='./pdb', file_format ='pdb'))
    owd = os.getcwd()
    output_pdb = os.path.join(owd, "backend")
    output_pdb = os.path.join(output_pdb, "pdb")
    result["fafafa"] = pdbl.retrieve_pdb_file(id,pdir= output_pdb, file_format ='pdb')

	# esto me devuelve tooooda la lista de los atomos de al cadena, no es posible hacerlo con SEQRES, pero se ve interesante para trabajar, lo dejo por las dudas
    #result2.append(PandasPdb().fetch_pdb(id).df['ATOM'])
	
	# convierto a la secuencia primaria
    pdb_dw = os.path.join(output_pdb, "pdb"+id+".ent")
    
    for record in SeqIO.parse(pdb_dw, "pdb-seqres"):
        res =str(record.seq)
        result["seq"] = res
    
    #HOMOLOGAS con blast
    # convert to fasta section
    fasta_path = os.path.join(owd, "backend")
    fasta_path = os.path.join(fasta_path, "fasta")
    if not os.path.exists(fasta_path):
        os.mkdir(fasta_path)
    
    base_fasta_file = os.path.join(fasta_path, id+".fasta")
    out_blast_file = os.path.join(fasta_path, id+".blast") #fasta_path+'\'+id+".blast"
    #print(base_fasta_file)
    #print(out_blast_file)

    """esto no se usa por ahora...
    cline = NcbiblastpCommandline(query=base_fasta_file, db='pdb', evalue=0.1, remote=True, num_alignments = 3, ungapped = False, out=out_blast_file)
    cline = NcbiblastpCommandline(query=base_fasta_file, db="pdb", evalue=0.001, remote=True, ungapped=True, out=out_blast_file, comp_based_stats = '0', num_alignments = 20)
    cline()"""

    #result_handle = NCBIWWW.qblast(program="blastp", database="pdb", sequence=result["seq"]) #, word_size=7, descriptions= 10, alignments = 10, format_type ="text")
    #blast = "output.xml"

    blast_path = os.path.join(owd, "backend")
    blast_path = os.path.join(blast_path, "blast")
    blast_path = os.path.join(blast_path, "out_blast_file.xml")
    if not os.path.exists(blast_path):
        os.mkdir(blast_path)

    #blast_path = os.path.join(blast_path, 'out_blast_file.xml') #"pdb"+id+".ent")
    s = "blastp -query ./backend/db/1.fasta -out ./backend/blast/out_blast_file.xml -db ./backend/db/pdbaa -evalue 0.001 -outfmt 5"
    #s = "blastp -query ./backend/db/1.fasta -out "+ blast_path + "-db ./backend/db/pdbaa -evalue 0.001 -outfmt 5"
    os.system(s)

    #print(blast_path)

    blast_records = NCBIXML.parse(open(blast_path))

    file = open(base_fasta_file, "w") 
    for blast_record in blast_records:
        id= 0 #ver de poner id real
        for alignment in blast_record.alignments:
            file.writelines("> " + str(id)) 
            file.writelines("\n")
            file.writelines(str(alignment.hsps[0].query)) 
            file.writelines("\n")
            id = id + 1

    file.close() 
    

    result["id"]=id
    json_object = json.dumps(result, indent = 4)
    return (json_object)

if __name__ == '__main__':
    app.run()
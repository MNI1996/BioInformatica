import flask
import json
import os
import Bio

from flask import request, jsonify, Response
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
from flask_restful import abort

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["CORS_HEADERS"] = "Content-Type"
def createRoute(app) :
    app.add_resources("/pdbSearch")


CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return	 "<h1>Prueba.</p>"

# el path debería ser /pdb?id=XXXX donde XXXX representa el código de cuatro letras de la proteina
@app.route('/pdbSearch')
@cross_origin()
def post()-> Response:
    result={"fafafa":"","seq":"","id":""}

    pdbl = PDBList()
	# esto descarga el archivo pdb
    #result.append(pdbl.retrieve_pdb_file(id,pdir='./pdb', file_format ='pdb'))
    result["fafafa"] = pdbl.retrieve_pdb_file(id,pdir='./pdb', file_format ='pdb')


	# esto me devuelve tooooda la lista de los atomos de al cadena, no es posible hacerlo con SEQRES, pero se ve interesante para trabajar, lo dejo por las dudas
    #result2.append(PandasPdb().fetch_pdb(id).df['ATOM'])
	
	# convierto a la secuencia primaria  
    for record in SeqIO.parse("PDB/pdb"+id+".ent", "pdb-seqres"):
        res =str(record.seq)
        result["seq"] = res
 
    #HOMOLOGAS con blast
    """esto no se usa por ahora...
    cline = NcbiblastpCommandline(query=base_fasta_file, db='pdb', evalue=0.1, remote=True, num_alignments = 3, ungapped = False, out=out_blast_file)
    cline = NcbiblastpCommandline(query=base_fasta_file, db="pdb", evalue=0.001, remote=True, ungapped=True, out=out_blast_file, comp_based_stats = '0', num_alignments = 20)
    cline()"""

    #result_handle = NCBIWWW.qblast(program="blastp", database="pdb", sequence=result["seq"]) #, word_size=7, descriptions= 10, alignments = 10, format_type ="text")
    blast = "output.xml"
    
    #save_clk = open(blast, "w")
    #save_clk.write(result_handle.read())    
    #save_clk.close()

    blast_records = NCBIXML.parse(open(blast))

    # convert to fasta section
    owd = os.getcwd()
    if not os.path.exists("./fasta"):
        os.mkdir("./fasta")

    base_fasta_file = "./fasta/"+id+".fasta"
    out_blast_file = "./fasta/"+id+".blast"

    #Creo el archivo fasta con contenido
    file = open(base_fasta_file, "w") 
    
    for blast_record in blast_records:
        id= 0 #ver de poner id real
        for alignment in blast_record.alignments:
            file.writelines("> " + str(id)) 
            file.writelines("\n")
            file.writelines(str(alignment.hsps[0].query)) 
            file.writelines("\n")
            id = id + 1
            #print(str(alignment.hsps[0].query))

    file.close()   
    
    
    #pasado a clustal, genera dos archivos uno .aln donde está alineado y un .dnd que es el arbol
    clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
    clustalw_cline = ClustalwCommandline(cmd = clustalw_exe, infile=base_fasta_file, output=fasta)
    clustalw_cline() 

    #out_file = "./fasta/clustal"+id+".fasta"
    #clustalomega_cline = ClustalOmegaCommandline(infile=base_fasta_file, outfile=out_file, verbose=True, auto=True, force=True)
    #clustalomega_cline()
    #print(str(clustalomega_cline))
    #result.append(str(clustalomega_cline))
	
	
	# crear el objeto con todo,
    # result["id"]=id
	# result["seq"] = seq primaria
	# result["blast"] =
	# result["clustal"] =

    result["id"]=id
    json_object = json.dumps(result, indent = 4)
    return (json_object)

if __name__ == '__main__':
    app.run()

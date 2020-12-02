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
import logomaker
import subprocess

app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["CORS_HEADERS"] = "Content-Type"
CORS(app)

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
    
    #identity = float(data["identity"]) if str(data["identity"]).strip()!="" or not data["identity"]  else 39.9
    identity = float(validateField(data, "identity", 39.9))
    identity = identity if identity > 0 else 39.9
    num_align = int(validateField(data, "num_align", 5)) 
    num_align = num_align if num_align > 0 else 5
    chain = validateField(data, "chain", "A")
    e_value = float(data["e_value"])
    db = validateField(data, "db", "pdb")
    word_size = int(data["word_size"])
    gapopen = int(data["gapopen"])

    # esto descarga el archivo pdb
    #result.append(pdbl.retrieve_pdb_file(id,pdir='./pdb', file_format ='pdb'))
    owd = os.getcwd()
    output_pdb = os.path.join(owd, "backend")
    output_pdb = os.path.join(output_pdb, "pdb")
    pdbl = PDBList()
    result["fafafa"] = pdbl.retrieve_pdb_file(id,pdir= output_pdb, file_format ='pdb')
	
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

    blast_path = os.path.join(owd, "backend")
    blast_path = os.path.join(blast_path, "blast")
    if not os.path.exists(blast_path):
        os.mkdir(blast_path)
    blast_path = os.path.join(blast_path, "out_blast_file.fa")
    
    #blast_path = "./backend/blast/out_blast_file.fa"
    db_path = os.path.join(owd, "backend")
    db_path = os.path.join(db_path, "db")
    if db == "pdb":
        db_path = "./backend/db/pdbaa"

    #creo primero el archivo fasta con las ecuencia de la proteina pasada en el json correspondiente al argumento id
    with open(base_fasta_file, "w") as file:
        file.writelines("> " + str(id))
        file.writelines("\n")
        file.writelines(str(result["seq"]))
        file.writelines("\n")
        file.close()

    s = "blastp -query " + base_fasta_file + " -out " + blast_path + " -db " + db_path + " -evalue " + str(e_value) + " -outfmt 5"
    os.system(s)

    blast_records = NCBIXML.parse(open(blast_path))
    #abro el archivo donde voy a guardar el fasta post blast con las secuencias homólogas
    file = open(base_fasta_file, "w")

    #recorre el archivo devuelto y obtengo las homólogas que cumplen la identidad pasada por argumento correspondiente al campo identity
    for blast_record in blast_records:
        sorted_aligntments = []
        for alignment in blast_record.alignments:
            title = str(alignment.title)
            title = title[4]+title[5]+title[6]+title[7]
            identities = alignment.hsps[0].identities
            align_length = alignment.hsps[0].align_length
            porcent =  identities / align_length * 100
            if (porcent > identity):
                sorted_aligntments.append((title, alignment.hsps[0].query, porcent))
        sorted_aligntments.sort(key=lambda x: x[1])
        reversed_alignments = sorted_aligntments[::-1]

    #abro el archivo donde voy a guardar las n secuencias correspondiente al argumento pasado en el json del campo num_align
    # en el fasta para luego ser tomado por clustal
    id = 0
    """cada elemento de la lista reversed_alignments son tripletas 
        cada uno compuesto por la sig estructura (id, seq, porcentaje_identidad)
        por eso el [0] me devuelve el id, el [1] la seq y el [2] no lo uso, no es necesario para el fasta
    """
    while id < num_align:
        file.writelines("> " + str(reversed_alignments[id][0]) )
        file.writelines("\n")
        file.writelines(str(reversed_alignments[id][1]))
        file.writelines("\n")
        id = id + 1  

    file.close() 

    clustal_output_path = os.path.join(owd, "backend")
    clustal_output_path = os.path.join(clustal_output_path, "clustal")
    if not os.path.exists(clustal_output_path):
        os.mkdir(clustal_output_path)
    clustal_output_path = os.path.join(clustal_output_path, "out_clustal_file.fa")
    
    clustalw_cline = ClustalwCommandline(cmd = clustalw_exe, infile=base_fasta_file, outfile= clustal_output_path, output="clustal")
    clustalw_cline() 

    records = SeqIO.parse(clustal_output_path, "clustal")
    seqs= []
    for record in records:
        seq = (str(record.description), str(record.seq))
        seqs.append(seq)
    print(str(seqs))


    json_object = json.dumps(result, indent = 4)
    return (json_object)

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
    if not os.path.exists(blast_path):
        os.mkdir(blast_path)
    blast_path = os.path.join(blast_path, "out_blast_file.fa")

    #blast_path = os.path.join(blast_path, 'out_blast_file.xml') #"pdb"+id+".ent")
    s = "blastp -query ./backend/db/1.fasta -out ./backend/blast/out_blast_file.fa -db ./backend/db/pdbaa -evalue 0.001 -outfmt 5"
    #s = "blastp -query ./backend/db/1.fasta -out "+ blast_path + "-db ./backend/db/pdbaa -evalue 0.001 -outfmt 5"
    os.system(s)

    #print(blast_path)

    blast_records = NCBIXML.parse(open(blast_path))

    file = open(base_fasta_file, "w") 
    for blast_record in blast_records:
        sorted_aligntments = []
        for alignment in blast_record.alignments:
            identities = alignment.hsps[0].identities
            align_length = alignment.hsps[0].align_length
            porcent =  identities / align_length * 100

            if (porcent > 39.9):
                sorted_aligntments.append((alignment.hsps[0].query, porcent))
        sorted_aligntments.sort(key=lambda x: x[1])
        reversed_alignments = sorted_aligntments[::-1]

    id = 0
    while id < 5:
        file.writelines("> " + str(id)) 
        file.writelines("\n")
        file.writelines(str(reversed_alignments[id][0])) 
        file.writelines("\n")
        id = id + 1  

    file.close()  
    
    #pasado a clustal, genera dos archivos uno .aln donde está alineado y un .dnd que es el arbol
    clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
    clustal_output_path = os.path.join(owd, "backend")
    clustal_output_path = os.path.join(clustal_output_path, "clustal")
    if not os.path.exists(clustal_output_path):
        os.mkdir(clustal_output_path)
    clustal_output_path = os.path.join(clustal_output_path, "out_clustal_file.fa")

    clustalw_cline = ClustalwCommandline(cmd = clustalw_exe, infile=base_fasta_file, outfile= clustal_output_path, output="fasta")
    clustalw_cline() 


    result["id"]=id
    json_object = json.dumps(result, indent = 4)
    return (json_object)

if __name__ == '__main__':
    app.run()

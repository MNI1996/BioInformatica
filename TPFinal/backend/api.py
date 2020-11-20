import flask
import os
from flask import request, jsonify
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.PDB import *
#from biopandas.pdb import PandasPdb
from Bio.Align.Applications import ClustalOmegaCommandline
from Bio import AlignIO
from Bio.Align.Applications import ClustalwCommandline
from Bio.Blast.Applications import NcbiblastpCommandline

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

	# convert to fasta
    owd = os.getcwd()
    if not os.path.exists("./fasta"):
        os.mkdir("./fasta")  

    base_fasta_file = "./fasta/"+id+".fasta"
    out_blast_file = "./fasta"+id+".blast"
    file = open(base_fasta_file, "w") 
    file.writelines("> "+id)
    file.writelines("\n")
    file.writelines(str(record.seq)) 
    file.writelines("\n")
    file.close()

    #HOMOLOGAS
    
    #cline = ""
    
    """try:
        #cline = NcbiblastpCommandline(query=str(record.seq), db="nr", evalue=0.001, remote=True, ungapped=True, out=out_blast_file)
        cline = NcbiblastpCommandline(cmd='blastp', query=str(record.seq),
            db='nr', evalue=0.001, remote=True, ungapped=True, num_alignments = 10, out=out_blast_file)
        cline()
        #print(cline)
    except: 
        print("Ups...")"""
    blastp_path = r"C:\Program Files\NCBI\blast-2.11.0+\bin\blastp.exe"
    cline = NcbiblastpCommandline(cmd=blastp_path, query=base_fasta_file,
            db='pdb', evalue=0.001, remote=True,num_alignments = 3, out=out_blast_file)
    cline()
    print(cline())

    """ ESTO ES HARDCODING GROSO PARA USAR HOMOLOGAS
    file.writelines(">NP_001183974.1 cytochrome c [Canis lupus familiaris]")
    file.writelines("\n")
    file.writelines("MGDVEKGKKIFVQKCAQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGFSYTDANKNKGITWGEETLMEYLE")
    file.writelines("\n")
    file.writelines("NPKKYIPGTKMIFAGIKKTGERADLIAYLKKATKE")
    file.writelines("\n")

    file.writelines(">NP_477164.1 cytochrome c distal, isoform A [Drosophila melanogaster]")
    file.writelines("\n")
    file.writelines("MGSGDAENGKKIFVQKCAQCHTYEVGGKHKVGPNLGGVVGRKCGTAAGYKYTDANIKKGVTWTEGNLDEY")
    file.writelines("\n")
    file.writelines("LKDPKKYIPGTKMVFAGLKKAEERADLIAFLKSNK")
    file.writelines("\n")

    file.writelines(">NP_001157486.1 cytochrome c [Equus caballus]")
    file.writelines("\n")
    file.writelines("MGDVEKGKKIFVQKCAQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGFSYTDANKNKGITWKEETLMEYLE")
    file.writelines("\n")
    file.writelines("NPKKYIPGTKMIFAGIKKKTEREDLIAYLKKATNE")
    file.writelines("\n")

    file.writelines(">NP_001072946.1 cytochrome c [Gallus gallus]")
    file.writelines("\n")
    file.writelines("MGDIEKGKKIFVQKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAEGFSYTDANKNKGITWGEDTLMEYLE")
    file.writelines("\n")
    file.writelines("NPKKYIPGTKMIFAGIKKKSERVDLIAYLKDATSK")
    file.writelines("\n")

    file.writelines(">AEP27192.1 cytochrome c [Gorilla gorilla]")
    file.writelines("\n")
    file.writelines("MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLE")
    file.writelines("\n")
    file.writelines("NPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE")
    file.writelines("\n")
     
    file.writelines(">NP_061820.1 cytochrome c [Homo sapiens]")
    file.writelines("\n")
    file.writelines("MGDVEKGKKIFIMKCSQCHTVEKGGKHKTGPNLHGLFGRKTGQAPGYSYTAANKNKGIIWGEDTLMEYLE")
    file.writelines("\n")
    file.writelines("NPKKYIPGTKMIFVGIKKKEERADLIAYLKKATNE")
    file.writelines("\n")

    file.close()
    
    for record in SeqIO.parse("./fasta/1UBQ.fasta", "fasta"):
        print(record)

    #pasado a clustal, genera dos archivos uno .aln donde está alineado y un .dnd que es el arbol
    #clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
    clustalw_cline = ClustalwCommandline(infile=base_fasta_file)
    """

    #PROBAR QUE HACE
    #print(clustalw_cline)
    #align = AlignIO.read(str(cline), "clustal")
    #result.append(align)

	# pasarlo a blast y clustal
    in_file = "./fasta/"+id+"alineado.fasta"
    out_file = "./fasta/clustal"+id+".fasta"
    #clustalomega_cline = ClustalOmegaCommandline(infile=base_fasta_file, outfile=out_file, verbose=True, auto=True, force=True)
    #clustalomega_cline()
    #print(str(clustalomega_cline))
    #result.append(str(clustalomega_cline))
	
	
	# crear el objeto con todo,
	# arr[0] = seq primaria
	# arr[1] = seq sec
	# arr[2] = seq terc
	# arr[3] = seq cuaternaria
	# arr[4] = secuncias conservadas

    result.append(id)
	
	
    return jsonify(result)

app.run(port=5001)

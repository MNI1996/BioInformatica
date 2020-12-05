import os

from Bio import SeqIO
from Bio.PDB import PDBList


class PDBService:

    def __init__(self):
        output_pdb=""
        owd = os.getcwd()
        self.output_pdb = os.path.join(owd, "backend")
        self.output_pdb = os.path.join(self.output_pdb, "pdb")


    def getPDB(self,id):
    # esto descarga el archivo pdb
    #result.append(pdbl.retrieve_pdb_file(id,pdir='./pdb', file_format ='pdb'))
        pdbl = PDBList()
        return pdbl.retrieve_pdb_file(id,pdir= self.output_pdb, file_format ='pdb')

    def converToSequence(self,id):
    # convierto a la secuencia primaria
        pdb_dw = os.path.join(self.output_pdb, "pdb"+id+".ent")

        for record in SeqIO.parse(pdb_dw, "pdb-seqres"):
            res =str(record.seq)
        return res
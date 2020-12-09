import os

from Bio import SeqIO
from Bio.PDB import PDBList


class PDBService:

    def __init__(self):
        self.output_pdb=""
        owd = os.getcwd()
        #self.output_pdb = os.path.join(owd, "backend")
        self.output_pdb = os.path.join(owd, "pdb")


    def getPDB(self,id):
        pdbl = PDBList()

        return pdbl.retrieve_pdb_file(id,pdir= self.output_pdb, file_format ='pdb')

    def converToSequence(self,id):
        pdb_dw = os.path.join(self.output_pdb, "pdb"+id+".ent")

        for record in SeqIO.parse(pdb_dw, "pdb-seqres"):
            res =str(record.seq)
        return res

    def getSequence(self, id):
        pdbl = PDBList()
        pdbl.retrieve_pdb_file(id, pdir=self.output_pdb, file_format='pdb')

        return self.converToSequence(id)

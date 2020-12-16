import os

from Bio import SeqIO
from Bio.PDB import PDBList
"""
from backend.exceptions.ChainPDBDoesNotExistException import ChainPDBDoesNotExistException
from backend.exceptions.PDBDoesNotExistException import PDBDoesNotExistException
"""
from TPFinal.backend.exceptions.ChainPDBDoesNotExistException import ChainPDBDoesNotExistException#
from TPFinal.backend.exceptions.PDBDoesNotExistException import PDBDoesNotExistException


class PDBService:

    def __init__(self):
        self.output_pdb=""
        owd = os.getcwd()
        self.output_pdb = os.path.join(owd, "pdb")


    def getPDB(self,id):
        pdbl = PDBList()
        retStr = pdbl.retrieve_pdb_file(id,pdir= self.output_pdb, file_format ='pdb')
        if not os.path.exists(retStr):
            raise PDBDoesNotExistException();
        return retStr

    def converToSequence(self,id, chain):
        pdb_dw = os.path.join(self.output_pdb, "pdb"+id+".ent")
        seqs= []
        ret = ""
        for record in SeqIO.parse(pdb_dw, "pdb-seqres"):
            seqs.append((str(record.seq), str(record.annotations["chain"])))

        for seq in seqs:
            if seq[1] in chain.upper():
                ret = seq[0]  # me quedo con la posición 0 que es la secuencia de esa cadena
                break

        if ret == "":
            raise ChainPDBDoesNotExistException()
        return ret

    def getSequence(self, id):
        pdbl = PDBList()
        id_protein= id[0: 4]
        chain = id[5]
        pdbl.retrieve_pdb_file(id_protein, pdir=self.output_pdb, file_format='pdb')

        return self.converToSequence(id_protein, chain)

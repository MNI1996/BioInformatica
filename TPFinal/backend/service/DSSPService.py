from Bio.PDB import PDBParser
from Bio.PDB.DSSP import DSSP
import os

class DSSPService:
    def conservate(self, alignments):
        # aligments es una lista de clave valor, que es lo que se devuelve de clustal
        dssps = []
        for align in alignments:
            id_protein = align[0][0: 4]
            chain = align[0][5]
            primary_seq = align[1]
            secondary_seq = self.obtain_dssp(id_protein, chain)
            conservated = self.align(secondary_seq, primary_seq) #llamar a dssp que me traiga la conservación de seq
            result = (align[0], conservated)
            dssps.append(result)

        self._writeFile(dssps)
        return dssps

    def _writeFile(self, dssps):
        path = os.getcwd().replace("backend", "frontend")
        path= path.replace("service", "")
        path = os.path.join(path, "Files" )
        path = os.path.join(path, "Dssp")

        if not os.path.exists(path):
            os.makedirs(path)

        fst_protein = dssps[0][0][0:4]
        path = os.path.join(path, fst_protein+".fa")
        with open(path, "w") as file:
            for dssp in dssps:
                id_protein_chain = str(dssp[0])
                id = id_protein_chain[0:4]
                chain = id_protein_chain[5]
                seq = dssp[1]
                file.writelines("> " + id + "_" + chain)
                file.writelines("\n")
                file.writelines(str(seq))
                file.writelines("\n")
            file.close()

    def align(self, secondary_seq, primary_seq ):

        for index in range(len(primary_seq)):
            if primary_seq[index] == '-':
                secondary_seq[0].insert(index, (1, '-', '_'))

        rst = ''.join([st[2] if not st[2] == '-' else '0' for st in secondary_seq[0]])
        rstf=self.rLG(rst)
        return rstf

    def rLG(self,ls):
        lsf=ls.replace("_","-")
        return lsf

    def obtain_dssp(self, id_protein, chain):
        pdb_path = os.getcwd().replace("service", "pdb")
        os.chdir(pdb_path)
        pdb_file = os.path.join(pdb_path, "pdb")
        pdb_file = os.path.join(pdb_file, 'pdb' + id_protein + '.ent')
        dssp_route = os.getcwd()
        dssp_route = os.path.join(dssp_route, "dssp")
        dssp_route = os.path.join(dssp_route, "dssp-2.0.4-win32.exe")


        p = PDBParser()
        structure = p.get_structure(id_protein, pdb_file)
        model = structure[0]
        dssp = DSSP(model, pdb_file, dssp=dssp_route)
        valid_keys = [key for key in dssp.keys() if key[0] in chain]

        result = [ dssp[key] for key in valid_keys], (valid_keys[:1], valid_keys[-1:])

        return result

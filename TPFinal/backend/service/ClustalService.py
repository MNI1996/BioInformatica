import os
from shutil import copyfile

from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline


class ClustalService:
    def __init__(self):
        self.id = ""
        self.fasta_path=""
        self.owd = os.getcwd()

    def getClustal(self,clustalw_exe,base_fasta_file,id, log_path):
        self.id = id
        clustal_output_path = os.path.join(self.owd, "clustal")
        if not os.path.exists(clustal_output_path):
            os.mkdir(clustal_output_path)
        clustal_output_path = os.path.join(clustal_output_path, id+".fa")

        #self._log(log_path, clustalw_exe, clustal_output_path)

        clustalw_cline = ClustalwCommandline(cmd = clustalw_exe, infile=base_fasta_file, outfile= clustal_output_path, output="fasta")
        clustalw_cline()

        records = SeqIO.parse(clustal_output_path, "fasta")
        seqs= []
        for record in records:
            seq = (str(record.description), str(record.seq))
            seqs.append(seq)

        path = os.getcwd().replace("backend", "frontend")
        path = os.path.join(path, "Files")
        path = os.path.join(path, "Align")
        if not os.path.exists(path):
            os.makedirs(path)
        path = os.path.join(path, self.id + ".txt")
        copyfile(clustal_output_path, path)

        return seqs

    def _log(self, log_path, clustalw_exe, clustal_output_path):
        # leo lo que ha tenía
        with open(log_path, "r") as out_file:
            content = out_file.read()

        # concateno lo viejo con lo nuevo
        with open(log_path, "w") as out_file:
            out_file.writelines(content)
            out_file.writelines("\n")
            out_file.writelines("Clustal command:")
            out_file.writelines("\n")
            out_file.writelines("Clustal path: " + clustalw_exe)
            out_file.writelines("\n")
            out_file.writelines("Output path: " + clustal_output_path)
            out_file.writelines("\n")
            out_file.writelines("Output format: fasta")
            out_file.writelines("\n")
            out_file.writelines(
                "Para ver los parámetros por defecto consultar con https://biopython.org/docs/1.75/api/Bio.Align.Applications.html#Bio.Align.Applications.ClustalwCommandline")
            out_file.close()
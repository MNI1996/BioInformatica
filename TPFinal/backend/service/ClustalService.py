import os

from Bio import SeqIO
from Bio.Align.Applications import ClustalwCommandline


class ClustalService:
    def __init__(self):
        fasta_path=""
        owd = os.getcwd()

    def getClustal(self,clustalw_exe,base_fasta_file):
        clustal_output_path = os.path.join(self.owd, "backend")
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
        return seqs
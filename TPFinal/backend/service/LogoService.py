import logomaker as lm
import matplotlib.pyplot as plt
plt.ion()

class LogoService:

    def logoMaker(id):
        with lm.open_example_datafile('crp_sites.fa', print_description=False) as f:
            raw_seqs = f.readlines()
        seqs = [seq.strip() for seq in raw_seqs if ('#' not in seq) and ('>') not in seq]
        # preview s equences
        print('There are %d sequences, all of length %d'%(len(seqs), len(seqs[0])))
        counts_mat = lm.alignment_to_matrix(seqs)
        counts_mat.head()
        lm.Logo(counts_mat)
        plt.savefig("frontend/Images/dssp/"+id+".png")
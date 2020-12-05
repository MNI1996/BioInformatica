import logomaker as lm
import matplotlib.pyplot as plt
import pandas as pd

plt.ion()


class LogoService:


    def logoMaker(self,pseqs,id):
        seqs=[]
        for i in pseqs:
            seqs.append(i[1])
        crp_counts_df = lm.alignment_to_matrix(sequences=seqs, to_type='counts', characters_to_ignore='.-X')
        crp_counts_m=lm.transform_matrix(crp_counts_df, from_type='counts',to_type='probability')
        lm.Logo(crp_counts_m)
        plt.savefig("frontend/Images/dssp/"+id+".png")

#prob_mat = lm.transform_matrix(crp_df, from_type='counts', to_type='probability') characters_to_ignore='.-X'
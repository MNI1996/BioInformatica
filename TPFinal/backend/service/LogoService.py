import logomaker as lm
import matplotlib.pyplot as plt
import os

plt.ion()


class LogoService:


    def logoMaker(self,pseqs,id):
        seqs=[]
        for i in pseqs:
            seqs.append(i[1])
        crp_counts_df = lm.alignment_to_matrix(sequences=seqs, to_type='counts', characters_to_ignore='.-X')
        #crp_counts_m=lm.transform_matrix(crp_counts_df, from_type='counts',to_type='probability')
        #lm.Logo(crp_counts_m)
        lm.Logo(crp_counts_df)
        img_path = os.getcwd().replace("backend", "frontend")
        os.chdir(img_path)
        img_path = os.path.join(img_path, "Images")
        img_path = os.path.join(img_path, "dssp")
        if not os.path.exists(img_path):
            os.mkdir(img_path)
        plt.savefig(img_path+"/"+id+".png")

#prob_mat = lm.transform_matrix(crp_df, from_type='counts', to_type='probability') characters_to_ignore='.-X'
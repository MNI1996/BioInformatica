import logomaker as lm
import matplotlib.pyplot as plt
import os

plt.ion()


class LogoService:

    def parseSeq( self,seq) :
        charperline = (len(seq) / 30) + 1
        cutvalue = int(len(seq) /int(charperline))
        rsf = []
        for i in range(0,int(charperline)):
            start = (int(charperline) * i)
            res = seq[ start: start + cutvalue]
            rsf.append(res)
        return rsf

    def listHomologas(self,tuplas) :
        listFinal = []
        for i in range(0, len(tuplas)) :
            listReturn = []
            res = self.parseSeq(tuplas[i][1])
            for j in range (0,len(res)):
                par = res[j]
                listReturn.append(par)

            listFinal.append(listReturn)

        al_return = self.transposedMatrix(listFinal)
        return al_return

    def transposedMatrix(self,lists):
        resList = []
        for i in range(0, len(lists[0])) :
            auxList = []
            for j in range(0, len(lists)):
                elem = lists[j][i]
                auxList.append(elem)
            resList.append(auxList)
        return resList

    def multiLogo(self,pseqs,id):
        n = 0
        lsSeqs = self.listHomologas(pseqs)
        for i in lsSeqs:
            self.logoMaker(i,id,n)
            n += 1

        return n

    def logoMaker(self, pseqs, idP, n):
        crp_counts_df = lm.alignment_to_matrix(sequences=pseqs, to_type='counts', characters_to_ignore='.-X')
        lm.Logo(crp_counts_df)
        img_path = os.getcwd().replace("backend", "frontend")
        os.chdir(img_path)
        img_path = os.path.join(img_path, "Images")
        img_path = os.path.join(img_path, idP)
        img_path = os.path.join(img_path, "Align")
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        plt.savefig(img_path+"/"+str(n)+".png")


    def multiLogoS(self,pseqs,id):
        n = 0
        lsSeqs = self.listHomologas(pseqs)
        for i in lsSeqs:
            self.logoMakerS(i,id,n)
            n += 1

        return n

    def logoMakerS(self, pseqs, idP, n):
        crp_counts_df = lm.alignment_to_matrix(sequences=pseqs, to_type='counts', characters_to_ignore='.-X')
        lm.Logo(crp_counts_df)
        img_path = os.getcwd().replace("backend", "frontend")
        os.chdir(img_path)
        img_path = os.path.join(img_path, "Images")
        img_path = os.path.join(img_path, idP)
        img_path = os.path.join(img_path, "Dssp")
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        plt.savefig(img_path+"/"+str(n)+".png")
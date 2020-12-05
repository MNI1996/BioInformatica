import os

from Bio.Blast import NCBIXML


class BlastService:
    def __init__(self):
        base_fasta_file=""
        fasta_path=""
        owd = os.getcwd()

    def getBaseFasta(self):
        return self.base_fasta_file

    def getBlast(self,id,seq,db,num_align,e_value,identity):
        #HOMOLOGAS con blast
        # convert to fasta section
        self.fasta_path = os.path.join(self.owd, "backend")
        self.fasta_path = os.path.join(self.fasta_path, "fasta")
        if not os.path.exists(self.fasta_path):
            os.mkdir(self.fasta_path)

        self.base_fasta_file = os.path.join(self.fasta_path, id+".fasta")
        out_blast_file = os.path.join(self.fasta_path, id+".blast") #fasta_path+'\'+id+".blast"

        blast_path = os.path.join(self.owd, "backend")
        blast_path = os.path.join(blast_path, "blast")
        if not os.path.exists(blast_path):
            os.mkdir(blast_path)
        blast_path = os.path.join(blast_path, "out_blast_file.fa")

        #blast_path = "./backend/blast/out_blast_file.fa"
        db_path = os.path.join(self.owd, "backend")
        db_path = os.path.join(db_path, "db")
        if db == "pdb":
            db_path = os.path.join(db_path, "pdbaa")

        #creo primero el archivo fasta con las ecuencia de la proteina pasada en el json correspondiente al argumento id
        with open(base_fasta_file, "w") as file:
            file.writelines("> " + str(id))
            file.writelines("\n")
            file.writelines(str(seq))
            file.writelines("\n")
            file.close()

        s = "blastp -query " + base_fasta_file + " -out " + blast_path + " -db " + db_path + " -evalue " + str(e_value) + " -outfmt 5"
        os.system(s)

        blast_records = NCBIXML.parse(open(blast_path))
        #abro el archivo donde voy a guardar el fasta post blast con las secuencias homólogas
        file = open(base_fasta_file, "w")

        #recorre el archivo devuelto y obtengo las homólogas que cumplen la identidad pasada por argumento correspondiente al campo identity
        for blast_record in blast_records:
            sorted_aligntments = []
            for alignment in blast_record.alignments:
                title = str(alignment.title)
                title = title[4]+title[5]+title[6]+title[7]
                identities = alignment.hsps[0].identities
                align_length = alignment.hsps[0].align_length
                porcent = identities / align_length * 100
                if (porcent > identity):
                    sorted_aligntments.append((title, alignment.hsps[0].query, porcent))
            sorted_aligntments.sort(key=lambda x: x[1])
            reversed_alignments = sorted_aligntments[::-1]

        #abro el archivo donde voy a guardar las n secuencias correspondiente al argumento pasado en el json del campo num_align
        # en el fasta para luego ser tomado por clustal
        id = 0
        """cada elemento de la lista reversed_alignments son tripletas 
            cada uno compuesto por la sig estructura (id, seq, porcentaje_identidad)
            por eso el [0] me devuelve el id, el [1] la seq y el [2] no lo uso, no es necesario para el fasta
        """
        while id < num_align:
            file.writelines("> " + str(reversed_alignments[id][0]) )
            file.writelines("\n")
            file.writelines(str(reversed_alignments[id][1]))
            file.writelines("\n")
            id = id + 1

        file.close()
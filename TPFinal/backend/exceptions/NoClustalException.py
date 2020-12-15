class NoClustalException(Exception):

    @classmethod
    def message(self):
        return ("Error: Clustal no existe en el sistema")
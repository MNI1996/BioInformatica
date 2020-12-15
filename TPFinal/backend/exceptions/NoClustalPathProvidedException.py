class NoClustalPathProvidedException(Exception):

    @classmethod
    def message(self):
        return "Falta el path de Clustal"
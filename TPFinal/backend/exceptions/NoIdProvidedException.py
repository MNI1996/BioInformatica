class NoIdProvidedException(Exception):

    @classmethod
    def message(self):
        return "No ingresó código el PDB a analizar"
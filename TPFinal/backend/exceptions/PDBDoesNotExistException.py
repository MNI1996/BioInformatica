class PDBDoesNotExistException(Exception):

    @classmethod
    def message(self):
        return "Código PDB inexistente"
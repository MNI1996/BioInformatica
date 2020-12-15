class ChainPDBDoesNotExistException(Exception):

   @classmethod
   def message(self):
        return "No existe cadena pdb. Verifique y reintente"
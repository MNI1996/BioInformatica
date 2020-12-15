class NoHomologousException(Exception):

    @classmethod
    def message(self):
        return ("Error: Blast no puede encontrar homólogas")
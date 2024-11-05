class Comentario:
    def __init__(self,id,nome,comentario,data):
        self.id = id
        self.nome = nome
        self.comentario = comentario
        self.data = data

    def get_id(self):
        return self.id
    
    def get_nome(self):
        return self.nome
    
    def get_comentario(self):
        return self.comentario
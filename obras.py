class Obra:
    def __init__(self,id,foto,artista,nome,descricao):
        self.id = id
        self.foto = foto
        self.artista = artista
        self.nome = nome
        self.descricao = descricao

    def get_id(self):
        return self.id
    
    def get_foto(self):
        return self.foto
    
    def get_artista(self):
        return self.artista
    
    def get_nome(self):
        return self.nome
    
    def get_descricao(self):
        return self.descricao
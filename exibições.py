class Exibicao:
    def __init__(self,id,local_exibicao,foto,historia_local_exibicao):
        self.id = id
        self.local_exibicao = local_exibicao
        self.foto = foto
        self.historia_local_exibicao = historia_local_exibicao

    def get_id(self):
        return self.id
    
    def get_local_exibicao(self):
        return self.local_exibicao
    
    def get_foto(self):
        return self.foto
    
    def get_historia_local_exibicao(self):
        return self.historia_local_exibicao
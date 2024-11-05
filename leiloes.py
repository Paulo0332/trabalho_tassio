class Leilao:
    def __init__(self,id,primeiro_lance,ultimo_lance,maior_lance):
        self.id = id
        self.primeiro_lance = primeiro_lance
        self.ultimo_lance = ultimo_lance
        self.maior_lance = maior_lance
        

    def get_id(self):
        return self.id
    
    def get_primeiro_lance(self):
        return self.primeiro_lance
    
    def get_ultimo_lance(self):
        return self.ultimo_lance
    
    def get_maior_lance(self):
        return self.maior_lance
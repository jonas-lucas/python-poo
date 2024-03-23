from datetime import datetime

class Pessoa:
    ano_atual = datetime.now().year

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:    # Se estiver comendo
            print(f'{self.nome} não pode falar comendo.')
        elif self.falando:  # Se já estiver falando 
            print(f'{self.nome} já está falando.')
        else:               # Começar a falar
            print(f'{self.nome} está falando sobre {assunto}.')
            self.falando = True

    def parar_falar(self):
        if not self.falando:    # Se não estiver falando
            print(f'{self.nome} não está falando.')
        else:                   # Parar de falar
            print(f'{self.nome} parou de falar.')
            self.falando = False

    def comer(self, alimento):
        if self.falando:    # Se estiver falando
            print(f'{self.nome} não pode comer falando.')
        elif self.comendo:  # Se já estiver comendo
            print(f'{self.nome} já está comendo.')        
        else:               # Começar a comer
            print(f'{self.nome} está comendo {alimento}.')
            self.comendo = True

    def parar_comer(self):
        if not self.comendo:    # Se não estiver comendo
            print(f'{self.nome} não está comendo.')
        else:                   # Parar de comer
            print(f'{self.nome} parou de comer.')
            self.comendo = False

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade

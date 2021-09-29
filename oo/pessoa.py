class Pessoa:
    def __init__(self, nome=None, idade=18):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa('Amorim')
    print(Pessoa.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Gabriel'
    print(p.nome)
    print(p.idade)

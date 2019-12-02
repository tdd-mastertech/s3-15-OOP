# Enunciado
# Criar uma classe cliente com seus respectivos dados no init: nome, email, rg
# Quando realizar o print no cliente criado, aparecer a seguinte mensagem:
# "Olá {nome do cliente}, você foi cadastrado com sucesso em nosso sistema"


class funcionario:
    salario = 2000
    aumento_salario = int(input('digite a quantidade de aumento: '))

    def __init__(self, nome, email, rg):
        self.nome = nome
        self.email = email
        self.rg = rg

    def __str__(self):
        return f'Olá {self.nome}, você foi cadastrado com sucesso'

    @classmethod
    def aumentar_salario(item):
        return item.salario.__add__(item.aumento_salario)

c1 = funcionario(nome='José', email='jose@bol.com', rg='3409309430')

print(c1)
print(c1.aumentar_salario())


from ControleFinanceiro import ControleFinanceiro
from Despesa import Despesa
from Receita import Receita

class Pessoa:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.controle_financeiro = ControleFinanceiro()

    def iniciar_controle_financeiro(self):
        # Inicializar o controle financeiro
        pass
#=====Criando a pessoa======
Mikael = Pessoa('Mikael', 'mikaeljunior.dev@gmail.com')
print(Mikael.nome)

#======Atribuindo suas despesas=====
Gasolina = Despesa( 'Carro', 350.0, '12/01/2024', 'Gasolina')
Mikael.controle_financeiro.adicionar_despesa(Gasolina)

Academia = Despesa( 'Saude', 149.0, '12/01/2024', 'Academia')
Mikael.controle_financeiro.adicionar_despesa(Academia)

Vivo = Despesa( 'Plano_celular', 47.0, '12/01/2024', 'Vivo')
Mikael.controle_financeiro.adicionar_despesa(Vivo)

prime_video = Despesa( 'Streaming', 15.0, '12/01/2024', 'prime_video')
Mikael.controle_financeiro.adicionar_despesa(prime_video)

Aluguel = Despesa( 'Moradia',1300.0, '12/01/2024', 'Aluguel')
Mikael.controle_financeiro.adicionar_despesa(Aluguel)

Mikael.controle_financeiro.exibir_valor_despesa()

#===Atribuindo suas receitas=====
Salario = Receita('Salario', 2900.0, '12/01/2024')
Mikael.controle_financeiro.adicionar_receita(Salario)

vale_refeicao = Receita('Vale_refeicao', 828.30, '12/01/2024')
Mikael.controle_financeiro.adicionar_receita(vale_refeicao)

Mikael.controle_financeiro.exibir_valor_receita()

#=====Consultando seu saldo=====
print(f'Saldo do mikael: {Mikael.controle_financeiro.calcular_saldo()}')

df_despesas = Mikael.controle_financeiro.criar_df_despesas()
print('\nDataFrame de Despesas:')
print(df_despesas)

df_despesas = Mikael.controle_financeiro.criar_df_despesas()
print('\nDataFrame de Despesas:')
print(df_despesas)
from ControleFinanceiro import ControleFinanceiro
from Despesa import Despesa
from Receita import Receita
from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)




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


Cosmeticos = Despesa( 'Saude', 80.0, '12/01/2024', 'Cosmeticos')
Mikael.controle_financeiro.adicionar_despesa(Cosmeticos)


Perfume = Despesa( 'Saude', 175.0, '21/12/2023', 'Perfume')
Mikael.controle_financeiro.adicionar_despesa(Perfume)


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

df_receita = Mikael.controle_financeiro.criar_df_receita()
print('\nDataFrame de Receitas:')
print(df_receita)

@app.route('/')
def index():
    # Criar um gráfico de barras empilhadas

    # Criar um gráfico de barras empilhadas
    plt.figure(figsize=(15, 6))

    # Agrupar por data e categoria e calcular o total gasto por categoria em cada data
    df_grouped = df_despesas.groupby(['Data', 'categoria'])['Valor'].sum().unstack(fill_value=0)
    # Especificar manualmente as cores para cada categoria
    cores_categorias = ['#DCDCDC', '#A9A9A9', '#4F4F4F',  '#FFA500', '#FF8C00', '#FF4500', '#7f7f7f', '#bcbd22', '#17becf']

    # Subplot 1: Gráfico de barras empilhadas
    ax1 = plt.subplot(1, 2, 1)
    df_grouped.plot(kind='bar', stacked=True, color=cores_categorias, ax=ax1)

    # Adicionar as legendas exatas de valor dentro de cada cor
    for container in ax1.containers:
        for i, value in enumerate(container.datavalues):
            if value != 0:
                x_pos = container.patches[i].get_x() + container.patches[i].get_width() / 2
                y_pos = container.patches[i].get_y() + container.patches[i].get_height() / 2

                # Verificar se a largura da legenda é menor que a largura da barra
                if ax1.transData.transform((x_pos, y_pos))[0] < ax1.transAxes.transform((1, 0))[0]:
                    ax1.text(x_pos, y_pos, f'{value:.2f}', ha='center', va='center', fontsize=8, color='black')

    ax1.set_xlabel('Mês/Ano')
    ax1.set_ylabel('Total Gasto')
    ax1.set_title('Despesas por Categoria ao longo do Tempo')
    ax1.legend(title='Categoria', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=0)

    # Subplot 2: Gráfico de pizza com porcentagens e valor total gasto por categoria
    ax2 = plt.subplot(1, 2, 2)
    total_por_categoria = df_despesas.groupby('categoria')['Valor'].sum()

    ax2.pie(total_por_categoria, labels=total_por_categoria.index, autopct='%1.1f%%', colors=cores_categorias, startangle=90)
    ax2.set_title('Porcentagem do Valor Total Gasto por Categoria')

    # Ajustar o layout
    plt.tight_layout()

    img_buf_bar = BytesIO()
    plt.savefig(img_buf_bar, format='png', bbox_inches='tight')
    img_buf_bar.seek(0)
    img_encoded_bar = base64.b64encode(img_buf_bar.getvalue()).decode('utf-8')

    # Salvar o gráfico de pizza em um buffer de bytes
    img_buf_pie = BytesIO()
    plt.savefig(img_buf_pie, format='png', bbox_inches='tight')
    img_buf_pie.seek(0)
    img_encoded_pie = base64.b64encode(img_buf_pie.getvalue()).decode('utf-8')

    # Passar a imagem codificada para o template
    return render_template('index.html', pessoa=Mikael, graph_bar=img_encoded_bar, graph_pie=img_encoded_pie)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port = 8080)
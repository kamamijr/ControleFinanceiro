import pandas as pd 
class ControleFinanceiro:
    def __init__(self):
        self.despesas = []
        self.receitas = []

    def adicionar_despesa(self, despesa):
        # Adicionando despesa à lista de despesas
        self.despesas.append(despesa)
        pass

    def adicionar_receita(self, receita):
        # Adicionando receita à lista de receitas
        self.receitas.append(receita)
        pass
    
    def soma_valor_despesas(self):
        return sum(despesa.valor for despesa in self.despesas)

    def exibir_valor_despesa(self):
        total_despesas = self.soma_valor_despesas()
        print(f'Total de Despesas: {total_despesas}')

    def soma_valor_receitas(self):
        return sum(receita.valor for receita in self.receitas)

    def exibir_valor_receita(self):
        total_receitas = self.soma_valor_receitas()
        print(f'Total de receitas: {total_receitas}')

    def calcular_saldo(self):
        total_receitas = self.soma_valor_receitas()
        total_despesas = self.soma_valor_despesas()
        return round((total_receitas - total_despesas),2)

    def criar_df_despesas(self):
            # Criação de um DataFrame a partir das despesas
            df_despesas = pd.DataFrame({
                'categoria': [despesa.categoria for despesa in self.despesas],
                'Destino': [despesa.destino for despesa in self.despesas],
                'Valor': [despesa.valor for despesa in self.despesas],
                'Data': [despesa.data for despesa in self.despesas]
            })
            return df_despesas
    
    def gerar_relatorio(self):
        # Gerar relatório com gráficos, se necessário
        pass


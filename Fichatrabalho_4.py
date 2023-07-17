# Ficha de trabalho 4

#Estrutura do Menu a ser mostrada ao utilizador:

print()
print("Este código utiliza a biblioteca Pandas para analisar dados sobre o consumo de energia elétrica de vários países e calcular a variação percentual no consumo de energia elétrica em Qualquer País entre 1990 e 2000.")

#1. Importar pandas para tratar dados

import pandas as pd

# Carregar dados do Excel

dados = pd.read_excel('P_Data_Extract_From_World_Development_Indicators.xlsx')
dadossemnan = dados.dropna() #Retirar da lista os valores nulos

#Criação do menu inicial que aparecerá para o utilizador:
 
while True:
    print("\n-----Menu de opções a cerca dos dados-----\n")
    print("1. Ver os dados importados")
    print("2. Filtrar dados por país desejado pelo utilizador calcular a variação percentual")
    print("0. Sair")

    opcao = input("\nEscolha uma opção: ")

#Opções:

    if opcao == "1":
        print("\n\nOs dados importados são:\n")
        print(dadossemnan)

    elif opcao == "2":
        print("\nNesta opção você irá filtrar os dados por um país.")
        pais = input("\nPara realizar esta seleção precisamos de saber mais dados... Digite o nome do país desejado (em inglês)\n").lower()
        dados = dados[['Country Name', '1990 [YR1990]', '2000 [YR2000]']] #Selecionar as colunas no excel
        dados_pais = dados[dados['Country Name'].str.lower() == pais] #Foi utilizado o .str.lower() para converter os dados da tabela case-insensitive
#Exibir dados do país        
        if len(dados_pais) > 0: #Aqui se compara o input do utilizador aos países na base de dados.
            print(f"\nOs dados que deseja para o país: '{pais}' são:")
            print(f"\n{dados_pais}")
            print()
        else:
            print(f"\nErro: O país '{pais}' não foi encontrado nos dados. Verifique que digitou corretamente e repita este passo")
    #Calcular a variação percentual
        consumo_1990 = dados_pais['1990 [YR1990]'].values[0]
        consumo_2000 = dados_pais['2000 [YR2000]'].values[0]

        if consumo_1990 != ".." and consumo_2000 != "..":
            def calcular_variacao_percentual(consumo_inicial, consumo_final): #Definição da função para variação
                return(consumo_final - consumo_inicial) / consumo_inicial * 100
            #Definição das variáveis interpretando os dados como números 
            consumo_1990 = float(consumo_1990)
            consumo_2000 = float(consumo_2000)
            #Chamada da função
            variacao_percentual = calcular_variacao_percentual(consumo_1990, consumo_2000)
            print(f"\nVariação percentual no consumo de energia elétrica em '{pais}' entre 1990 e 2000: {variacao_percentual:.2f}%")
        else:
            print("Como não existem dados deste país, a variação é nula")
               
    elif opcao == "0":
        print("\nPrograma Encerrado. Obrigada\n")
        break

    else:
        print("Não digitou um número dentro dos números das opções do Menu. Por favor repetir")
import os
   
# Comentar várias linhas: Ctrl + /

carros_alugados = []

portifolio = [['Chevrolet Tracker - R$ 120 por dia', 120], 
              ['Chevrolet Onix - R$ 90 por dia', 90],
              ['Chevrolet Spin - R$ 150 por dia', 150],
              ['Hyundai HB20 - R$ 85 por dia', 85],
              ['Hyundai Tucson - R$ 120 por dia', 120],
              ['Fiat Uno - R$ 60 por dia', 60],
              ['Fiat Mobi - R$ 70 por dia', 70],
              ['Fiat Pulse - R$ 130 por dia', 130]]

def mostrar_lista(lista):
    for indice, elemento in enumerate(lista):
        descricao = elemento[0]
        print(f"[{indice}] {descricao}")
        
def alugar_carro():
    print('ALUGAR! Dê uma olhada em nosso portifólio!\n')
    print('======================================')
    mostrar_lista(portifolio)
    print('======================================')
    
    codigo = int(input('Escolha o Código do Carro: '))
    while codigo >= 8:
        codigo = int(input("Digite um Código Válido: "))
    dia = int(input('Escolha por Quantos dias deseja Alugar: \n'))

    os.system('clear')

    valor = portifolio[codigo][1]
    nome = portifolio[codigo][0]
    total = dia * valor
    
    print('======================================')
    print(f"Você escolheu {nome}")
    print(f"O aluguel totalizaria R$ {total} por {dia} dias. Deseja Alugar?")
    print("0 - SIM | 1 - NÂO")

    conf = int(input())
    if conf == 0:
        print(f'Parabéns você alugou o {nome} por {dia} dias!')
        carros_alugados.append(portifolio.pop(codigo))
    
    print("\nLista atualizada")
    print('======================================')
    mostrar_lista(portifolio)

def devolver_carro():
    
    if len(carros_alugados) == 0:
        print('Não há Carros alugados!')
    else:
        print('ALUGADO(S)! Segue a Lista de Carros Alugados! Qual você deseja devolver?\n')
        print('======================================')
        mostrar_lista(carros_alugados)     
        
        codigo = int(input('Escolha o Código do Carro:'))
        while codigo >= 8:
            codigo = int(input("Digite um Código Válido!"))

        print(f'Obrigado por devolver o carro {carros_alugados[codigo][0]}')
        print('======================================')
        portifolio.append(carros_alugados.pop(codigo))

while True:
    os.system('clear')

    print('======================================')
    print('Bem vindo à locadora de Carros!')
    print('======================================\n')
    print('O que deseja fazer?\n')
    print('======================================')
    print('0 - Mostrar Portifólio')
    print('1 - Alugar um Carro')
    print('2 - Devolver um Carro')
    print('3 - Sair')
    print('======================================')

    opcao = int(input())

    os.system('clear')

    if opcao == 0:
        print('======================================')
        mostrar_lista(portifolio)
        print('======================================')

    elif opcao == 1:
        alugar_carro()

    elif opcao == 2:
        devolver_carro()

    elif opcao == 3:
        exit()
        
    elif opcao >= 4:
        print('opção inválida!')

    print('0 - CONTINUAR | 1 - SAIR')
    if int(input()) == 1:
        break
    print('======================================')

    

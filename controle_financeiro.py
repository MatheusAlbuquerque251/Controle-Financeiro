import tkinter as tk
from tkinter import messagebox
import json

movimentacoes = []

janela = tk.Tk()
janela.title("Controle Financeiro")
janela.geometry("500x500")

janela.mainloop()

def carregar_movimentacao():
    try:
        with open('movimentacoes.json', mode='r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)
            movimentacoes.extend(dados)
    except FileNotFoundError:
        pass

def salvar_movimentacao():
    with open('movimentacoes.json', mode='w', encoding='utf-8') as arquivo:
        json.dump(movimentacoes, arquivo, indent=4, ensure_ascii=False)

def adicionar_receita():
    descricao_receita = input('Descrição da Receita: ')

    while True:
        try:
            valor_receita = float(input('Valor: '))
            break
        except ValueError:
            print('\nValor Inválido!\nDigite um número.\n')

    movimentacao = {"tipo": "Receita", "descricao": descricao_receita, "valor": valor_receita}

    movimentacoes.append(movimentacao)
    salvar_movimentacao()

    print('\nReceita adicionada com sucesso!\n')

def adicionar_despesa():
    descricao_despesa = input('Descrição da Despesa: ')

    while True:
        try:
            valor_despesa = float(input('Valor: '))
            break
        except ValueError:
            print('\nValor Inválido!\nDigite um número.\n')
        
    movimentacao = {"tipo": "Despesa", "descricao": descricao_despesa, "valor": valor_despesa}

    movimentacoes.append(movimentacao)
    salvar_movimentacao()

    print('\nDespesa adicionada com sucesso!\n')

def listar_movimentacoes():

    if len(movimentacoes) == 0:
        print('Não existem movimentações para serem listadas')

    else:
        print(' MOVIMENTAÇÕES '.center(50, '='))
        print('\n')

        for movimentacao in movimentacoes:
            print(movimentacao['tipo'], '-', movimentacao['descricao'], '-', movimentacao['valor'])

        print('\n')

def remover_movimentacao():
    descricao = input('Descrição da movimentação a remover: ')

    for movimentacao in movimentacoes:
        if movimentacao['descricao'] == descricao:
            movimentacoes.remove(movimentacao)
            salvar_movimentacao()
            print('Removida com sucesso!')
            return
        
    print('Movimentação não encontrada!\n')

def calcular_saldo():
    total_receitas = 0
    total_despesas = 0

    for movimentacao in movimentacoes:
        if movimentacao['tipo'] == "Receita":
            total_receitas += movimentacao['valor']
        elif movimentacao['tipo'] == "Despesa":
            total_despesas += movimentacao['valor']
        else:
            print('Movimentação não existe!')

    saldo = total_receitas - total_despesas

    print(' SALDO '.center(50,'='))
    print('\n')
    print(f'Total de Receitas: {total_receitas:.2f}')
    print(f'Total de Despesas: {total_despesas:.2f}')
    print(f'Saldo: {saldo:.2f}\n')

def menu():
    print(' CONTROLE FINANCEIRO '.center(50, '='))
    print('\n')

    print(' 1 - Adicionar Receita \n 2 - Adicionar Despesa \n 3 - Listar Movimentações \n 4 - Remover Movimentação \n 5 - Calcular o Saldo \n 6 - Sair\n')


carregar_movimentacao()

while True:

    menu()

    while True:
        try:
            opcao = int(input('Selecione uma opção digitando um número: '))
            print('\n')
            break
        except ValueError:
            print('\nValor Inválido!\nDigite um número.\n')

    if opcao == 1:
        adicionar_receita()
    elif opcao == 2:
        adicionar_despesa()
    elif opcao == 3:
        listar_movimentacoes()
    elif opcao == 4:
        remover_movimentacao()
    elif opcao == 5:
        calcular_saldo()
    elif opcao == 6:
        salvar_movimentacao()
        break
    else:
        print(' Opção inválida! \n Digite novamente.\n')
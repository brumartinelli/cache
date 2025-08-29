from Tarefa import Tarefa
import datetime

lista_de_tarefas = []

def main():

    print("\n =====  Menu  ===== \n")
    print("1. Adicionar tarefa\n2. Listar tarefas\n3. Marcar tarefa como concluída\n4. Remover tarefa\n\n0.Sair\n\n")
    resp = int(input(">>:"))

    if resp == 1:
        i = 0
        r = int(input("Quantas tarefas?: "))
        while i < r:
            descricao = input("Digite a tarefa: ")
            status = False
            data = datetime.datetime.now()
            lista_de_tarefas.append(Tarefa(descricao,status,data))
            i+=1
        retornar_menu()
        
    elif resp == 2:
        for i in lista_de_tarefas:
            if i.status == True:
               print(f"[x] {i.descricao} - {i.data.strftime("%d/%m/%Y, %X")}")
            else:
                print(f"[ ] {i.descricao} - {i.data.strftime("%d/%m/%Y, %X")}")
               
        retornar_menu()

    elif resp == 3:
        print("\nDeseja concluir qual tarefa?\n")
        j = 0
        for i in lista_de_tarefas:
            print(f"{j}. {i.descricao}")
            j += 1
        r = int(input(">>:"))
        lista_de_tarefas[r].status = True
        lista_de_tarefas[r].data = datetime.datetime.now()
        retornar_menu()

    elif resp == 4:
        print("\nDeseja excluir qual tarefa?\n")
        j = 0
        for i in lista_de_tarefas:
            print(f"{j}. {i.descricao}")
            j += 1
        r = int(input(">>:"))
        lista_de_tarefas.pop(r)
        retornar_menu()

def retornar_menu():
    input("\nEnter para retornar ao menu")
    i = 0
    while i < 10:
        print(">")
        i += 1
    main()

if __name__ == '__main__':
    main()
lista_de_contatos = []

while True:

    print("-"*100)
    match input('''Selecione um elemento abaixo:
            1.Criar contato
            2.Remover contato
            3.Editar contato 
            4.Pesquisar contato
            5.Exibir contato
            6.Sair
            > '''): 
        
            case '1':

                print('-' * 100,
                      '\nO numero deve conter:\n'
                      '-numero do pais\n'
                      '-DDD\n'
                      '-apenas numeros inteiros\n'
                      '-> Exemplo: 5585123451234 <-\n',
                      '-' * 100)

                numero = int(input('Digite o número de contato: '))
                numero = str(numero)
                if len(numero) < 12 or len(numero) > 14:
                    print("numero inválido")

                else:
                    nome = input('Digite o nome do contato salvo: ')
                    contatos = {}
                    contatos['name'] = nome
                    contatos['number'] = numero
                    lista_de_contatos.append(contatos)
                continue

            case '2':

                numero = input('Digite o número a ser retirado: ')

                for contatos in lista_de_contatos:
                    if contatos['number'] == numero:
                            lista_de_contatos.remove(contatos)
                            print(f"lista atualizada:\n{lista_de_contatos}")
                continue

            case '3':
                op = int(input('Editar:\n1.Número\n2.Nome\n3.Ambos\n'))

                if op == 1:
                    numero = input('Digite o número: ') 
                    if len(numero) < 12 or len(numero) > 14:
                                print("numero inválido.")
                    else:
                        for contatos in lista_de_contatos:
                            if numero == contatos['number']:
                                numero = input('Digite o novo' 
                                               'número de contato: ')
                                contatos['number'] = numero
                                print(f"contato atualizado: {contatos}")

                elif op == 2:
                    nome = input('Digite o nome: ')

                    for contatos in lista_de_contatos:
                        if nome == contatos['name']:
                            nome = input('Digite o novo' 
                                         'nome de contato: ')
                            contatos['name'] = nome
                            print(f"contato atualizado: {contatos}")

                elif op == 3:
                    numero = input('Digite o número: ') 

                    for contatos in lista_de_contatos:
                            if numero == contatos['number']:
                                numero = input('Digite o novo' 
                                               'número de contato: ')
                                
                                if len(numero) < 12 or len(numero) > 14:
                                    print("numero inválido.")
                                else:
                                    contatos['number'] = numero

                                    nome = input('Digite o novo' 
                                                 'nome de contato: ')
                                    contatos['name'] = nome
                                    print(f"contato atualizado: {contatos}")
                continue
        
            case '4':
                op = int(input('Procura contato por:\n1.Número\n2.Nome\n'))

                if op == 1:
                    number = input('Digite o número: ') 

                    for contatos in lista_de_contatos:
                         if number in contatos['number']:
                            print("Informações sobre o contato -> " 
                                  f"nome: {contatos['name']} "
                                  f"numero: +{contatos['number']}")

                elif op == 2:
                    nome = input('Digite o nome: ')

                    for contatos in lista_de_contatos:
                        if nome in contatos['name']:
                            print("informações sobre o contato ->" 
                                  f"nome: {contatos['name']} | "
                                  f"numero: +{contatos['number']}")
                else:
                    print("Opção invalida! Tente novamente...")
                continue

            case '5':
                for contato in lista_de_contatos:
                    print(f"\nNome: {contato['name']} | "
                          f"Número: +{contato['number']}")
                continue

            case '6':
                break

            case _:
                print("Caractere inválido!\n")
                continue
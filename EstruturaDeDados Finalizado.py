valores = {
  'Celular': { 'nome': 'Celular', 'id': 1, 'peso': 300, 'valor': 1200, 'fornecedor': 'Ponto Frio'},
  'Tablet': {'nome': 'Tablet','id': 2,'peso': 450, 'valor': 1000, 'fornecedor': 'Americanas'},
  'Computador': {'nome': 'Computador','id': 3,'peso': 1100, 'valor': 1600, 'fornecedor': 'Submarino'},
  'Alexa': {'nome': 'Alexa','id': 4,'peso': 200, 'valor': 220, 'fornecedor': 'Amazon'},
  'Ps5': {'nome': 'Ps5','id': 5,'peso': 900, 'valor': 4000, 'fornecedor': 'Mercado Livre'},
  'Xbox': {'nome': 'Xbox','id': 6,'peso':900, 'valor': 3500, 'fornecedor': 'Casas Bahia'}
}


while True:
    menu = int(input('================= MENU ============================  \n\n(1) Listar todos os produtos \n\n(2) Listar produtos pelo ID \n\n(3) Listar todos os produtos ordenados (A/Z) \n\n(4) Cadastrar novo produto \n\n(5) Editar produto \n\n(6) Excluir produto \n\n(7) Sair do programa \n\n ==================================================\n  '))

    if menu == 1:
        for produto, info in valores.items():
            print(f'Produto: {info["nome"]}, ID: {info["id"]}, Preço: {info["valor"]}R$, Peso: {info["peso"]}g, Fornecedor: {info["fornecedor"]}\n')

    

    elif menu == 2:
        for produto, info in valores.items():
            print(f'ID: {info["id"]}, Produto: {info["nome"]}\n')
        
        id = int(input('Selecione o ID (1-6): \n'))

        if id in [produtos['id'] for produtos in valores.values()]:
            for produtos in valores.values():
             if produtos['id'] == id:
              print(f'Produto: {produtos["nome"]}\n')
              print(f'Peso {produtos["peso"]}g\n')
              print(f'Preço {produtos["valor"]}R$')

            
               

    elif menu == 3:
      print('\n(a) - Bubble Sort')
      print('\n(b) - Insertion Sort')
      print('\n(c) - Selection sort')
    

      menu2 = input('\n Digite uma letra: ')

      if menu2 == 'a': 
      
        print('\n(d) - Crescente')
        print('\n(e) - Decrescent')
        menu3 = input('Digite oque gostaria de Selecionar: ')
      
        if menu3 == 'd':
            print('\n(f) - Id')
            print ('\n(g) - Descricao')
            print ('\n(h) - Peso')
            print('\n(i) - Valor')
            print('\n(j) - fornecedor')

            menu4 = input('\nDigite qual opção voce deseja: ')
            if menu4 == 'f':
              itens = list(valores.values())
              n = len(itens)
              for j in range (n-1):
                  for i in range (0, n -1):
                      if itens[i]['id'] > itens[i+1]['id']:
                        itens[i]['id'],itens[i+1]['id'] = itens[i+1]['id'],itens[i]['id']
              
              for itens in valores.values():
                print(f'ID: {itens["id"]}, Produto: {itens["nome"]}')

            
            elif menu4 == 'g':
                  valores = {
                  'Celular': { 'nome': 'Celular', 'id': 1, 'peso': 300, 'valor': 1200},
                  'Tablet': {'nome': 'Tablet','id': 2,'peso': 450, 'valor': 1000},
                  'Computador': {'nome': 'Computador','id': 3,'peso': 1100, 'valor': 1600},
                  'Alexa': {'nome': 'Alexa','id': 4,'peso': 200, 'valor': 220},
                  'Ps5': {'nome': 'Ps5','id': 5,'peso': 900, 'valor': 4000},
                  'Xbox': {'nome': 'Xbox','id': 6,'peso':900, 'valor': 3500}
                    }
                  items = list(valores.items())
                  n = len(items)

                  for j in range(n - 1):
                    for i in range(0, n - j - 1):
                      if items[i][1]['nome'] > items[i + 1][1]['nome']:
                          items[i], items[i + 1] = items[i + 1], items[i]

                  valores = dict(items)

                  for produto, info in valores.items():
                    print(f'Produto: {info["nome"]}')
                  

            elif menu4 == 'h':
                  itens = list(valores.values())
                  n = len(itens)
                  for j in range (n-1):
                        for i in range (0, n-1):
                            if itens[i]['peso'] > itens[i+1]['peso']:
                             itens[i]['peso'],itens[i+1]['peso'] = itens[i+1]['peso'],itens[i]['peso']
                        
                  for itens in valores.values():
                    print(f'Peso: {itens["peso"]}g, Produto: {itens["nome"]}')
            
            
            elif menu4 == 'i':
                  itens = list(valores.values())
                  n = len(itens)
                  for j in range (n-1):
                        for i in range (0, n -1):
                            if itens[i]['valor'] > itens[i+1]['valor']:
                              itens[i]['valor'],itens[i+1]['valor'] = itens[i+1]['valor'],itens[i]['valor']
                        
                  for itens in valores.values():
                      print(f'Valor: {itens["valor"]}R$, Produto: {itens["nome"]}')


            elif menu4 == 'j':
                valores = {
                  'Celular': { 'nome': 'Celular', 'id': 1, 'peso': 300, 'valor': 1200, 'fornecedor': 'Ponto Frio'},
                  'Tablet': {'nome': 'Tablet','id': 2,'peso': 450, 'valor': 1000, 'fornecedor': 'Americanas'},
                  'Computador': {'nome': 'Computador','id': 3,'peso': 1100, 'valor': 1600, 'fornecedor': 'Submarino'},
                  'Alexa': {'nome': 'Alexa','id': 4,'peso': 200, 'valor': 220, 'fornecedor': 'Amazon'},
                  'Ps5': {'nome': 'Ps5','id': 5,'peso': 900, 'valor': 4000, 'fornecedor': 'Mercado Livre'},
                  'Xbox': {'nome': 'Xbox','id': 6,'peso':900, 'valor': 3500, 'fornecedor': 'Casas Bahia'}
                    }
                items = list(valores.items())
                n = len(items)

                for j in range(n - 1):
                    for i in range(0, n - j - 1):
                      if items[i][1]['fornecedor'] > items[i + 1][1]['fornecedor']:
                          items[i], items[i + 1] = items[i + 1], items[i]

                valores = dict(items)

                for produto, info in valores.items():
                    print(f'Fornecedores: {info["fornecedor"]}')
        
        elif menu3 == 'e':
            print('\n(f) - Id')
            print ('\n(g) - Descricao')
            print ('\n(h) - Peso')
            print('\n(i) - Valor')
            print('\n(j) - fornecedor')

            menu4 = input('\nDigite qual opção voce deseja: ')
            if menu4 == 'f':
              itens = list(valores.values())
              n = len(itens)
              for j in range (n-1):
                  for i in range (0, n -1):
                    if itens[i+1]['id'] > itens[i]['id']:
                        itens[i]['id'],itens[i+1]['id'] = itens[i+1]['id'],itens[i]['id']
                        
              for itens in valores.values():
                print(f'ID: {itens["id"]}, Produto: {itens["nome"]}')
            
            elif menu4 == 'g':
                 valores = {
                  'Celular': { 'nome': 'Celular', 'id': 1, 'peso': 300, 'valor': 1200},
                  'Tablet': {'nome': 'Tablet','id': 2,'peso': 450, 'valor': 1000},
                  'Computador': {'nome': 'Computador','id': 3,'peso': 1100, 'valor': 1600},
                  'Alexa': {'nome': 'Alexa','id': 4,'peso': 200, 'valor': 220},
                  'Ps5': {'nome': 'Ps5','id': 5,'peso': 900, 'valor': 4000},
                  'Xbox': {'nome': 'Xbox','id': 6,'peso':900, 'valor': 3500}
                    }
                 items = list(valores.items())
                 n = len(items)

                 for j in range(n - 1):
                    for i in range(0, n - j - 1):
                      if items[i][1]['nome'] < items[i + 1][1]['nome']:
                          items[i], items[i + 1] = items[i + 1], items[i]

                 valores = dict(items)

                 for produto, info in valores.items():
                    print(f'Produto: {info["nome"]}')
            elif menu == 'h':
                 itens = list(valores.values())
                 n = len(itens)
                 for j in range (n-1):
                        for i in range (0, n-1):
                            if itens[i]['peso'] < itens[i+1]['peso']:
                             itens[i]['peso'],itens[i+1]['peso'] = itens[i+1]['peso'],itens[i]['peso']
                        
                 for itens in valores.values():
                    print(f'Peso: {itens["peso"]}g, Produto: {itens["nome"]}')


            elif menu4 == 'i':
    
                 itens = list(valores.values())
                 n = len(itens)
                 for j in range (n-1):
                        for i in range (0, n -1):
                            if itens[i]['valor'] < itens[i+1]['valor']:
                              itens[i]['valor'],itens[i+1]['valor'] = itens[i+1]['valor'],itens[i]['valor']
                        
                 for itens in valores.values():
                  print(f'Valor: {itens["valor"]}R$, Produto: {itens["nome"]}')


            elif menu4 == 'j':
                 valores = {
                  'Celular': { 'nome': 'Celular', 'id': 1, 'peso': 300, 'valor': 1200, 'fornecedor': 'Ponto Frio'},
                  'Tablet': {'nome': 'Tablet','id': 2,'peso': 450, 'valor': 1000, 'fornecedor': 'Americanas'},
                  'Computador': {'nome': 'Computador','id': 3,'peso': 1100, 'valor': 1600, 'fornecedor': 'Submarino'},
                  'Alexa': {'nome': 'Alexa','id': 4,'peso': 200, 'valor': 220, 'fornecedor': 'Amazon'},
                  'Ps5': {'nome': 'Ps5','id': 5,'peso': 900, 'valor': 4000, 'fornecedor': 'Mercado Livre'},
                  'Xbox': {'nome': 'Xbox','id': 6,'peso':900, 'valor': 3500, 'fornecedor': 'Casas Bahia'}
                    }
                 items = list(valores.items())
                 n = len(items)

                 for j in range(n - 1):
                    for i in range(0, n - j - 1):
                      if items[i][1]['fornecedor'] < items[i + 1][1]['fornecedor']:
                          items[i], items[i + 1] = items[i + 1], items[i]

                 valores = dict(items)

                 for produto, info in valores.items():
                    print(f'Fornecedores: {info["fornecedor"]}')
 
      elif menu2 == 'b':

        print('\n(d) - Crescente')
        print('\n(e) - Decrescent')
        menu3 = input('Digite oque gostaria de Selecionar: ')
      
        if menu3 == 'd':
          print('\n(f) - Id')
          print ('\n(g) - Descricao')
          print ('\n(h) - Peso')
          print('\n(i) - Valor')
          print('\n(j) - fornecedor')

          menu4 = input('\nDigite qual opção voce deseja: ')
          if menu4 == 'f':
             
             itens = list(valores.values())
             n = len(itens)

             for i in range(1, n):
               chave = itens[i]
               j = i - 1
             while j >= 0 and itens[j]['id'] > chave['id']:
               itens[j + 1] = itens[j]
               j = j - 1
             itens[j + 1] = chave

             for item in itens:
              print(f'ID: {item["id"]}, Nome: {item["nome"]},')

          elif menu4 == 'g':
               valores = {
                 'Celular': { 'nome': 'Celular', 'id': 1, 'peso': 300, 'valor': 1200, 'fornecedor': 'Ponto Frio'},
                 'Tablet': {'nome': 'Tablet','id': 2,'peso': 450, 'valor': 1000, 'fornecedor': 'Americanas'},
                 'Computador': {'nome': 'Computador','id': 3,'peso': 1100, 'valor': 1600, 'fornecedor': 'Submarino'},
                 'Alexa': {'nome': 'Alexa','id': 4,'peso': 200, 'valor': 220, 'fornecedor': 'Amazon'},
                 'Ps5': {'nome': 'Ps5','id': 5,'peso': 900, 'valor': 4000, 'fornecedor': 'Mercado Livre'},
                 'Xbox': {'nome': 'Xbox','id': 6,'peso':900, 'valor': 3500, 'fornecedor': 'Casas Bahia'}
                }

               valores_list = list(valores.values())

               for i in range(1, len(valores_list)):
                  key = valores_list[i]
                  j = i - 1
               while j >= 0 and key['nome'] < valores_list[j]['nome']:
                  valores_list[j + 1] = valores_list[j]
                  j -= 1
                  valores_list[j + 1] = key

               sorted_valores = {item['nome']: item for item in valores_list}

               for nome, info in sorted(sorted_valores.items()):
                  print(f'Produto: {nome}')
                
          elif menu4 == 'h':
               
               itens = list(valores.values())
               n = len(itens)

               for i in range(1, n):
                 chave = itens[i]
                 j = i - 1
               while j >= 0 and itens[j]['peso'] > chave['peso']:
                 itens[j + 1] = itens[j]
                 j = j - 1
               itens[j + 1] = chave

               for item in itens:
                print(f'Peso: {item["peso"]}g, Nome: {item["nome"]},')

          elif menu4 == 'i':
               
               itens = list(valores.values())
               n = len(itens)

               for i in range(1, n):
                 chave = itens[i]
                 j = i - 1
               while j >= 0 and itens[j]['valor'] > chave['valor']:
                 itens[j + 1] = itens[j]
                 j = j - 1
               itens[j + 1] = chave

               for item in itens:
                print(f'Valor: {item["valor"]}R$, Nome: {item["nome"]},')

          elif menu4 == 'j':
                valores = {
                 'Celular': { 'nome': 'Celular', 'id': 1, 'peso': 300, 'valor': 1200, 'fornecedor': 'Ponto Frio'},
                 'Tablet': {'nome': 'Tablet','id': 2,'peso': 450, 'valor': 1000, 'fornecedor': 'Americanas'},
                 'Computador': {'nome': 'Computador','id': 3,'peso': 1100, 'valor': 1600, 'fornecedor': 'Submarino'},
                 'Alexa': {'nome': 'Alexa','id': 4,'peso': 200, 'valor': 220, 'fornecedor': 'Amazon'},
                 'Ps5': {'nome': 'Ps5','id': 5,'peso': 900, 'valor': 4000, 'fornecedor': 'Mercado Livre'},
                 'Xbox': {'nome': 'Xbox','id': 6,'peso':900, 'valor': 3500, 'fornecedor': 'Casas Bahia'}
                }

       
                valores_list = list(valores.values())

                for i in range(1, len(valores_list)):
                  key = valores_list[i]
                  j = i - 1
                while j >= 0 and key['fornecedor'] < valores_list[j]['fornecedor']:
                  valores_list[j + 1] = valores_list[j]
                  j -= 1
                  valores_list[j + 1] = key

                sorted_valores = {item['fornecedor']: item for item in valores_list}

                for fornecedor, info in sorted(sorted_valores.items()):
                  print(f'Fornecedor: {fornecedor}')
                

        elif menu3 == 'e':
          print('\n(f) - Id')
          print ('\n(g) - Descricao')
          print ('\n(h) - Peso')
          print('\n(i) - Valor')
          print('\n(j) - fornecedor')

          menu4 = input('\nDigite qual opção voce deseja: ')
          if menu4 == 'f':
             
             itens = list(valores.values())
             n = len(itens)

             for i in range(1, n):
              chave = itens[i]
              
              j = i - 1
              while j >= 0 and itens[j]['id'] < chave['id']:
               itens[j + 1] = itens[j]
               j = j - 1
               itens[j + 1] = chave

             
             for item in itens:
              print(f'ID: {item["id"]}, Nome: {item["nome"]}')

          elif menu4 == 'g':
               valores = {
                 'Celular': { 'nome': 'Celular', 'id': 1, 'peso': 300, 'valor': 1200, 'fornecedor': 'Ponto Frio'},
                 'Tablet': {'nome': 'Tablet','id': 2,'peso': 450, 'valor': 1000, 'fornecedor': 'Americanas'},
                 'Computador': {'nome': 'Computador','id': 3,'peso': 1100, 'valor': 1600, 'fornecedor': 'Submarino'},
                 'Alexa': {'nome': 'Alexa','id': 4,'peso': 200, 'valor': 220, 'fornecedor': 'Amazon'},
                 'Ps5': {'nome': 'Ps5','id': 5,'peso': 900, 'valor': 4000, 'fornecedor': 'Mercado Livre'},
                 'Xbox': {'nome': 'Xbox','id': 6,'peso':900, 'valor': 3500, 'fornecedor': 'Casas Bahia'}
                }

               valores_list = list(valores.values())

               for i in range(1, len(valores_list)):
                  key = valores_list[i]
                  j = i - 1
               while j >= 0 and key['nome'] > valores_list[j]['nome']:
                  valores_list[j + 1] = valores_list[j]
                  j -= 1
                  valores_list[j + 1] = key

               sorted_valores = {item['nome']: item for item in valores_list}

               for nome, info in sorted(sorted_valores.items(), reverse=True):
                  print(f'Produto: {nome}')

          elif menu4 == 'h':
               itens = list(valores.values())
               n = len(itens)

               for i in range(1, n):
                 chave = itens[i]
                 j = i - 1
                 while j >= 0 and itens[j]['peso'] < chave['peso']:
                  itens[j + 1] = itens[j]
                  j = j - 1
                 itens[j + 1] = chave

               for item in itens:
                print(f'Peso: {item["peso"]}g, Nome: {item["nome"]},')
          
          elif menu4 == 'i':
               itens = list(valores.values())
               n = len(itens)

               for i in range(1, n):
                 chave = itens[i]
                 j = i - 1
                 while j >= 0 and itens[j]['valor'] < chave['valor']:
                  itens[j + 1] = itens[j]
                  j = j - 1
                 itens[j + 1] = chave

               for item in itens:
                print(f'Valor: {item["valor"]} R$, Nome: {item["nome"]},')
          
          elif menu4 == 'j':
                valores = {
                 'Celular': { 'nome': 'Celular', 'id': 1, 'peso': 300, 'valor': 1200, 'fornecedor': 'Ponto Frio'},
                 'Tablet': {'nome': 'Tablet','id': 2,'peso': 450, 'valor': 1000, 'fornecedor': 'Americanas'},
                 'Computador': {'nome': 'Computador','id': 3,'peso': 1100, 'valor': 1600, 'fornecedor': 'Submarino'},
                 'Alexa': {'nome': 'Alexa','id': 4,'peso': 200, 'valor': 220, 'fornecedor': 'Amazon'},
                 'Ps5': {'nome': 'Ps5','id': 5,'peso': 900, 'valor': 4000, 'fornecedor': 'Mercado Livre'},
                 'Xbox': {'nome': 'Xbox','id': 6,'peso':900, 'valor': 3500, 'fornecedor': 'Casas Bahia'}
                  }

       
                valores_list = list(valores.values())

                for i in range(1, len(valores_list)):
                  key = valores_list[i]
                  j = i - 1
                while j >= 0 and key['fornecedor'] < valores_list[j]['fornecedor']:
                  valores_list[j + 1] = valores_list[j]
                  j -= 1
                  valores_list[j + 1] = key

                sorted_valores = {item['fornecedor']: item for item in valores_list}

                for fornecedor, info in sorted(sorted_valores.items(), reverse=True):
                  print(f'Fornecedor: {fornecedor}')
            
        
      elif menu2 == 'c':
        print('\n(d) - Crescente')
        print('\n(e) - Decrescent')
        menu3 = input('Digite oque gostaria de Selecionar: ')
      
        if menu3 == 'd':
          print('\n(f) - Id')
          print ('\n(g) - Descricao')
          print ('\n(h) - Peso')
          print('\n(i) - Valor')
          print('\n(j) - fornecedor')

          menu4 = input('\nDigite qual opção voce deseja: ')
          if menu4 == 'f':
             valores_list = list(valores.values())

             for i in range(len(valores_list)):
                min_index = i
                for j in range(i + 1, len(valores_list)):
                   if valores_list[j]['id'] < valores_list[min_index]['id']:
                       min_index = j
                valores_list[i], valores_list[min_index] = valores_list[min_index], valores_list[i]

             sorted_valores = {item['id']: item for item in valores_list}

             for id, info in sorted_valores.items():
              print(f'ID: {id}, Nome: {info["nome"]}')

          elif menu4 == 'g':
             valores_list = list(valores.values())

             for i in range(len(valores_list)):
                min_index = i
                for j in range(i + 1, len(valores_list)):
                   if valores_list[j]['nome'] < valores_list[min_index]['nome']:
                       min_index = j
                valores_list[i], valores_list[min_index] = valores_list[min_index], valores_list[i]

             sorted_valores = {item['nome']: item for item in valores_list}

             for id, info in sorted_valores.items():
              print(f'Nome: {info["nome"]}')

          elif menu4 == 'h':
             valores_list = list(valores.values())

             for i in range(len(valores_list)):
                min_index = i
                for j in range(i + 1, len(valores_list)):
                   if valores_list[j]['peso'] < valores_list[min_index]['peso']:
                       min_index = j
                valores_list[i], valores_list[min_index] = valores_list[min_index], valores_list[i]

             sorted_valores = {item['peso']: item for item in valores_list}

             for peso, info in sorted_valores.items():
              print(f'Peso: {peso}g, Nome: {info["nome"]}')

          elif menu4 == 'i':
             valores_list = list(valores.values())

             for i in range(len(valores_list)):
                min_index = i
                for j in range(i + 1, len(valores_list)):
                   if valores_list[j]['valor'] < valores_list[min_index]['valor']:
                       min_index = j
                valores_list[i], valores_list[min_index] = valores_list[min_index], valores_list[i]

             sorted_valores = {item['valor']: item for item in valores_list}

             for valor, info in sorted_valores.items():
              print(f'Valor: {valor}R$, Nome: {info["nome"]}')

          elif menu4 == 'j':
             valores_list = list(valores.values())

             for i in range(len(valores_list)):
                min_index = i
                for j in range(i + 1, len(valores_list)):
                   if valores_list[j]['fornecedor'] < valores_list[min_index]['fornecedor']:
                       min_index = j
                valores_list[i], valores_list[min_index] = valores_list[min_index], valores_list[i]

             sorted_valores = {item['fornecedor']: item for item in valores_list}

             for id, info in sorted_valores.items():
              print(f'Fornecedor: {info["fornecedor"]}')
        
        elif menu3 == 'e':
          print('\n(f) - Id')
          print ('\n(g) - Descricao')
          print ('\n(h) - Peso')
          print('\n(i) - Valor')
          print('\n(j) - fornecedor')

          menu4 = input('\nDigite qual opção voce deseja: ')
          if menu4 == 'f':
             valores_list = list(valores.values())

             for i in range(len(valores_list)):
                min_index = i
                for j in range(i + 1, len(valores_list)):
                   if valores_list[j]['id'] > valores_list[min_index]['id']:
                       min_index = j
                valores_list[i], valores_list[min_index] = valores_list[min_index], valores_list[i]

             sorted_valores = {item['id']: item for item in valores_list}

             for id, info in sorted_valores.items():
              print(f'ID: {id}, Nome: {info["nome"]}')
          
          elif menu4 == 'g':
             valores_list = list(valores.values())

             for i in range(len(valores_list)):
                min_index = i
                for j in range(i + 1, len(valores_list)):
                   if valores_list[j]['nome'] > valores_list[min_index]['nome']:
                       min_index = j
                valores_list[i], valores_list[min_index] = valores_list[min_index], valores_list[i]

             sorted_valores = {item['nome']: item for item in valores_list}

             for id, info in sorted_valores.items():
              print(f'Nome: {info["nome"]}')
          
          elif menu4 == 'h':
             valores_list = list(valores.values())

             for i in range(len(valores_list)):
                min_index = i
                for j in range(i + 1, len(valores_list)):
                   if valores_list[j]['peso'] > valores_list[min_index]['peso']:
                       min_index = j
                valores_list[i], valores_list[min_index] = valores_list[min_index], valores_list[i]

             sorted_valores = {item['peso']: item for item in valores_list}

             for peso, info in sorted_valores.items():
              print(f'Peso: {peso}g, Nome: {info["nome"]}')
          
          elif menu4 == 'i':
             valores_list = list(valores.values())

             for i in range(len(valores_list)):
                min_index = i
                for j in range(i + 1, len(valores_list)):
                   if valores_list[j]['valor'] > valores_list[min_index]['valor']:
                       min_index = j
                valores_list[i], valores_list[min_index] = valores_list[min_index], valores_list[i]

             sorted_valores = {item['valor']: item for item in valores_list}

             for valor, info in sorted_valores.items():
              print(f'Valor: {valor}R$, Nome: {info["nome"]}')
          
          elif menu4 == 'j':
             valores_list = list(valores.values())

             for i in range(len(valores_list)):
                min_index = i
                for j in range(i + 1, len(valores_list)):
                   if valores_list[j]['fornecedor'] > valores_list[min_index]['fornecedor']:
                       min_index = j
                valores_list[i], valores_list[min_index] = valores_list[min_index], valores_list[i]

             sorted_valores = {item['fornecedor']: item for item in valores_list}

             for id, info in sorted_valores.items():
              print(f'Fornecedor: {info["fornecedor"]}')
    
    
    elif menu == 4:
        print('Digite as seguintes informações')
    
        novoNome = input('Digite o nome do produto novo: ')
        idNova = int(input('Digite uma ID do produto: '))
        pesoProduto = int(input('Digite o Peso do produto (em gramas): '))
        valorNovo = int(input('Digite o valor do produto: '))
        fonecedorNovo = input('Digite o nome do novo fornecedor: ')
          
        novoProduto = {
        'nome': novoNome,
        'id': idNova,
        'peso': pesoProduto,
        'valor': valorNovo,
        'fornecedor': fonecedorNovo
      }

        valores[novoNome] = novoProduto
    

    if menu == 7:
      sair = input('Digite "Sair" para deixar o looping: ')
   
      if sair.lower() =='sair':
        break


    elif menu == 5:
    
      for produto, info in valores.items():
          print(f'Produto: {info["nome"]}, ID: {info["id"]}, Preço: {info["valor"]}R$, Peso: {info["peso"]}g, Fornecedor: {info["fornecedor"]}')
          
      excluir = input('Digite oque voce deseja editar na lista: ')
      if excluir in valores:
            valores.pop(excluir)
      
            nomeEditado = input('Edite o nome: ')
            idEditada =  int(input('Edite a ID: '))
            pesoEditado = int(input('Edite o peso em gramas: '))
            valorEditado = int(input('Edite o valor: '))
            fornecedorEditado = input('Edite o fornecedor')

            produtoEditado = {
            'nome': nomeEditado,
            'id': idEditada,
            'peso': pesoEditado,
            'valor': valorEditado,
            'fornecedor': fornecedorEditado
            }

            valores[nomeEditado] = produtoEditado
            for produto, info in valores.items():
              print(f'Produto: {info["nome"]}, ID: {info["id"]}, Preço: {info["valor"]}R$, Peso: {info["peso"]}g, Fornecedor: {info["fornecedor"]}')

      else: 
       print('Produto não encontrado')


    elif menu == 6:
        
      for produto, info in valores.items():
          print(f'Produto: {info["nome"]}, ID: {info["id"]}, Preço: {info["valor"]}R$, Peso: {info["peso"]}g, Fornecedor: {info["fornecedor"]}')
          
      excluir = input('Digite oque voce deseja editar na lista: ')
      if excluir in valores:
              valores.pop(excluir)
              print ('Produto removido: ',excluir)

      for produto, info in valores.items():
          print(f'Produto: {info["nome"]}, ID: {info["id"]}, Preço: {info["valor"]}R$, Peso: {info["peso"]}g, Fornecedor: {info["fornecedor"]}')

        
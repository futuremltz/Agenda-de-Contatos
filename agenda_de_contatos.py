def adicionar_contato(contatos):
  nome = input("Digite o nome do contato: ")
  telefone = input("Digite o telefone: ")
  email = input("Digite o email: ")
  contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}
  contatos.append(contato)
  return

def ver_contatos(contatos):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "⭐" if contato["favorito"] else " "
    print(f"{indice}.Nome: {contato['nome']} | Telefone: {contato['telefone']} | Email: {contato['email']} | Favorito: {status}")
  return

def editar_contato(contatos,novo_nome,novo_telefone,novo_email,indice_contato):
  novo_indice = int(indice_contato) - 1
  if novo_indice >= 0 and novo_indice < len(contatos):
    contatos[novo_indice]["nome"] = novo_nome
    contatos[novo_indice]["telefone"] = novo_telefone
    contatos[novo_indice]["email"] = novo_email
    print(f"\nO contato {indice_contato} foi atualizado")
  else:
    print("\nIndice de contato invalido")
  return

def favoritar(contatos, indice_contato):
  indice_novo = int(indice_contato) - 1
  if 0 <= indice_novo < len(contatos):
    if contatos[indice_novo]["favorito"] == False:
      contatos[indice_novo]["favorito"] = True
      print(f"\nO contato {indice_contato} foi favoritado")
    else:
      contatos[indice_novo]["favorito"] = False
      print(f"\nO contato {indice_contato} foi desfavoritado")
  else:
    print("\nÍndice inválido")
  return

def ver_favoritos(contatos):
  print("\nLista de contatos favoritos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "⭐" 
    if contato["favorito"] == True:
      print(f"{indice}.Nome: {contato['nome']} | Telefone: {contato['telefone']} | Email: {contato['email']} | Favorito: {status}")
  return

def apagar(contatos):
  escolha = input("\nDigite o número do contato que deseja apagar: ")
  indice_real = int(escolha) - 1

  if indice_real >= 0 and indice_real < len(contatos):
    contato_removido = contatos.pop(indice_real)
    print(f"\nO contato '{contato_removido['nome']}' foi apagado com sucesso")
  else:
    print("\nNúmero de contato inválido.")
  return

contatos = []
while True:
  print("\nAgenda de Contatos")
  print("1.Adicionar contato")
  print("2.Ver contatos")
  print("3.Editar contato")
  print("4.Favoritar contato")
  print("5.Ver contatos favoritos")
  print("6.Apagar contato")
  print("7.Desligar")

  escolha = input("Digite a sua escolha: ")
  
  if escolha == "1":
    adicionar_contato(contatos)
    print("Contato salvo com sucesso")

  elif escolha == "2":
    ver_contatos(contatos)

  elif escolha == "3":
    ver_contatos(contatos)
    indice_contato = input("Digite qual o contato que deseja mudar (use os numeros): ")
    novo_nome = input("Digite novo nome do contato: ")
    novo_telefone = input("Digite o novo numero: ")
    novo_email = input("Digite o novo email: ")
    editar_contato(contatos, novo_nome, novo_telefone, novo_email, indice_contato)

  elif escolha == "4":
    ver_contatos(contatos)
    indice_contato = input("Digite qual o contato que deseja favoritar (use os numeros): ")
    favoritar(contatos, indice_contato)

  elif escolha == "5":
    ver_favoritos(contatos)

  elif escolha == "6":
    ver_contatos(contatos)
    apagar(contatos)

  elif escolha == "7":
    break

  else:
    print("\n Escolha fora de 1 a 7")

print("\nDesligando sistema")


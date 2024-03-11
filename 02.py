def reformulando(frase):
    palavras = frase.split()

    if palavras[0].lower() == "olá":
        nova_frase = "Olá Pessoal"
        return nova_frase
    else:
        return frase

frase = input("Digite uma frase: ")

nova_frase = reformulando(frase)

print("Nova frase:", nova_frase)
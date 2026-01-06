meme_dict = {
            "CRINGE": "Algo vergonhoso ou constrangedor",
            "STALKEAR": "Investigar a vida de alguém online",
            "DELULU": "Pessoa louca",
            "NORMIE": "pessoa desinteressante",
            "X1": "duelo",
            }
for i in range(5):
    word = input("Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas")
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Palavra não encontrada")

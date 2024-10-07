import random
def embaralhar():
    palavra = list(input("Digite sua Palavra:").lower())
    random.shuffle(palavra)
    result = ''.join(palavra)
    print(result)
embaralhar()

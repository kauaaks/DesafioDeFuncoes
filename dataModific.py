def dataporextenso():
    data = input("Digite a data no formato DD/MM/AAAA")
    datamodificada = data.replace("/"," ").split()
    getMes = int(datamodificada[1])
    meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
    if getMes >= 1 and getMes <= 12:
        mes = getMes - 1
        print(f"{datamodificada[0]}/{meses[mes]}/{datamodificada[2]}")
    else:
        print("Mês Inválido.")
dataporextenso()
        

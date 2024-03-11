import traceback

try:
    nome_arquivo = input("Diga o nome do arquivo que você deseja ler").strip()
    arquivo = open(nome_arquivo)
except:
    tracelog = traceback.format_exc()
    print("Erro que aconteceu: ", tracelog)
    open("tracelog.log",'a').write(tracelog)
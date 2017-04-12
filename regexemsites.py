import re
import requests
import sys

#Armazena o valor do parametro numa variavel a ser enviada como requisição

site = str(sys.argv[1])
print('Buscando dados em site: '+ site)

try:
    req = requests.get('http://'+ site)
    #filtra somente os emails do conteudo do site
    padrao = re.findall(r'[\w\.-]+@[\w-]+\.[\w\.-]+', req.text)
    
    #verifica se funcionou se existe um email no corpo da pagina
    if padrao:
        print(padrao)
    else:
        print("Padrao nao encontrado")
except Exception as e:
    print("Detalhes do erro: %s" % e)
    exit()





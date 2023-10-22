import os
import shutil

origem=os.getcwd()
lista=os.listdir(os.getcwd())
remove=['index.py','.gitignore','.gitattributes']
lista=[i for i in lista if i not in remove]

for i in lista:
    print(i)

try:
    for i in lista:
        j=i.split(".")
        origem1=origem+f"\\{i}"
        

                
        if not os.path.exists(j[1]):
            os.makedirs(j[1])
            dd=os.getcwd() 
            destino=dd+f"\\{j[1]}"
        else:
            dd=os.getcwd()
            destino=dd+f"\\{j[1]}"
        shutil.move(origem1,destino)
except:
    print('A sua Pasta Não contem Nenhum arquivo...')

# Apenas uma atualização
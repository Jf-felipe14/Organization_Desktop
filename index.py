import os
import shutil
import sys

origen=os.getcwd()
list=os.listdir(origen)
remove=['.gitignore','index copy.py','index.py']
lis=[i for i in list if i not in remove]
arquivo=[]
for i in lis:
    if os.path.isfile(i):
        arquivo.append(i)
    else:
        continue

class Arquivo:
    def __init__(self,nome,numero):
        self.nome=nome
        self.numero=numero


for j,i in enumerate(arquivo):
    nome,exten1=os.path.splitext(i)
    
    exten=exten1[1:]
    if os.path.exists(exten):
        try:
            shutil.move(f'{origen}/{i}',f'{origen}/{exten}')
        except:
            j+=5
            j=str(j)
            os.rename(i,nome+j+exten1)
            try:
                shutil.move(f'{origen}/{i}',f'{origen}/{exten}')
            except:
                shutil.move(f'{origen}/{i}',f'{origen}/{exten}')
                        
    else:
        os.makedirs(exten)
        shutil.move(f'{origen}/{i}',f'{origen}/{exten}')

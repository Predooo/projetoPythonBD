import os
from re import I

def lerPasta(a):
    arquivo = open(a, 'rt', encoding="utf8")
    a=[]
    for b in arquivo:
        a.append(b)
    arquivo.close()
   
    return a
a = lerPasta('EspéciesArbóreasCampus2.csv')
js = []
i=0
for b in a:
    linha = b.split(':')
    insert = ""
    k=0
    for valor in linha:
        valor = valor.strip()
        if k==0:
            valor = valor.title()
            insert = "bd.arvoresCampus.create({\n  familia: '" + valor+"',"
        if k==1:
            contE = 0
            nomeAutor=""
            nomeEspecie = ""
            for nomeEsp in valor:
                if contE>=2:
                    nomeAutor= nomeAutor+nomeEsp
                if nomeEsp==" ":
                    contE+=1
                if contE<2:
                    nomeEspecie = nomeEspecie+nomeEsp
            insert = insert +  "\n  especie: '" + nomeEspecie+"',"
            insert = insert +  "\n  autor: '" + nomeAutor+"',"
        if k==2:
            valor = valor.title()
            insert = insert +  "\n  nomePopular: '" + valor+"',"
        if k==3:
            valor = valor.title()
            insert = insert +  "\n  tipoCaule: '" + valor+"',"
        if k==4:
            valor = valor.title()
            insert = insert +  "\n  tipoFolha: '" + valor+"',"
        if k==5:
            valor = valor.title()
            insert = insert +  "\n  filotaxia: '" + valor+"',"
        if k==6:
            valor = valor.title()
            insert = insert +  "\n  forma: '" + valor+"',"
        if k==7:
            valor = valor.title()
            insert = insert +  "\n  margem: '" + valor+"',"
        if k==8:
            valor = valor.title()
            insert = insert +  "\n  apice: '" + valor+"',"
        if k==9:
            valor = valor.title()
            insert = insert +  "\n  base: '" + valor+"',"
        if k==10:
            valor = valor.title()
            insert = insert +  "\n  nervacao: '" + valor+"',"
        if k==11:
            valor = valor.title()
            insert = insert +  "\n  consistencia: '" + valor+"',"
        if k==12:
            valor = valor.title()
            insert = insert +  "\n  pilosidade: '" + valor+"',"
        if k==13:
            valor = valor.title()
            insert = insert +  "\n  caracteresEspeciaisFolha: '" + valor+"',"
        if k==14:
            valor = valor.title()
            insert = insert +  "\n  aparenciaRitidoma: '" + valor+"',"
        if k==15:
            valor = valor.title()
            insert = insert +  "\n  deiscenciaRitidoma: '" + valor+"',"
        if k==16:
            valor = valor.title()
            insert = insert +  "\n  texturainterna: '" + valor+"',"
        if k==17:
            valor = valor.title()
            insert = insert +  "\n  corCascaInterna: '" + valor+"',"
        if k==18:
            valor = valor.title()
            insert = insert +  "\n  caracteresEspeciaisCaule: '" + valor+"'\n})"
        k+=1
    i+=1
    js = js + [insert]
i=1
while i<(len(js)):
    print(js[i])
    i+=1
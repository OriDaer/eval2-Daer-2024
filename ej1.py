import requests,os,json
url= 'https://jsonplaceholder.typicode.com/posts'
data=requests.get(url)
cant_posts=int(input('ingrese la cantidad de post que desea obtener '))
print(cant_posts)
num=0
def Aux(cant_posts):
    if(cant_posts%2==1 and cant_posts>1):
        cant_posts_primo=cant_posts
        num+=1
    if(cant_posts%2==0 and cant_posts>1):
        cant_posts_par=cant_posts
        num+=1

#cant_posts_primo y par no agarran xq no son globales,entonces cm hacer????
def Api(Aux,cant_posts_primo,cant_posts_par):
    if data.status_code==200:
        data_json=data.json()
        if (cant_posts > 0 and cant_posts >= 100):
            direct=os.makedirs('../ej1.py/Dowloads')
            for i in range(cant_posts):
                if(cant_posts_primo==True):#es primo
                    archiv=open(f'dl{num}NotPrimes.json','w')
                    json.dumps(data_json,archiv)
                if(cant_posts_par==True):#es par
                    archiv=open(f'dl{num}Primes.json','w')
                    json.dumps(data_json,archiv)
        else:
            print('lo que ingresaste no es valido,intenta nuevamente')
    else:
        print(f'url no valida,intente con otra{data.status_code}') 

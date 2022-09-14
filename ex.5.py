def crearea_listei():
    n=int(input('nr. de elemente'))
    lista_locala=[]
    for i in range(n):
        element=input(f'elementul {i} e ')
        if type(element)== 'int':
            lista_locala.append(element)
     return lista_locala
print(crearea_listei())
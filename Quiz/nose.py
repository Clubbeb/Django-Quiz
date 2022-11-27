import sqlite3

feliz = 1
triste = 1
enojado = 1
indiferente = 1


x = []
con = sqlite3.connect("C:/Users/clubb/OneDrive/Documentos/GitHub/Django-Quiz/db.sqlite3")
cur = con.cursor()
for row in cur.execute('SELECT * FROM Quiz_quizusuario'):
    x.append(row[1])
        
con.close()

for valor in x:
    if valor == 10:
        feliz += 1 
    elif valor == 5:
        triste += 1
    elif valor == 3:
        enojado += 1
    elif valor == 0:
        indiferente += 1
    elif valor == 15:
        feliz += 1
        triste += 1
    elif valor == 8:
        triste += 1
        enojado += 1
    elif valor == 13:
        feliz += 1
        enojado += 1
    elif valor == 18:
        feliz +=1
        triste +=1
        enojado +=1

print(feliz,triste,enojado,indiferente)


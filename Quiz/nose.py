import sqlite3
x = []

con = sqlite3.connect("C:/Users/clubb/OneDrive/Documentos/GitHub/Django-Quiz/db.sqlite3")
cur = con.cursor()
    
for row in cur.execute('SELECT * FROM Quiz_quizusuario'):
    print(row)
    x.append(row[1])
        
con.close()

print(x)

for valor in x:
    if valor <=10 and valor >= 8:
        print(valor)


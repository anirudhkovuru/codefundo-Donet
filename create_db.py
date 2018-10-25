import sqlite3 as sql
import string
import random

letters = list(string.ascii_lowercase)
letters.extend([i+b for i in letters for b in letters])

donors = ['Imelda','Roxy','Nidia','Bennett','Roxanne','Kirstin','Markus','Jona','Kylie','Austin','Tiana','Demetra',
          'Edris','Jacquetta','Ilana','Eugene','Brunilda','Andreas','Milton','Thora', 'Anirudh']

conn = sql.connect('refugee.db')
print("Opened database successfully")

conn.execute('CREATE TABLE refugees (name TEXT, age INT, gender TEXT, '
             'disability TEXT, Familial_status TEXT, dependencies INT, '
             'orphan_status TEXT, balance INT, donor TEXT)')

c = conn.cursor()

for i in letters:
    name = i
    age = str(random.randint(5, 101))
    gender = random.choice(['Male', 'Female'])
    disability = random.choice(['Yes', 'No'])
    familial_status = random.choice(['Married', 'Unmarried'])
    dependencies = str(random.randint(0, 9))
    orphan_status = random.choice(['Yes', 'No'])
    balance = str(random.randint(0, 1001))
    donor = random.choice(donors)
    c.execute('INSERT INTO refugees '
              'VALUES ("'+name+'","'+age+'","'+gender+'","'+disability+'","'+familial_status+'","'+dependencies+'","'+orphan_status+'","'+balance+'","'+donor+'")')
conn.commit()

print("Table created successfully")
c.execute("select * from refugees")
rows = c.fetchall()
print(rows)
conn.close()

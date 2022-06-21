import sqlite3

# connect to the database

conn = sqlite3.connect(r'file:\\corp-rmm-01\c$\ProgramData\Admin Arsenal\PDQ Inventory\Database.db?mode=ro', uri=True)
cur = conn.cursor()

# Find the computers a user is logged into
cur.execute(r"SELECT Name FROM Computers WHERE CurrentUser LIKE '%stogsdill%'")

computerList = cur.fetchall()

if computerList == []:
    print("No computers found")
try:
    for computer in computerList:
        print(computer)
except Exception as e:
    print("Error")
    print(e)

# close the connection
conn.close()
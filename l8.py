import sqlite3
con = sqlite3.connect("time.db")

cur = con.cursor()

listOfTables = cur.execute(
  """SELECT name FROM sqlite_master WHERE type='table'
  AND name='test'; """).fetchall()
 
if listOfTables == []:
    print('Table not found!')
    cur.execute("CREATE TABLE test(id, first_name,last_name)")
else:
    print('Table found!')
    cur.execute("""
    INSERT INTO test VALUES
        (4,'dave','smol'),
        (5,'mike','tyson')
""")


con.commit()


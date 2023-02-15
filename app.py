from flask import Flask, redirect, request
import sqlite3
from flask_cors import CORS


con = sqlite3.connect("time.db", check_same_thread=False)
cur = con.cursor()
db = cur.execute("SELECT * FROM test").fetchall()


app = Flask(__name__)
CORS(app)

@app.route("/add",methods=['POST'])
def posting():
    id =request.form['id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    cur.execute(f"INSERT INTO test VALUES ('{id}', '{first_name}', '{last_name}')")
    print(f"{id},{first_name},{last_name}")
    con.commit()
    print(cur.execute("SELECT * FROM test").fetchall())
    return redirect("http://localhost:5500", code=302)

@app.route("/delete",methods=['DELETE'])
def delete():
    id =request.form['id']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    cur.execute(f"DELETE FROM test WHERE id={id};")
    print(f"{id},{first_name},{last_name}")
    con.commit()
    print(cur.execute("SELECT * FROM test").fetchall())
    return redirect("http://localhost:5500", code=302)
@app.route("/")
def hello_world():
    return db

if __name__ == '__main__':
    app.debug = True
    app.run()
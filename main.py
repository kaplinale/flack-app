 #!/usr/bin/env python
 # -*- coding: utf-8 -*-
from flask import Flask
import psycopg2
app = Flask(__name__)
 

@app.route('/test1')
def test1():
    return 'test1 route revision2'

@app.route('/test2')
def test2():
    return('test2 route revision2')

@app.route('/testdb')
def testdb():
    conn = psycopg2.connect(dbname="flackapp", user="flackapp", password="flackapp", host="local-db", port=5432)
    conn.autocommit = True  # устанавливаем актокоммит
    sql1="select version()"
    cursor = conn.cursor()
    cursor.execute(sql1)    # непосредственное выполнение команды sql1
    txt = cursor.fetchone()
    cursor.close()
    conn.close()
    return ''.join(txt)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0', port=5000)
import psycopg2
import yaml
import os

def connectToServer():
    config = {}
    yml_pth = os.path.join(os.path.dirname(__file__), '../config/server.yml')
    with open(yml_pth, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return psycopg2.connect(dbname=config['database'], user=config['user'], password=config['password'], host=config['host'], port=config['port'])
    
def exec_get_one(sql, args={}):
    conn = connectToServer()
    cur = conn.cursor()
    cur.execute(sql, args)
    one = cur.fetchone()
    conn.close()
    return one

def exec_get_all(sql, args={}):
    conn = connectToServer()
    cur = conn.cursor()
    cur.execute(sql, args)
    all = cur.fetchall()
    conn.close()
    return all

def exec_sql_file(path):
    full = os.path.join(os.path.dirname(__file__), f'../../{path}')
    conn = connectToServer()
    cur = conn.cursor()
    with open(full, 'r') as file:
        cur.execute(file.read())
    conn.commit()
    conn.close()
    
def exec_commit(sql, args={}):
    conn = connectToServer()
    cur = conn.cursor()
    result = cur.execute(sql, args)
    conn.commit()
    conn.close()
    return result
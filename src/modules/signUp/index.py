from src.modules.database import getConnection
from src.modules.signUp.controller import signUp

def mainSignUp(name, username, password):
    try:
        conn = getConnection()
        cur = conn.cursor()
        signUp(cur, name, username, password)
        conn. commit()
        cur.close()
    except Exception as e :
        print(e)
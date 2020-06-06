from src.modules.database import getConnection
from src.modules.signIn.controller import signIn, createSession

def mainSignIn(username, password): 
    try:
        conn = getConnection()
        cur = conn.cursor()
        res = signIn(cur, username, password)
        if(res != None):
            createSession(cur, res[0])
        conn. commit()
        cur.close()
        return res
    except Exception as e:
        print(e)
        return None
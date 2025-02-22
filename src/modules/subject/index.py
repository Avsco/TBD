from src.modules.database import getConnection
from src.modules.subject.controller import GET, SHOW

def getSubjects(): 
    try:
        conn = getConnection()
        cur = conn.cursor()
        res = GET(cur)
        conn. commit()
        cur.close()
        return res
    except Exception as e:
        print(e)
        return None

def getSubjectsById(id):
    try:
        conn = getConnection()
        cur = conn.cursor()
        res = SHOW(cur, id)
        conn. commit()
        cur.close()
        return res
    except Exception as e:
        print(e)
        return None
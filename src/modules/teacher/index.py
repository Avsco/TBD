from src.modules.database import getConnection
from src.modules.teacher.controller import GET, SHOW

def getTeachers(): 
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

def getTeacherById(id):
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
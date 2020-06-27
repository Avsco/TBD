from src.modules.database import getConnection
from src.modules.postulation.controller import POST, GET

def insertPostulation(id_subject, id_postulant):
    try:
        conn = getConnection()
        cur = conn.cursor()
        msg = POST(cur, id_subject, id_postulant)
        conn. commit()
        cur.close()
        return msg
    except Exception as e:
        print(e)

def getPostulation(id_student):
    try:
        conn = getConnection()
        cur = conn.cursor()
        postulations = GET(cur, id_student)
        conn. commit()
        cur.close()
        return postulations
    except Exception as e:
        print(e)

print(getPostulation(2))
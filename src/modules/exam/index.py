from src.modules.database import getConnection
from src.modules.exam.controller import POST

def insertExam(id_subject, id_teacher, image):
    try:
        conn = getConnection()
        cur = conn.cursor()
        msg = POST(cur, id_subject, id_teacher, image)
        conn. commit()
        cur.close()
        return msg
    except Exception as e:
        print(e)
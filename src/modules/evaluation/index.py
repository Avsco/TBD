from src.modules.database import getConnection
from src.modules.evaluation.controller import SHOW, GETSubjectsByTeacher, GETStundentByTeacherAndSubject, PUTAssistence

def getEvaluations(id_subject, id_postulant):
    try:
        conn = getConnection()
        cur = conn.cursor()
        response = SHOW(cur, id_subject, id_postulant)
        conn. commit()
        cur.close()
        return response
    except Exception as e:
        print(e)

def getSubjects(id_teacher):
    try:
        conn = getConnection()
        cur = conn.cursor()
        response = GETSubjectsByTeacher(cur, id_teacher)
        conn. commit()
        cur.close()
        return response
    except Exception as e:
        print(e)

def getStudents(id_subject, id_teacher):
    try:
        conn = getConnection()
        cur = conn.cursor()
        response = GETStundentByTeacherAndSubject(cur, id_subject, id_teacher)
        conn. commit()
        cur.close()
        return response
    except Exception as e:
        print(e)

# controlar gestion
def isOnEvaluation(id_subject, id_postulant):
    try:
        conn = getConnection()
        cur = conn.cursor()
        PUTAssistence(cur, id_subject, id_postulant)
        conn. commit()
        cur.close()
    except Exception as e:
        print(e)
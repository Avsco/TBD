def SHOW(cur, id_subject, id_postulant):
    try:
        SQL = """SELECT application_management, note_evaluation FROM evaluation
                WHERE  id_subject = %s AND id_postulant = %s"""
        cur.execute(SQL, (id_subject, id_postulant))
        return cur.fetchall()
    except Exception as e:
        print(e)
        return "Error en el registro"

def GETSubjectsByTeacher(cur, id_teacher):
    try:
        SQL = """SELECT sub.id_subject, sub.subject_name FROM( 
                    SELECT DISTINCT id_subject FROM evaluation
                    WHERE  id_teacher = %s) AS uno, subject AS sub
                WHERE uno.id_subject = sub.id_subject"""
        cur.execute(SQL, [id_teacher])
        return cur.fetchall()
    except Exception as e:
        print(e)
        return "Error en el registro"

#aumetar control de gestion
def GETStundentByTeacherAndSubject(cur, id_subject, id_teacher):
    try:
        SQL = """SELECT u.name_user FROM(
                    SELECT id_postulant FROM evaluation
                    WHERE id_teacher=%s AND id_subject=%s) AS uno, "USER" AS u
                WHERE uno.id_postulant = u.id_user"""
        cur.execute(SQL, [id_teacher, id_subject])
        return cur.fetchall()
    except Exception as e:
        print(e)
        return "Error en el registro"

def PUTAssistence(cur, id_subject, id_postulant):
    try:
        SQL = """UPDATE evaluation
                SET assistance_evaluation = true
                WHERE id_subject = %s AND id_postulant = %s"""
        cur.execute(SQL, [id_subject, id_postulant])
    except Exception as e:
        print(e)
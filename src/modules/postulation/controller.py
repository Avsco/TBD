from datetime import date

def POST(cur, id_subject, id_postulant):
    try:
        SQL = """INSERT INTO postulation(id_subject, id_postulant, application_management)
                  VALUES(%s, %s, %s);"""
        cur.execute(SQL, (id_subject, id_postulant, date.today()))
        return 'Tranquilo'
    except Exception as e:
        print(e)
        return "Error en el registro"

def GET(cur, id_student):
    try:
        SQL = """SELECT * FROM postulation WHERE id_postulant=%s;"""
        cur.execute(SQL, [id_student])
        return cur.fetchall()
    except Exception as e:
        print(e)
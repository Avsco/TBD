from datetime import date

def POST(cur, id_subject, id_teacher, image):
    try:
        SQL = """INSERT INTO exam(id_subject, management_exam, id_teacher)
                  VALUES(%s, %s, %s);"""
        cur.execute(SQL, (id_subject, date.today(), id_teacher))
        return 'Tranquilo'
    except Exception as e:
        print(e)
        return "Error en el registro"

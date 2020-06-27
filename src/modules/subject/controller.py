def GET(cur):
    try:
        SQL = """SELECT id_subject, subject_name FROM subject"""
        cur.execute(SQL)
        return cur.fetchall()
    except Exception as e:
        print(e)
        return None

def SHOW(cur, id_subject):
    try:
        SQL = """SELECT subject_name FROM subject WHERE id_subject=%s"""
        cur.execute(SQL, [id_subject])
        return cur.fetchone()[0]
    except Exception as e:
        print(e)
def GET(cur):
    try:
        SQL = """SELECT id_subject, subject_name FROM subject"""
        cur.execute(SQL)
        return cur.fetchall()
    except Exception as e:
        print(e)
        return None
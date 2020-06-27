def GET(cur):
    try:
        SQL = """SELECT "USER".id_user, "USER".name_user FROM(
                    SELECT id_user FROM user_rol
                    WHERE id_rol = 2) AS uno, "USER"
                WHERE uno.id_user = "USER".id_user;"""
        cur.execute(SQL)
        return cur.fetchall()
    except Exception as e:
        print(e)
        return None

def SHOW(cur, id_subject):
    try:
        SQL = """SELECT user_name FROM "USER" WHERE id_user = %s"""
        cur.execute(SQL, [id_subject])
        return cur.fetchone()[0]
    except Exception as e:
        print(e)
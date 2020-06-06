def signIn(cur, username, password):
    try:
        SQL = """SELECT id_user, name_user FROM "USER" WHERE  username_user=%s AND password_user=%s;"""
        cur.execute(SQL, (username, password))
        return cur.fetchone()
    except Exception as e:
        print(e)
        return None

def createSession(cur, id_user):
    try:
        SQL = """INSERT INTO SESSION(id_user, pid_session, start_session) VALUES (%s, %s, %s);"""
        cur.execute( SQL, (id_user, getPID(cur), getTimeStamp(cur)))
    except Exception as e:
        print(e)
        return None
 
def getPID(cur):
    try:
        cur.execute("SELECT pg_backend_pid();")
        return cur.fetchone()[0]
    except Exception as e:
        print(e)
        return None

def getTimeStamp(cur):
    try:
        cur.execute("SELECT current_timestamp;")
        return cur.fetchone()[0]
    except Exception as e:
        print(e)
        return None

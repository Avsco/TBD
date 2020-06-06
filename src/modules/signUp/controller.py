def signUp(cur, name, username, password):
    try:
        SQL = """INSERT INTO "USER"(name_user, username_user, password_user) VALUES(%s, %s, %s);"""
        cur.execute(SQL, (name, username, password))
    except Exception as e:
        print(e)
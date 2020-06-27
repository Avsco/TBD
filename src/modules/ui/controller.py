def GETUIByID(cur, id_user):
    try:
            SQL = """SELECT name_ui FROM(SELECT function_ui.id_ui
                        FROM (SELECT rol_function.id_function
                              FROM (SELECT user_rol.id_rol
                                    FROM (SELECT id_user 
                                          FROM "USER" 
                                          WHERE id_user = %s) as uno, user_rol
                                    WHERE uno.id_user = user_rol.id_user) as dos, rol_function
                              WHERE dos.id_rol = rol_function.id_rol) as tres, function_ui
                        WHERE tres.id_function = function_ui.id_function) AS cuatro, ui
                     WHERE cuatro.id_ui = ui.id_ui"""
            cur.execute(SQL, (id_user,))
            return cur.fetchall()
    except Exception as e:
        print(e)
        return tuple()

def SHOWUI(cur, id_ui):
      try:
            SQL = """SELECT name_ui
                     FROM ui
                     WHERE id_ui = %s"""
            cur.execute(SQL, (id_ui,))
            return cur.fetchall()
      except Exception as e:
            print(e)
            return tuple()
from src.modules.database import getConnection
from src.modules.ui.controller import GETUIByID, SHOWUI

def getUIByID_user(id_user):
    try:
        conn = getConnection()
        cur = conn.cursor()
        res = GETUIByID(cur, id_user)
        conn. commit()
        cur.close()
        return res
    except Exception as e :
        print(e)
        return tuple()

def showUi(id_ui):
    try:
        conn = getConnection()
        cur = conn.cursor()
        res = SHOWUI(cur, id_ui)
        conn. commit()
        cur.close()
        return res
    except Exception as e :
        print(e)
        return tuple()
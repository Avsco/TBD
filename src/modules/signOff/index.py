from src.modules.database import getConnection
from src.modules.signOff.controller import updateClosingTime

def signOff():
    try:
        conn = getConnection()
        cur = conn.cursor()
        updateClosingTime(cur)
        conn. commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(e)
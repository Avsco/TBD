from src.modules.signIn.controller import getTimeStamp, getPID

def updateClosingTime(cur):
    try:
        SQL = """UPDATE session 
             SET end_session = %s 
             WHERE end_session IS NULL AND pid_session = %s;"""
        cur.execute(SQL, (getTimeStamp(cur), getPID(cur)))
    except Exception as e:
        print(e)
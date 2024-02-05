import mysql.connector as psc


def Connect(pwd):
    global cur, con
    con = psc.connect(host='localhost', user='root', passwd=pwd)
    cur = con.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS cloudcast")
    cur.execute("use cloudcast")


def update(week, day, stat, val):
    if stat == 'P':
        cur.execute(f"UPDATE 30_day_forecasted_weather SET Pressure={val} WHERE Date={(week-1)*7 + day}")
    elif stat == 'H':
        cur.execute(f"UPDATE 30_day_forecasted_weather SET Humidity={val} WHERE Date={(week-1)*7 + day}")
    elif stat == 'T':
        cur.execute(f"UPDATE 30_day_forecasted_weather SET Temperature={val} WHERE Date={(week-1)*7 + day}")
    con.commit()


def display(week=0):
    from prettytable import PrettyTable
    x = PrettyTable()
    x.field_names = ["Date", "Temperature (°C)", "Pressure (hPa)", "Humidity (rel. %)"]
    
    if week==0:
        cur.execute("SELECT * FROM 30_day_forecasted_weather")
        print('\nPredicted Data')
        predic=cur.fetchall()
        x.clear_rows()
        x.add_rows(predic)
        print(x)
        print()
        cur.execute("SELECT * FROM 30_day_recorded_weather")
        print('\nObserved Data')
        act=cur.fetchall()
        x.clear_rows()
        x.add_rows(act)
        print(x)
        print()
    elif week==5:
        cur.execute("SELECT * FROM 30_day_forecasted_weather WHERE Date IN (29,30)")
        print('\nPredicted Data')
        predic=cur.fetchall()
        x.clear_rows()
        x.add_rows(predic)
        print(x)
        print()
        cur.execute("SELECT * FROM 30_day_recorded_weather WHERE Date IN (29,30)")
        print('\nObserved Data')
        act=cur.fetchall()
        x.clear_rows()
        x.add_rows(act)
        print(x)
        print()
    else:
        cur.execute(f"SELECT * FROM 30_day_forecasted_weather WHERE Date BETWEEN {(week-1)*7+1} AND {(week-1)*7+7}")
        print('\nPredicted Data')
        predic=cur.fetchall()
        x.clear_rows()
        x.add_rows(predic)
        print(x)
        print()
        cur.execute(f"SELECT * FROM 30_day_recorded_weather WHERE Date BETWEEN {(week-1)*7+1} AND {(week-1)*7+7}")
        print('\nObserved Data')
        act=cur.fetchall()
        x.clear_rows()
        x.add_rows(act)
        print(x)
        print()


def get_val(week, day, stat):
    if stat=='T':
        x='Temperature'
    elif stat=='P':
        x='Pressure'
    elif stat=='H':
        x='Humidity'
    cur.execute(f"SELECT {x} FROM 30_day_forecasted_weather WHERE Date = {(week-1)*7 + day}")
    valp=cur.fetchall()
    cur.execute(f"SELECT {x} FROM 30_day_recorded_weather WHERE Date = {(week-1)*7 + day}")
    valr=cur.fetchall()
    return valp[0][0], valr[0][0]


#cleanup
def exit(maxdiff=0, scoreslate=0, offset=0, moves=0, save=False):
    if not save:
        cur.execute("DROP TABLE IF EXISTS 30_day_forecasted_weather")
        cur.execute("DROP TABLE IF EXISTS 30_day_recorded_weather")
    else:
        with open('score.txt','w') as ob:
            ob.write("%s\n%s\n%s\n%s"%(moves, offset, scoreslate, maxdiff))
    con.close()


def load():
    try:
        with open('score.txt','r') as ob:
            moves, offset, scoreslate, maxdiff = map(int, ob.readlines())
        return maxdiff, scoreslate, offset, moves
    except OSError as e:
        return(-1)


def get_tables():
    cur.execute("SELECT * FROM 30_day_forecasted_weather")
    predicted = cur.fetchall()

    cur.execute("SELECT * FROM 30_day_recorded_weather")
    actual = cur.fetchall()

    return predicted, actual

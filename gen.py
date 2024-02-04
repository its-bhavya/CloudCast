from random import randint
import mysql.connector as psc
import requests


def generator(pwd):
    con = psc.connect(host='localhost', user='root', passwd=pwd, database='cloudcast')
    cur = con.cursor()
    
    cur.execute("DROP TABLE IF EXISTS 30_day_forecasted_weather")
    cur.execute("DROP TABLE IF EXISTS 30_day_recorded_weather")
    con.commit()

    cur.execute("CREATE TABLE 30_day_forecasted_weather(Date int, Temperature int, Pressure int, Humidity int)")
    cur.execute("CREATE TABLE 30_day_recorded_weather(Date int, Temperature int, Pressure int, Humidity int)")
    con.commit()


    #predicted dataset:
    #30_day_forecasted_weather

    for date in range(1, 31):
        cur.execute(f"INSERT INTO 30_day_forecasted_weather VALUES({date}, {randint(-20, 10)}, {randint(595, 680)}, {randint(20, 55)})")
        con.commit()
    
    #recorded dataset:
    #30_day_recorded_weather

    rseed = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=27.649319&lon=88.40538985091041&appid=b37ff37feb0a2483e3dad14d943672e1&units=metric")
    
    if(rseed.status_code==200):
       rseed = rseed.json()['main']
    else:
        return 404
    rseed['pressure'] = rseed['grnd_level']

    sdate = randint(1, 30)

    seed = rseed.copy()
    date = 1
    while(date < sdate):
        const = randint(1, 2)
        offset = (1, 2, 3, 4, 5, -1, -2, -3, -4, -5)[randint(0,9)]
        seed['pressure'] += offset
        offset = (1, 2, 3, 4, 5, -1, -2, -3, -4, -5)[randint(0,9)]
        seed['temp'] += offset
        offset = (1, 2, 3, 4, 5, -1, -2, -3, -4, -5)[randint(0,9)]
        seed['humidity'] += offset
        lim = date+const
        while(date < lim and date < sdate):
            cur.execute(f"INSERT INTO 30_day_recorded_weather VALUES({date}, {seed['temp']}, {seed['pressure']}, {seed['humidity']})")
            con.commit()
            date += 1

    cur.execute(f"INSERT INTO 30_day_recorded_weather VALUES({sdate}, {rseed['temp']}, {rseed['pressure']}, {rseed['humidity']})")
    con.commit()

    seed = rseed.copy()
    date = sdate+1
    while(date < 31):
        const = randint(1, 2)
        offset = (1, 2, 3, 4, 5, -1, -2, -3, -4, -5)[randint(0,9)]
        seed['pressure'] += offset
        offset = (1, 2, 3, 4, 5, -1, -2, -3, -4, -5)[randint(0,9)]
        seed['temp'] += offset
        offset = (1, 2, 3, 4, 5, -1, -2, -3, -4, -5)[randint(0,9)]
        seed['humidity'] += offset
        lim = date+const
        while(date < lim and date < 31):
            cur.execute(f"INSERT INTO 30_day_recorded_weather VALUES({date}, {seed['temp']}, {seed['pressure']}, {seed['humidity']})")
            con.commit()
            date += 1
    
    con.close()


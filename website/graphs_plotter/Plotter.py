import sqlite3
from sqlite3 import Error

import matplotlib.pyplot as plt

# DATABASEPATH = r"D:/WeatherStation/sensorData.db"
from STATICVALUES import DATABASEPATH


def create_connection(db_file):
    """ Create a connection to the sqlite database
    :param db_file: database file
    :return: Connection or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def select_all_sensor_history(conn, sensor_id):
    """
    This function selects every property from the SensorHistory table
    :param conn: connection to the database
    """
    cur = conn.cursor()
    sql_statement = '''SELECT Date, Time, Value FROM SensorHistory WHERE SensorId = ?'''
    cur.execute(sql_statement, "{0}".format(sensor_id))

    rows = cur.fetchall()
    return rows
    # for row in rows:
    #     print(row)


def select_destinct_dates(conn, sensor_id):
    cur = conn.cursor()
    sql_statement = '''SELECT DISTINCT DATE from SensorHistory WHERE SensorId = ?'''
    cur.execute(sql_statement, "{0}".format(sensor_id))

    rows = cur.fetchall()
    dates = []
    for row in rows:
        dates.append(row[0])
    return dates


def select_average_values(conn, sensor_id, date):
    cur = conn.cursor()
    sql_statement = '''SELECT AVG(Value) AS average FROM SensorHistory WHERE Date = ? and SensorId = ?'''
    cur.execute(sql_statement, ("{0}".format(date), "{0}".format(sensor_id)))
    rows = cur.fetchall()
    return round(rows[0][0], 1)


def plotHumidity(conn):
    dates = select_destinct_dates(conn, 0)
    averages = []
    for date in dates:
        averages.append(select_average_values(conn, 0, date))

    print("Plotting humidity")
    # x axis values
    x = dates
    # corresponding y axis values
    y = averages
    plt.xticks(rotation=90)
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('Date')
    # naming the y axis
    plt.ylabel('Humidity')

    # giving a title to my graph
    plt.title('Room humidity')
    plt.savefig("static/humidity.png")
    # function to show the plot
    # plt.show()


def plotTemperatureFromHumidity(conn):
    dates = select_destinct_dates(conn, 1)
    averages = []
    for date in dates:
        averages.append(select_average_values(conn, 1, date))

    print("Plotting Temperature from humidity")
    # x axis values
    x = dates
    # corresponding y axis values
    y = averages
    plt.xticks(rotation=90)
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('Date')
    # naming the y axis
    plt.ylabel('Temperature')

    # giving a title to my graph
    plt.title('Room temperature from humidity')

    plt.savefig("static/temperatureFromHumidity.png")

    # function to show the plot
    # plt.show()


def plotTemperatureFromPressure(conn):
    dates = select_destinct_dates(conn, 2)
    averages = []
    for date in dates:
        averages.append(select_average_values(conn, 2, date))

    print("Plotting Temperature from pressure")
    # x axis values
    x = dates
    # corresponding y axis values
    y = averages
    plt.xticks(rotation=90)
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('Date')
    # naming the y axis
    plt.ylabel('Temperature')

    # giving a title to my graph
    plt.title('Room temperature from pressure')

    plt.savefig("static/temperatureFromPressure.png")

    # function to show the plot
    # plt.show()


def plotBarometricPressure(conn):
    dates = select_destinct_dates(conn, 3)
    averages = []
    for date in dates:
        averages.append(select_average_values(conn, 3, date))

    print("Plotting Temperature from humidity")
    # x axis values
    x = dates
    # corresponding y axis values
    y = averages
    plt.xticks(rotation=90)
    # plotting the points
    plt.plot(x, y)

    # naming the x axis
    plt.xlabel('Date')
    # naming the y axis
    plt.ylabel('Pressure')

    # giving a title to my graph
    plt.title('Room pressure')

    plt.savefig("static/pressure.png")

    # function to show the plot
    # plt.show()


def main():
    """
    This file is used to test database connections in python
    """
    # Create a database connection
    conn = create_connection(DATABASEPATH)

    # Check if the database connection is successful
    if conn is None:
        # Error while loading the database connection.
        exit(1)

    try:
        with conn:
            plotHumidity(conn)
            plotTemperatureFromHumidity(conn)
            plotTemperatureFromPressure(conn)
            plotBarometricPressure(conn)
    except Error as e:
        print(e)
    finally:
        conn.close()
        print("CLOSED")


if __name__ == '__main__':
    main()

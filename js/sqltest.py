import pyodbc
server = 'remema-sqlsrv.database.windows.net'
database = 'libraire'
username = 'rememauser'
password = '{Remema2022}'   
driver= '{ODBC Driver 18 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM librairie")
        row = cursor.fetchone()
        while row:
            print (str(row[0]) + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3]))
            row = cursor.fetchone()


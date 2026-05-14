import pyodbc
try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LenovoRB\SQLEXPRESS;"
        "DATABASE=PracticeDB;"
        "Trusted_Connection=yes;"
    )

    print("connected")

    conn.close()
except Exception as e:
    print("failed")
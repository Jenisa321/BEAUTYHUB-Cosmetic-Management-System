import oracledb

try:
    connection = oracledb.connect(
        user="BEAUTYHUB",
        password="hub123",
        dsn="localhost:1521/XEPDB1"
    )

    print("✅ Oracle Database connected successfully!")

    connection.close()

except Exception as e:
    print("❌ Oracle connection failed!")
    print("Error:", e)
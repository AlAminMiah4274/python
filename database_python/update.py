import mysql.connector;

db_name = "pythonTestDB";

my_connection = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="amin@5078",
	database="pythonTestDB"
);


my_cursor = my_connection.cursor();
sql_query = """
	UPDATE Students
	SET Name = "Shafim Rahman"
	WHERE Roll = 101
""";

my_cursor.execute(sql_query);
my_connection.commit();
print("Table created successfully");
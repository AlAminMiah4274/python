import mysql.connector;

my_connection = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="amin@5078"
);

print(my_connection);

db_name = "pythonTestDB";
my_cursor = my_connection.cursor();
sql_query = "CREATE DATABASE " + db_name;
my_cursor.execute(sql_query);

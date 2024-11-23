import mysql.connector;
db_name = "pythonTestDB";

my_connection = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="*****",
	database=db_name
);

my_cursor = my_connection.cursor();
sql_query = """ 
	INSERT INTO Students(Roll, Name)
	VALUES(101, 'Al Amin Miah')
""";

my_cursor.execute(sql_query);
my_connection.commit();
print("Table created successfully");
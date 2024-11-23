import mysql.connector;


my_connection = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="amin@5078"
);

my_cursor = my_connection.cursor();

db_name = "studentLibraryManagementDB";
create_db_query = "CREATE DATABASE " + db_name;
my_cursor.execute(create_db_query);


use_db_query = "USE " + db_name;
my_cursor.execute(use_db_query);


student_table_query = """
	CREATE TABLE Student(
		Roll INT PRIMARY KEY,
		Student_Name VARCHAR(50)
	);
""";

my_cursor.execute(student_table_query);
my_connection.commit();


book_table_query = """
	CREATE TABLE Book(
		Book_id INT PRIMARY KEY,
		Book_name VARCHAR(50),
		Genre VARCHAR(30)
	);
""";

my_cursor.execute(book_table_query);
my_connection.commit();

librarian_table_query = """
	CREATE TABLE Librarian(
		Librarian_id INT PRIMARY KEY,
		Librarian_name VARCHAR(50)
	);
""";

my_cursor.execute(librarian_table_query);
my_connection.commit();

borrow_table_query = """
	CREATE TABLE Borrow(
		Roll INT,
		Book_id INT,
		Borrow_date DATE,
		Return_date DATE,

		PRIMARY KEY(Roll, Book_id),
		FOREIGN KEY(Roll) REFERENCES Student(Roll),
		FOREIGN KEY(Book_id) REFERENCES Book(Book_id)
	);
""";

my_cursor.execute(borrow_table_query);
my_connection.commit();


permission_table_query = """
	CREATE TABLE Permission(
		Librarian_id INT,
		Book_id INT,

		PRIMARY KEY(Librarian_id, Book_id),
		FOREIGN KEY(Librarian_id) REFERENCES Librarian(Librarian_id),
		FOREIGN KEY(Book_id) REFERENCES Book(Book_id)
	);
""";

my_cursor.execute(permission_table_query);
my_connection.commit();


print("Everything done successfully");

# #include <bits/stdc++.h>
# using namespace std;

# int main() {
# 	// your code goes here
#     int n;
#     cin >> n;
    
#     string t;
#     cin >> t;
    
#     bool flag = true;
#     if (n % 2 == 1)
#     {
#         int one = ((n + 1) / 2) - 1;
#         for (int i = 0; i < one; i++)
#         {
#             if (t[i] != '1')
#             {
#                 flag = false;
#                 break;
#             }
#         }
        
        
#         int slash = ((n + 1) / 2);
#         if (t[slash - 1] != '/')
#         {
#             flag = false;
#         }
        
#         int two = ((n + 1) / 2) + 1;
#         for (int i = two - 1; i < n; i++)
#         {
#             if (t[i] != '2')
#             {
#                 flag = false;
#                 break;
#             }
#         }
#     }
#     else 
#     {
#         flag = false;
#     }
    
#     if (flag) cout << "Yes" << "\n";
#     else cout << "No" << "\n";
    

#     return 0;
# }
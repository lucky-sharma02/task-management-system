# Todo Project
# CRUD => Create, Read, Update, Delete
 
# Step
 
# python => python -V or python --version
# pip list => display all the dependency of python
# mysql => pip install mysql-connector-python
 
# connect => connection, method
# cursor => cursor => cursor object
# execute => execute the query
 
import mysql.connector as mysql
 
con = mysql.connect(host="localhost", user="root", passwd="Mysql@123")
 
cursor = con.cursor()
 
cursor.execute("CREATE DATABASE IF NOT EXISTS TODOAPP")
# Database => collection of tables
 
 
print("Database created...")
 
cursor.execute("USE TODOAPP")
 
# create the tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tb_todo (
        id INT AUTO_INCREMENT PRIMARY KEY,
        task VARCHAR(50) NOT NULL,
        status ENUM('pending', 'completed') DEFAULT 'pending'
    )
""")
 

 
cursor.execute("SHOW TABLES")

for i in cursor:
    print(i)

    print("Table created...")


     
while True:
    print("\n Task Management")
    print("1. Add Task")
    print("2. View Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
 
    choice = input("Enter your choice: ")
 
    if choice == "1":
        task = input("Enter task: ")
        cursor.execute("INSERT INTO tb_todo (task) VALUES (%s)", (task,))
        print("Task added successfully!")
        con.commit() # commit the changes to the database
        print("Task added successfully!")
    
    elif choice == "2":
        cursor.execute("SELECT * FROM tb_todo")
        tasks = cursor.fetchall()
        if tasks:
            print("\nTasks List:")
            for task in tasks:
                print(f"ID: {task[0]} | Task: {task[1]}")
        else:
            print("No tasks available.")

    elif choice == "3":
        task_id = input("Enter task ID to update: ")
        new_task = input("Enter updated task: ")
        cursor.execute("UPDATE tb_todo SET task = %s WHERE id = %s", (new_task, task_id))
        con.commit()
        if cursor.rowcount > 0:
            print("Task updated successfully!")
        else:
            print("Task ID not found.")

    elif choice == "4":
        task_id = input("Enter task ID to delete: ")
        cursor.execute("DELETE FROM tb_todo WHERE id = %s", (task_id,))
        con.commit()
        if cursor.rowcount > 0:
            print("Task deleted successfully!")
        else:
            print("Task ID not found.")

    elif choice == "5" :
        print("Exiting task management ... ")
        break
     
    else:
        print("Invalid choice. Please try again.")
 
con.close()
   
 
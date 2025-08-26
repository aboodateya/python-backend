import sqlite3


conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    grade TEXT
)
""")
conn.commit()


def insert_student(name, age, grade):
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", (name, age, grade))
    conn.commit()
    print("✅ Student added successfully.")

def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_student(student_id, name, age, grade):
    cursor.execute("UPDATE students SET name = ?, age = ?, grade = ? WHERE id = ?", (name, age, grade, student_id))
    conn.commit()
    print("✏️ Student updated.")

def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    print("❌ Student deleted.")

def menu():
    while True:
        print("\n--- Student Manager ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            insert_student(name, age, grade)
        elif choice == "2":
            view_students()
        elif choice == "3":
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = input("Enter new grade: ")
            update_student(student_id, name, age, grade)
        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid choice, try again.")

if __name__ == "__main__":
    menu()
    conn.close()

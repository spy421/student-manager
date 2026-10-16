import json
def save_students(students):
    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(students, file, ensure_ascii=False, indent=4)
        
with open("students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

def show_students(students):
    if len(students) == 0:
        print("Список студентов пуст.")
        return
    for student in students:
        print(f"Имя: {student['name']}")
        print(f"Возраст: {student['age']}")
        print(f"Специальность: {student['major']}")
        print("-" * 25)
        
def add_student(students):
    name = input("Введите имя студента: ")
    
    while True:
        try:
            age = int(input("Введите возраст студента: "))
            if age <= 0:
                print("Возраст должен быть положительным числом. Попробуйте снова.")
            else:
                break
        except ValueError:
            print("Ошибка! Введите возраст цифрами.")
    
    major = input("Введите специальность студента: ")
    
    new_student = {
        "name": name,
        "age": age,
        "major": major 
    }
    students.append(new_student)
    save_students(students)
    print(f"Студент {name} успешно добавлен!")

def find_student(students):
    search_name = input("Введите имя студента для поиска: ")
    
    found_students = [
        student for student in students 
        if student['name'].lower() == search_name.lower()
        ]
    if found_students:
        print(f"Найдено {len(found_students)} студент(ов):")

        for student in found_students:
            print(
                f"Имя: {student['name']}, "
                f"Возраст: {student['age']}, "
                f"Специальность: {student['major']}"
            )
    else:
        print("Студент с таким именем не найден.")
    
def delete_student(students):
    delete_name = input("Введите имя студента для удаления: ")
    found = False
    for student in students:
        if student['name'].lower() == delete_name.lower():
            students.remove(student)
            found = True
            save_students(students)
            print(f"Студент {delete_name} успешно удален.")
            return
    if not found:
        print("Студент с таким именем не найден.")
        
def edit_student(students):
    edit_name = input("Введите имя студента для редактирования: ")
    found = False

    for student in students:
        if student["name"].lower() == edit_name.lower():
            found = True
            print(f"Текущие данные студента {student['name']}:")
            print(f"Возраст: {student['age']}")
            print(f"Специальность: {student['major']}")
            print(f"\nРедактирование студента {student['name']}")
            print("Оставьте поле пустым, если не хотите его менять.")

            new_name = input("Новое имя: ")
            new_age = input("Новый возраст: ")
            new_major = input("Новая специальность: ")

            if new_name.strip():
                student["name"] = new_name.strip()

            if new_age.strip():
                try:
                    age = int(new_age)
                    if age <= 0:
                        print("Возраст должен быть больше нуля. Возраст не изменён.")
                    else:
                        student["age"] = age

                except ValueError:
                    print("Возраст должен быть числом. Возраст не изменён.")

            if new_major.strip():
                student["major"] = new_major.strip()

            save_students(students)
            print("Изменения сохранены!")
            return

    if not found:
        print("Студент с таким именем не найден.")

while True:
    print("\n===STUDENT MANAGEMENT SYSTEM===")
    print("1. Показать список студентов")
    print("2. Добавить нового студента")
    print("3. Найти студента")
    print("4. Удалить студента")
    print("5. Редактировать студента")
    print("6. Выйти из программы")
    
    choice = input("Выбирете действие (1-5): ")
    
    if choice == "1":
        show_students(students)
    elif choice == "2":
        add_student(students)
    elif choice == "3":
        find_student(students)
    elif choice == "4":
        delete_student(students)
    elif choice == "5":
        edit_student(students)
    elif choice == "6":
        print("Выход из программы...")
        break
    else:
        print("Неверный выбор. Пожалуйста, выберите действие от 1 до 5.")
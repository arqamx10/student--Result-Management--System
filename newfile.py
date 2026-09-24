import json

students = []


def get_marks(subject):
    while True:
        try:
            marks = float(input("Enter " + subject + " marks: "))

            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


# Load saved students
try:
    with open("students.json", "r") as file:
        students = json.load(file)

except FileNotFoundError:
    students = []


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Result")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Edit Student")
    print("6. Exit")

    choice = input("Enter your choice: ")


    # ADD STUDENT
    if choice == "1":

        name = input("\nEnter student name: ")

        math = get_marks("Math")
        physics = get_marks("Physics")
        computer = get_marks("Computer")
        english = get_marks("English")

        student = {
            "name": name,
            "math": math,
            "physics": physics,
            "computer": computer,
            "english": english
        }

        students.append(student)

        with open("students.json", "w") as file:
            json.dump(students, file, indent=4)

        print("\nStudent added successfully!")


    # VIEW RESULT
    elif choice == "2":

        if len(students) == 0:
            print("\nNo students found.")

        else:

            print("\n===== STUDENTS =====")

            for i, student in enumerate(students, start=1):
                print(i, "-", student["name"])

            try:
                student_number = int(
                    input("\nEnter student number: ")
                )

                if 1 <= student_number <= len(students):

                    student = students[student_number - 1]

                    total_marks = (
                        student["math"]
                        + student["physics"]
                        + student["computer"]
                        + student["english"]
                    )

                    percentage = total_marks / 4

                    if percentage >= 90:
                        grade = "A+"
                        gpa = 4.0

                    elif percentage >= 80:
                        grade = "A"
                        gpa = 3.7

                    elif percentage >= 70:
                        grade = "B"
                        gpa = 3.0

                    elif percentage >= 60:
                        grade = "C"
                        gpa = 2.5

                    elif percentage >= 50:
                        grade = "D"
                        gpa = 2.0

                    else:
                        grade = "F"
                        gpa = 0.0

                    print("\n===== RESULT CARD =====")
                    print("Student:", student["name"])
                    print("Math:", student["math"])
                    print("Physics:", student["physics"])
                    print("Computer:", student["computer"])
                    print("English:", student["english"])
                    print("Total Marks:", total_marks)
                    print(
                        "Percentage:",
                        round(percentage, 2),
                        "%"
                    )
                    print("Grade:", grade)
                    print("GPA:", gpa)

                    if percentage >= 50:
                        print("Status: PASS")
                    else:
                        print("Status: FAIL")

                else:
                    print("\nInvalid student number.")

            except ValueError:
                print("\nPlease enter a valid number.")


    # SEARCH STUDENT
    elif choice == "3":

        search_name = input(
            "\nEnter student name: "
        )

        found = False

        for student in students:

            if student["name"].lower() == search_name.lower():

                print("\n===== STUDENT FOUND =====")
                print("Name:", student["name"])
                print("Math:", student["math"])
                print("Physics:", student["physics"])
                print("Computer:", student["computer"])
                print("English:", student["english"])

                found = True

        if not found:
            print("\nStudent not found.")


    # DELETE STUDENT
    elif choice == "4":

        if len(students) == 0:
            print("\nNo students found.")

        else:

            print("\n===== STUDENTS =====")

            for i, student in enumerate(students, start=1):
                print(i, "-", student["name"])

            try:

                student_number = int(
                    input(
                        "\nEnter student number to delete: "
                    )
                )

                if 1 <= student_number <= len(students):

                    deleted_student = students.pop(
                        student_number - 1
                    )

                    with open(
                        "students.json",
                        "w"
                    ) as file:
                        json.dump(
                            students,
                            file,
                            indent=4
                        )

                    print(
                        "\nStudent",
                        deleted_student["name"],
                        "deleted successfully!"
                    )

                else:
                    print("\nInvalid student number.")

            except ValueError:
                print("\nPlease enter a valid number.")


    # EDIT STUDENT
    elif choice == "5":

        if len(students) == 0:

            print("\nNo students found.")

        else:

            print("\n===== STUDENTS =====")

            for i, student in enumerate(
                students,
                start=1
            ):
                print(i, "-", student["name"])


            try:

                student_number = int(
                    input(
                        "\nEnter student number to edit: "
                    )
                )

                if 1 <= student_number <= len(students):

                    student = students[
                        student_number - 1
                    ]

                    print(
                        "\nEditing:",
                        student["name"]
                    )

                    student["name"] = input(
                        "Enter new name: "
                    )

                    student["math"] = get_marks("Math")
                    student["physics"] = get_marks("Physics")
                    student["computer"] = get_marks("Computer")
                    student["english"] = get_marks("English")


                    with open(
                        "students.json",
                        "w"
                    ) as file:

                        json.dump(
                            students,
                            file,
                            indent=4
                        )


                    print(
                        "\nStudent updated successfully!"
                    )

                else:

                    print("\nInvalid student number.")

            except ValueError:

                print("\nPlease enter a valid number.")


    # EXIT
    elif choice == "6":

        print("\nGoodbye!")
        break


    else:

        print(
            "\nInvalid choice. Please try again."
        )
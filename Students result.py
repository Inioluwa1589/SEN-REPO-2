

def calculate_grade(average):
    if average >= 70:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 45:
        return "D"
    else:
        return "F"

def main():
    student_name = input("Enter student name: ")
    matric_number = input("Enter matric number: ")

    number_of_subjects = int(input("Enter number of subjects: "))

    subjects = []
    scores = []

    for i in range(number_of_subjects):
        subject = input(f"Enter subject {i+1} name: ")
        score = float(input(f"Enter score for {subject}: "))
        subjects.append(subject)
        scores.append(score)

    total = sum(scores)
    average = total / number_of_subjects
    grade = calculate_grade(average)

    print("\n--- STUDENT RESULT ---")
    print("Name:", student_name)
    print("Matric Number:", matric_number)

    for i in range(number_of_subjects):
        print(subjects[i], ":", scores[i])

    print("Total Score:", total)
    print("Average Score:", average)
    print("Grade:", grade)

    with open("student_results.txt", "a") as file:
        file.write(f"{student_name}, {matric_number}, Total: {total}, Average: {average}, Grade: {grade}\n")

if __name__ == "__main__":
    main()

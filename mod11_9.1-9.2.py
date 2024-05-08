def write_grades_to_file():
    print("Enter any number of grades (-1 to quit)")

    file = open("grades.txt",'w')

    while True:
        grade = input()
        if grade == "-1":
            break
        else:
            file.write(f'{grade}\n')

def read_grades_from_file():
    with open("grades.txt","r") as file:
        grades = []

        for line in file:
            grades.append(int(line.strip()))

    file.close()

    print("Grades:")
    for grade in grades:
        print(grade)

    total = sum(grades)
    count = len(grades)
    average = sum(grades) / len(grades)

    print(f"\nTotal: {total}")
    print(f"Count: {count}")
    print(f"Average: {average:.2f}")

def main():
    write_grades_to_file()
    read_grades_from_file()

if __name__ == "__main__":
    main()
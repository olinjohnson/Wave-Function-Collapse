import pandas
import random

periods = 8

def main():
    classes = pandas.read_csv("./course-list.csv")
    students = pandas.read_csv("./student-names-reduced.csv")

    for i in range(0, len(students)):
        chosen_courses = []
        while(len(chosen_courses) < 8):
            course = random.randrange(0, len(classes))
            if(course in chosen_courses):
                continue
            else:
                chosen_courses[len(chosen_courses)] = course

    print("LEN STUDENTS: ", len(students))


if __name__ == "__main__":
    main()

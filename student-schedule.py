import pandas
import random

periods = 8

def assign_classes():
    classes = pandas.read_csv("./course-list.csv")
    students = pandas.read_csv("./student-names-reduced.csv")

    assigned_classes = pandas.DataFrame(columns=["Name", "Period 1", "Period 2", "Period 3", "Period 4", "Period 5", "Period 6", "Period 7", "Period 8"])

    for i in range(0, len(students)):
        chosen_courses = []
        while(len(chosen_courses) < 8):
            course = random.randrange(0, len(classes))
            if(course in chosen_courses):
                continue
            else:
                chosen_courses.append(course)
        
        assigned_classes.loc[i] = [students["name"][i]] + chosen_courses

    print("Classes assigned. View them in course-assignments.csv")
    assigned_classes.to_csv("./course-assignments.csv")


def main():
    assign_classes()

if __name__ == "__main__":
    main()

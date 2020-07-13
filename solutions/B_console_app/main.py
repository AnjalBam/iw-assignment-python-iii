from IT_academy.student import Student
from IT_academy.course import AllCourses
from IT_academy.display import display_student_data



def main():
    print("""
    Welcome To IW Academy
    We provide a wide range of Tech and Programming courses to boost you 
    career in the field of technology.
    you can view the course details for free... it wont take a day ;)
    """)
    courses = AllCourses()
    courses.display_course_data()
    display_student_data()


if __name__ == '__main__':
    main()

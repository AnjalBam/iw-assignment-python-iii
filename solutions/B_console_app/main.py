from .course import AllCourses


def main():
    print("""
    Welcome To IW Academy
    We provide a wide range of Tech and Programming courses to boost you 
    career in the field of technology.
    you can view the course details for free... it wont take a day ;)
    """)
    courses = AllCourses()
    courses.display_course_data()


if __name__ == '__main__':
    main()

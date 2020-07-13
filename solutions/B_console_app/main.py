import sys

from IT_academy.student import Student
from IT_academy.course import AllCourses
from IT_academy.display import display_student_data
from IT_academy.operations import complete_course, update_data, register_student


def main():
    print("""
    Welcome To IW Academy
    We provide a wide range of Tech and Programming courses to boost you 
    career in the field of technology.
    you can view the course details for free... it wont take a day ;)
    """)
    course_prompt = input('Are you interested to view Courses?(y/n) ')
    if course_prompt == 'y' or course_prompt == 'Y':
        courses = AllCourses()
        courses.display_course_data()
    else:
        print('*' * 30)
        print("Thank you for visiting... \nIW Academy")
        sys.exit()
    del course_prompt
    done_operating = False
    while not done_operating:
        print('*' * 30)
        print('Here\'s a list of operations you could take:')
        print('1. Register')
        print('2. View all student data')
        print('3. Student Course completed')
        print('4. Update Data')
        operation_prompt = int(
                input('What operation would you like to have?(1/2/3/4) ')
        )
        if operation_prompt == 1:
            register_student()

        elif operation_prompt == 2:
            display_student_data()

        elif operation_prompt == 3:
            complete_course()

        elif operation_prompt == 4:
            update_data()
        else:
            print('Invalid choice:')
            main()

        done_prompt = input('Are you done operating?(y/n) ')
        if done_prompt == 'y' or done_prompt == 'Y':
            done_operating = True
        else:
            done_operating = False

        print("Thank you for visiting"
              "Regards IW academy")


if __name__ == '__main__':
    main()

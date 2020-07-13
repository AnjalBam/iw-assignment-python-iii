import csv

from .student import Student
from .registration import RegisterStudent


def register_student():
    RegisterStudent()


def get_student_data():
    students_data_list = []
    with open('student_details.csv', 'r', newline='') as student_details:
        # fields = ['name', 'email', 'age', 'address', 'active_status',
        #           'course_status',
        #           'total_due', 'total_deposited', 'two_installment_plan']
        detail_reader = csv.reader(student_details)
        for detail in detail_reader:
            students_data_list.append(detail)
    student_details.close()
    return students_data_list


def search_details():
    student_data_list = get_student_data()
    print('Enter student details:')
    std_name = input('Name: ')
    std_email = input('Email: ')
    for student_data in student_data_list:
        if std_name in student_data and std_email in student_data:
            std_detail = student_data
            break
    else:
        print('No such detail found!')
        return
    return std_detail


def complete_course():
    std_detail = search_details()
    if std_detail:
        std = Student()
        std.set_data_from_csv(tuple(std_detail))
        std.course_completed()
    else:
        print('Invalid Data entered! No such record found!')


def update_data():
    std_detail = search_details()
    if std_detail:
        std = Student()
        std.set_data_from_csv(tuple(std_detail))
        std.delete()
        done_updating = False
        while not done_updating:
            print('*' * 30)
            print("""
            What would you like to update:
            1. Name
            2. Age
            3. Email
            4. Address
            """)
            print('*' * 30)
            is_choice_valid = False
            while not is_choice_valid:
                is_choice_valid = True
                choice_prompt = int(input('Enter your choice(1/2/3/4) '))
                if choice_prompt == 1:
                    name = input('Enter name: ')
                    std.update_name(name)
                elif choice_prompt == 2:
                    age = int(input('Enter Age: '))
                    std.update_age(age)
                elif choice_prompt == 3:
                    email = input('Enter Email: ')
                    std.update_email(email)
                elif choice_prompt == 4:
                    address = input('Enter Address: ')
                    std.update_address(address)
                else:
                    print('Invalid Choice!! Try Again.')
                    is_choice_valid = False

            finished_updating = input('Are you done updating?(y/n) ')
            if finished_updating == 'y' or finished_updating == 'Y':
                done_updating = True
            else:
                done_updating = False
        std.save()



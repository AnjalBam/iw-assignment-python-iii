import csv
import pprint


def display_student_data():
    with open('student_details.csv', 'r', newline='') as student_details:

        fields = ['name', 'email', 'age', 'address', 'active_status',
                  'course_status',
                  'total_due', 'total_deposited', 'two_installment_plan']
        detail_reader = csv.DictReader(student_details, fieldnames=fields)
        print('All Student Details')
        print('*' * 30)
        for detail in detail_reader:
            print()
            pprint.pprint(detail)
            print('-' * 30)


if __name__ == '__main__':
    display_student_data()

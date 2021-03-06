import csv
from .course import Course


class Student(Course):
    name = ''
    address = ''
    age = ''
    email = ''

    total_deposited = 0
    two_installments = False
    is_course_completed = False
    is_active = True

    def __init__(self):
        self.total_due = self.course_cost = super().total_cost
        self.one_installment_amt = super().one_installment_cost
        self.two_installment_amt = super().two_installment_cost

    # ['name', 'email', 'age', 'address', 'active_status',
    #  'course_status',
    #  'total_due', 'total_deposited', 'two_installment_plan']

    def set_data_from_csv(self, data_tuple):
        (self.name, self.email, self.age, self.address, self.is_active,
         self.is_course_completed, self.total_due, self.total_deposited,
         self.two_installments) = data_tuple

    def payment(self, paid_amt):
        if self.total_due > 0:
            if self.two_installments:
                if paid_amt != self.two_installment_amt:
                    print('Sorry, But you\'re only allowed to pay {} per '
                          'installment'.format(self.two_installment_amt))
                    return
                else:
                    self.total_due -= paid_amt
                    self.total_deposited += paid_amt
            else:
                if paid_amt == self.one_installment_cost:
                    self.total_due -= paid_amt
                    self.total_deposited += paid_amt
                else:
                    print('Sorry Your plan is One installment')
                    print(f'You should pay Rs.{self.one_installment_cost}')
                    return
        else:
            print('You dont have any due left!\n Thank you!')

    def get_student_info(self):
        print('*' * 10)
        print('Student Details:')
        print(f'Name: {self.name}')
        print(f'Email: {self.email}')
        print(f'Age: {self.age}')
        print(f'Address: {self.address}')
        print('-' * 10)
        print('Payment Details')
        if self.two_installments:
            print('Payment Plan: Two Installments')
        else:
            print('Payment Plan: One Installment')
        print('Total Deposited: {}'.format(self.total_deposited))
        print('Total Due: {}'.format(self.total_due))
        print('*' * 10)

    def set_data(self, name='', age='', email='',
                 address='', change_payment_plan=False):
        if name:
            self.update_name(name)
        if age:
            self.update_age(age)
        if email:
            self.update_email(email)
        if change_payment_plan:
            self.change_payment_plan(change_payment_plan)
        if address:
            self.update_address(address)

    def update_name(self, name):
        self.name = name

    def update_age(self, age):
        self.age = age

    def update_email(self, email):
        self.email = email

    def update_address(self, address):
        self.address = address

    def change_payment_plan(self, payment_plan):
        if self.total_due == self.course_cost:
            self.two_installments = payment_plan
        else:
            print('Sorry, but You cannot change the payment plan right now!')
            return

    def update_data(self, name='', age='', email='',
                    address='', change_payment_plan=False):
        self.delete()
        if name:
            self.update_name(name)
        if age:
            self.update_age(age)
        if email:
            self.update_email()
        if change_payment_plan:
            self.change_payment_plan(change_payment_plan)
        if address:
            self.update_address(address)
        self.save()

    def leave_program(self):
        self.is_active = False

    def course_completed(self):
        self.is_active = False
        print('Congratulations! You have successfully completed the course!')
        print(f'Your deposit of Rs.{self.total_deposited} is Returned!')
        self.total_deposited = 0
        self.total_due = 0
        self.delete()

    def get_student_data_as_tuple(self):
        student_data = (self.name, self.email, self.age, self.address,
                        self.is_active, self.is_course_completed,
                        self.total_due, self.total_deposited,
                        self.two_installments)
        return student_data

    def delete(self):
        print('deleting data...')
        all_data_list = []
        with open('student_details.csv', 'r', newline='') as student_details:
            detail_reader = csv.reader(student_details)
            for detail in detail_reader:
                all_data_list.append(tuple(detail))
                if self.name in detail and self.email in detail:
                    all_data_list.remove(tuple(detail))
        with open('student_details.csv', 'w', newline='') as student_details:
            detail_writer = csv.writer(student_details)
            detail_writer.writerows(all_data_list)
        print('Deleted!')

    def save(self):
        with open('student_details.csv', 'a', newline='') as student_details:
            student_data = self.get_student_data_as_tuple()
            data_writer = csv.writer(student_details)
            data_writer.writerow(student_data)
        student_details.close()


if __name__ == '__main__':
    std = Student()
    std.set_data_from_csv((
                          'Anjal', 'anjal@anjal.com', '20', 'Dhangadhi', 'True',
                          'False', '10000', '10000', 'True'))
    std.payment(10000)
    std.get_student_info()
    std.delete()

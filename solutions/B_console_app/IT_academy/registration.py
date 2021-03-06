from .student import Student
from .course import Course


class RegisterStudent:
    name = ''
    age = ''
    address = ''
    email = ''
    in_two_installments = False
    course_detail = Course()

    def __init__(self):
        print('*' * 30)
        print('Thank you for Registering for the IW Academy!')
        print('*' * 30)
        print('Since you\'ve viewed the courses and are interested in our '
              'courses, here\'s the payment plan.')
        print(f'The total course cost is Rs.{self.course_detail.total_cost}')
        print(f'You have two types of payment options:\n1. One installment '
              f'payment (Rs.{self.course_detail.one_installment_cost})\n'
              f'2. Two installment payment (Rs.'
              f'{self.course_detail.two_installment_cost}')
        _ = input('Please hit enter to continue... ')
        self.register()

    def register(self):
        self.name = input('Enter your name: ')
        self.age = input('How old are you? ')
        self.address = input('Please enter your address: ')
        self.email = input('Your E-mail address: ')
        print('-' * 20)
        print('The Total deposit would be Rs. 20,000')
        print('Here are your Payment Options:')
        print('1. In a Single Installment(Rs. 20,000)')
        print('2. In two installments(Rs. 10,000 each)')
        is_choice_invalid = True
        while is_choice_invalid:
            print('-' * 15)
            pref = int(input('What would you prefer? (1/2) '))
            if pref == 1:
                self.in_two_installments = False
                is_choice_invalid = False
            elif pref == 2:
                self.in_two_installments = True
                is_choice_invalid = False
            else:
                print('Invalid Choice! Please enter valid value!')
        self.assert_data()

    def update_data(self):
        print("""
        What would you like to update?
        1. Name
        2. Age
        3. Email
        4. Address
        """)
        updated = False
        while not updated:
            # updated = True
            choice = int(input('Enter your choice: (1/2/3/4)'))
            if choice == 1:
                self.name = input('Enter your name: ')
            elif choice == 2:
                self.age = input('Enter Age: ')
            elif choice == 3:
                self.email = input('Enter Email: ')
            elif choice == 4:
                self.address = input('Enter Address: ')
            else:
                # updated = False
                print("Invalid Choice!! Please select valid choice")
            more_updates = input("Do you want to update anything else?(y/n) ")
            if more_updates == 'y' or more_updates == 'Y':
                updated = False
            else:
                updated = True

    def assert_data(self):
        is_asserted = False
        while not is_asserted:
            print(f"""
Here's the data you entered. Please confirm it's valid
{'-' * 8}
Name: {self.name}
Age: {self.age}
E-mail: {self.email}
Address: {self.address}
Payment Plan: {'Two Installments'
            if self.in_two_installments else 'In Two Installments'}
""")
            is_valid = input('Is Data shown above valid? (y/n) ')
            if is_valid == 'y' or is_valid == 'Y':
                student = Student()
                student.set_data(self.name, self.age, self.email,
                                 self.address, self.in_two_installments)
                student.save()
                # print('Valid Data!')
                is_asserted = True
            else:
                self.update_data()


if __name__ == '__main__':
    regs = RegisterStudent()
    regs.assert_data()

class Course:
    total_cost = 20000
    one_installment_cost = total_cost
    two_installment_cost = total_cost / 2

    def set_total_cost(self, total_cost):
        self.total_cost = total_cost


class AllCourses(Course):
    all_courses = [
        {
            'name': 'Python Programming For All',
            'duration': '2 Months'
         },
        {
            'name':'Web development with HTML, CSS and JavaScript',
            'duration': '3 Months'
        },
        {
            'name': 'Git and Github Crash Course',
            'duration': '1 Month'
         },
        {
            'name': 'Learn Python By making Projects',
            'duration': '2 Months'
         },
        {
            'name': 'Intermediate Java for Android Development',
            'duration': '3 Months'
        },
        {
            'name': 'Django Full Stack Web Development',
            'duration': '2 Months'
        }
    ]

    def add_course(self, course_name, course_duration):
        course = {'name': course_name, 'duration': course_duration}
        self.all_courses.append(course)

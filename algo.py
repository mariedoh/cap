import pandas as pd
import random
import requests
class Course:
    def __init__(self, name):
        #this variable represents the name of the course
        self.name = name
        #this variable represents the students taking that course
        self.students = []
        self.red_flags = []
        #this represents the courses that this course cannot be grouped with
        '''this variable represents the students taking the course as a major course 
        elective and is to be used in implementing the soft constraints'''
        self.majors = 0;
        self.size = None;
        self.color = 9003;

    #mutator methods for the course attributes
    def  set_students(self, student):
        self.students.append(student)
    def  set_majors(self):
        self.majors += 1
    def set_name(self, name):
        self.name = name
    def set_size(self, size):
        self.size = size
    def update_red(self, red):
        for x in red:
            if x not in self.red_flags:
                self.red_flags.append(x)
    def set_red(self, red):
        self.red_flags = red
    def set_color(self, color):
        self.color = color

    #accessor method for name, students and majors variables
    def get_color(self):
        return self.color
    def get_red(self):
        return self.red_flags
    def get_name(self):
        return self.name
    def get_students(self):
        return self.students
    def get_majors(self):
        return self.majors
    def get_size(self):
        return self.size
    def is_compatible(self, others):
        if not others:
            return True
        for x in others:
            if x.get_name() in self.red_flags: 
                return False
        return True
    def get_size(self):
        self.set_size(len(self.students))
        return len(self.students)
class Student:
    def __init__(self, ID, course):
        #this variable represents the student's id
        #these represent is the student's program and year group
        self.id = ID
        self.course = course        
        self.year_group = ID[-4:]
        self.enrolled = []
    def set_enrolled(self, enrolled):
        self.enrolled = enrolled
    def get_ID(self):
        return self.id
    def get_course(self):
        return self.course
    def get_year_group(self):
        return self.year_group


def scheduler(exam_period, courses):
    ''' 
    This function takes a variable representing the number of days available for examinations and 
    the list of course objects to be scheduled and 
    Returns:
        List: Courses that couldn't be scheduled 
    '''
    unscheduled = []
    scheduled = []
    my_queue = []
    visited = []
    start = courses[0]
    my_queue.append(start)

    while my_queue:
        current = my_queue.pop(0)
        reds = [courses[course_index_hash_map[x]] for x in current.get_red()]
        colors = [y.get_color() for y in reds if y in visited]
        for x in range(0, exam_period):
            if x not in colors:
                current.set_color(x)
                scheduled.append(current)
                break

        visited.append(current)
        if current.get_color() not in range(0, exam_period):
            unscheduled.append(current)            

        my_queue.extend([y for y in reds if y not in my_queue and y not in visited])
        my_queue.sort(key=lambda x: len(x.get_red()), reverse=True)

    return (scheduled, unscheduled)


def excel_to_csv(excel_file_name):
    file_as_df = pd.read_excel(excel_file_name, header=0)
    return file_as_df

def drop_unneccessary_columns(enrol_df):
    return enrol_df[enrol_df['Type'] == "Schedule"] 

def prep_student_and_courses(enrol_excel_name):
    #opening the file as a panda dataframes and 
    #dropping all unnecessary courses that are not being scheduled
    enrol_df = drop_unneccessary_columns(excel_to_csv(enrol_excel_name))
    #initializing the list of Course objects to be scheduled
    courses = []
    students = []

    #setting up course objects
    courses_in_set = enrol_df["Course Name"].unique()
    index = 0
    for x in courses_in_set:
        #initialising the course
        new_course = Course(x)
        courses.append(new_course)
        #hash its location for quick retrieval later
        course_index_hash_map[x] = index
        index +=1

    #Setting up student objects
    students = enrol_df["Generated ID"].unique()
    for id in students:
        #get all the rows associated with the student
        student_set = enrol_df[enrol_df["Generated ID"] == id]

        #identify the student's program
        student_program = student_set["Student Program"].iloc[[0]]
        #use that data to create the student object
        student = Student(id, student_program)
        #get all the courses the student is enrolled in 
        enrolled =  student_set["Course Name"].unique().tolist()
        major_courses = student_set[student_set["Course Sub Category"] == "Required Major Classes"]["Course Name"].unique().tolist()
        #update course records as necessary.   
        for x in enrolled:
            course_loc = course_index_hash_map[x]
            #add student to the course's student list
            courses[course_loc].set_students(student)
            if x in major_courses:
                #update the courses's major var, if the student is taking it as a required major course
                courses[course_loc].set_majors()
            #update the red flags list in all courses to prevent clashing
            courses[course_loc].update_red(enrolled)

    courses.sort(key=lambda x: len(x.get_red()), reverse=True)
    return (courses, students, course_index_hash_map)

def prep_classroom_data(class_excel_name):
    classes = excel_to_csv(class_excel_name)
    #getting the total classroom capacity
    classrooms = classes['Capacity'].value_counts().to_dict()
    return classrooms

def prep_output(courses, num_days):
    # printing result of scheduling
    output = [[] for _ in range (num_days)]
    for co in courses:
        if co.get_color() in range(num_days):
            output[co.get_color()].append(co.get_name()) 

    for x in output:
        print(x, "\n")


def main(enrol_excel_name, classroom_excel_name, num_days):
    variables = prep_student_and_courses(enrol_excel_name)
    courses = variables[0]
    students = variables[1]
    course_index_hash_map = variables[2]
    classrooms = prep_classroom_data(classroom_excel_name)
    hello = scheduler(num_days, courses)
    print(len(hello[0]))
    print(len(courses))
    prep_output(courses, num_days)
    print("Unscheduled:\n", [x.get_name() for x in hello[1]])

course_index_hash_map = {}
main("original.xlsx", "classrooms.xlsx", 8)
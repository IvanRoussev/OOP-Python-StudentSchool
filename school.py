import json

from .student import Student


class School():

    def __init__(self, name):
        self.name = name

        with open('data/school.json') as fp:
            data = json.load(fp)
        self.students = []
        for item in data:
            self.students.append(Student(item['name'], item['student_id'], item['term']))
    
    def __len__(self):
        return len(self.students)



    def get_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student



    def get_by_name(self, name):
        instanceStudents = []
        for student in self.students:
            if student.name == name:
                instanceStudents.append(student)
        
        return instanceStudents


    def add(self, instance):
        return self.students.append(instance)
        

    def delete(self, student_id):
        for items in self.students:
            if items.student_id == student_id:
                self.students.remove(items)
                return True
            else:
                return False


    def save(self):
        new_items = []
        for items in self.students:
            new_items.append(Student.to_dict(items))

        with open("data/school.json", "w") as fp:
            data = json.dump(new_items, fp)

        return data

            

    
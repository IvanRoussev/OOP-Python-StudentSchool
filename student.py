from multiprocessing.sharedctypes import Value
from operator import index
from pickle import TRUE
import re

class Student:

    def __init__(self, name, student_id:str, term:int=1):
        self.name = name
        self.term = term
        self.student_id = student_id

        if (type(self.name) == int):
            raise ValueError
        
        if type(self.student_id) != str or (len(self.student_id) != 9):
            raise ValueError

        if self.student_id[0] != 'A' or self.student_id[1] != '0':
            raise ValueError
        
        if type(self.term) != int:
            raise ValueError

    def to_dict(self):
        return dict(name = self.name, student_id = self.student_id, term = self.term)


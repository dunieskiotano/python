class Person:
    def __init__(self, fname =None,lname = None, age = None, gender=None):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    
    def setFirstName(self, fname):
        self.fname = fname

    def getFirstName(self):
        return self.fname

    def setLastName(self, lname):
        self.lname = lname

    def getLastName(self):
        return self.lname

    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age
    
    def setGender(self, gender):
        self.gender = gender
        
    def getGender(self):
        return self.gender
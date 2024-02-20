# main.py
class StudentsInMLOps:
    def __init__(self, totalStudents):
        self.totalStudents = totalStudents

    def getTotalStudents(self):
        return self.totalStudents
    
    def addStudent(self):
        self.totalStudents += 1
    
    def removeStudent(self):
        self.totalStudents -= 1
    
    def getClassName(self):
        return "Machine Learning Operations (CS-B)"

# Create an instance of StudentsInMLOps
mlops_class = StudentsInMLOps(5)

# Call the methods
mlops_class.addStudent()
mlops_class.removeStudent()

# Print the results
print(mlops_class.getTotalStudents())
print(mlops_class.getClassName())

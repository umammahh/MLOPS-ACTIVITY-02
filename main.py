
class mlops:
        def __init__(self , totalStudents):
            self.totalStudents = totalStudents
        
        def getTotalStudents(self):
            return self.totalStudents

        def addStudents(self):
            self.totalStudents += 1

        def removeStudents(self):
            self.totalStudents -= 1
        
        def getClassName(self):
            return "MLOPS CS-B"
        

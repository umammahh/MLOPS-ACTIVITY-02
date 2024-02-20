# test.py
from main import StudentsInMLOps

def test_enroll_and_drop_students():
    classroom = StudentsInMLOps(5)
    classroom.enrollStudents(5)
    assert classroom.getTotalStrength() == 10
    classroom.dropStudents(2)
    assert classroom.getTotalStrength() == 8

def test_class_name():
    classroom = StudentsInMLOps(5)
    assert classroom.getClassName() == "Machine Learning Operations (CS-B)"

import pytest
from ..classTeacher import Teacher, DisciplineTeacher


@pytest.fixture()
def teacher_fixture():
    Teacher.teachers_list.clear()
    teacher = Teacher("Эйбел Херциг", "Стэнфордский университет", 4)
    return teacher


@pytest.fixture()
def dis_teacher_fixture():
    DisciplineTeacher.teachers_list.clear()
    discipline_teacher = DisciplineTeacher("Эйбел Херциг", "Стэнфордский университет",
                                4, "Python", "Директор вышки")
    return discipline_teacher

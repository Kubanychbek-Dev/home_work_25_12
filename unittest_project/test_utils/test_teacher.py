import unittest
from teacher import Teacher, DisciplineTeacher

"""Testing class Teacher"""
class TestTeacher(unittest.TestCase):
    teacher = Teacher("Эйбел Херциг", "Стэнфордский университет", 4)

    def test_get_name(self):
        self.assertEqual(self.teacher.get_name(), "Эйбел Херциг")

    def test_get_education(self):
        self.assertEqual(self.teacher.get_education(), "Стэнфордский университет")

    def test_get_experience(self):
        self.assertEqual(self.teacher.get_experience(), 4)

    def test_set_experience(self):
        self.assertEqual(self.teacher.set_experience(8), 8)

    def test_get_teacher_data(self):
        self.assertEqual(self.teacher.get_teacher_data(), "Эйбел Херциг, образование Стэнфордский университет, опыт работы 4 года")

    def test_add_mark(self):
        self.assertEqual(self.teacher.add_mark("Robert", 5), "Эйбел Херциг поставил оценку 5 студенту Robert")

    def test_remove_mark(self):
        self.assertEqual(self.teacher.remove_mark("John", 3), "Эйбел Херциг удалил оценку 3 студенту John")

    def test_give_a_consultation(self):
        self.assertEqual(self.teacher.give_a_consultation("KC-15"), "Эйбел Херциг провел консультацию в классе KC-15")

    def test_show_teachers_list(self):
        self.assertEqual(self.teacher.show_teachers_list(), "Данные выведены")

    """Testing fire_teacher"""
    def test_check_is_empty_list(self):
        self.assertEqual(self.teacher.fire_teacher("John"), "Учителя John нету в списке (или уже был уволен)")

    def test_fire_teacher(self):
        self.assertEqual(self.teacher.fire_teacher("Эйбел Херциг"), "Учитель Эйбел Херциг уволен")


"""Testing class DisciplineTeacher"""
class TestDisciplineTeacher(unittest.TestCase):
    discipline = DisciplineTeacher("Эйбел Херциг", "Стэнфордский университет", 4,"Python", "Директор вышки")

    def test_get_discipline(self):
        self.assertEqual(self.discipline.get_discipline(), "Python")

    def test_get_job_title(self):
        self.assertEqual(self.discipline.get_job_title(), "Директор вышки")

    def test_get_teacher_data(self):
        self.assertEqual(self.discipline.get_teacher_data(), "Эйбел Херциг, образование Стэнфордский университет, опыт работы 4 года Предмет: Python, должность: Директор вышки")

    def test_add_mark(self):
        self.assertEqual(self.discipline.add_mark("Robert", 5), "Эйбел Херциг поставил оценку 5 студенту Robert. Предмет: Python")

    def test_remove_mark(self):
        self.assertEqual(self.discipline.remove_mark("John", 3), "Эйбел Херциг удалил оценку 3 студенту John. Предмет: Python")

    def test_give_a_consultation(self):
        self.assertEqual(self.discipline.give_a_consultation("KC-15"), "Эйбел Херциг провел консультацию в классе KC-15. По предмету Python как Директор вышки")
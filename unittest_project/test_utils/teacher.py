class Teacher:

    teachers_list = []

    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
        Teacher.teachers_list.append(self.__name)

    def get_name(self):
        return self.__name

    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    def set_experience(self, exp):
        self.__experience = exp
        return exp

    #methods
    def get_teacher_data(self):
        return (f"{self.__name}, образование {self.__education}, "
                f"опыт работы {self.__experience} года")

    def add_mark(self, student, grade):
        return f"{self.__name} поставил оценку {grade} студенту {student}"

    def remove_mark(self, student, grade):
        return f"{self.__name} удалил оценку {grade} студенту {student}"

    def give_a_consultation(self, classname):
        return f"{self.__name} провел консультацию в классе {classname}"

    @classmethod
    def show_teachers_list(cls):
        if len(cls.teachers_list) != 0:
            print("Список учителей:")
            for teachers in cls.teachers_list:
                print(teachers)
        return "Данные выведены"

    @classmethod
    def fire_teacher(cls, teacher):
        if teacher not in cls.teachers_list:
            return f"Учителя {teacher} нету в списке (или уже был уволен)"
        elif teacher in cls.teachers_list:
            cls.teachers_list.remove(teacher)
            return f"Учитель {teacher} уволен"


# teacher1 = Teacher("Эйбел Херциг", "Стэнфордский университет", 4)
#teacher2 = Teacher("John", "Стэнфордский университет", 4)
#print(teacher1.get_teacher_data())
# print()
# print(teacher1.add_mark("Лукас", 5))
# print()
# print(teacher1.remove_mark("Jonh", 3))
# print()
# print(teacher1.give_a_consultation("KC-15"))
# print(teacher1.teachers_list)
# print(Teacher.fire_teacher("Эйбел Херциг"))


#Heir class
class DisciplineTeacher(Teacher):
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self.__discipline = discipline
        self.__job_title = job_title

    def get_discipline(self):
        return self.__discipline

    def get_job_title(self):
        return self.__job_title

    #methods
    def get_teacher_data(self):
        return f"{super().get_teacher_data()} Предмет: {self.__discipline}, должность: {self.__job_title}"

    def add_mark(self, student, grade):
        return f"{super().add_mark(student, grade)}. Предмет: {self.__discipline}"

    def remove_mark(self, student, grade):
        return f"{super().remove_mark(student, grade)}. Предмет: {self.__discipline}"

    def give_a_consultation(self, cls):
        return (f"{super().give_a_consultation(cls)}. По предмету"
                f" {self.__discipline} как {self.__job_title}")


#object
# dis = DisciplineTeacher("Эйбел Херциг", "Стэнфордский университет", 4,"Python", "Директор вышки")
#
# dis.set_experience(8)
# print(dis.get_discipline())
# print()
# print(dis.get_job_title())
# print()
# print(dis.get_teacher_data())
# print()
# print(dis.add_mark("Лукас", 5))
# print()
# print(dis.remove_mark("Jonh", 3))
# print()
# print(dis.give_a_consultation("KC-15"))
# print(dis.teachers_list)
#
# Python
#
# Директор вышки
#
# Эйбел Херциг, образование Стэнфордский университет, опыт работы 8 года Предмет: Python, должность: Директор вышки
#
# Эйбел Херциг поставил оценку 5 студенту Лукас. Предмет: Python
#
# Эйбел Херциг удалил оценку 3 студенту Jonh. Предмет: Python
#
# Эйбел Херциг провел консультацию в классе KC-15. По предмету Python как Директор вышки
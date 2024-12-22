"""Testing class Teacher"""
def test_get_name(teacher_fixture):
    get_name = teacher_fixture.get_name()
    assert get_name == "Эйбел Херциг"


def test_get_education(teacher_fixture):
    get_education = teacher_fixture.get_education()
    assert get_education == "Стэнфордский университет"


def test_get_experience(teacher_fixture):
    get_experience = teacher_fixture.get_experience()
    assert get_experience == 4


def test_set_experience(teacher_fixture):
    assert teacher_fixture.set_experience(8) == 8


def test_get_teacher_data(teacher_fixture):
    get_teacher_data = teacher_fixture.get_teacher_data()
    assert get_teacher_data == "Эйбел Херциг, образование Стэнфордский университет, опыт работы 4 года"


def test_add_mark(teacher_fixture):
    add_mark = teacher_fixture.add_mark("Kuba", 5)
    assert add_mark == "Эйбел Херциг поставил оценку 5 студенту Kuba"


def test_remove_mark(teacher_fixture):
    remove_mark = teacher_fixture.remove_mark("Jacob", 3)
    assert remove_mark == "Эйбел Херциг удалил оценку 3 студенту Jacob"


def test_give_a_consultation(teacher_fixture):
    give_a_consultation = teacher_fixture.give_a_consultation("KC-15")
    assert give_a_consultation == "Эйбел Херциг провел консультацию в классе KC-15"


def test_show_teachers(teacher_fixture):
    show_teachers = teacher_fixture.show_teachers_list()
    assert show_teachers == "Данные выведены"


def test_check_is_empty_list(teacher_fixture):
    is_empty_list = teacher_fixture.fire_teacher("John")
    assert is_empty_list == "Учителя John нету в списке (или уже был уволен)"


def test_fire_teacher(teacher_fixture):
    fire_teacher = teacher_fixture.fire_teacher("Эйбел Херциг")
    assert fire_teacher == "Учитель Эйбел Херциг уволен"


"""Testing class DisciplineTeacher"""
def test_get_discipline(dis_teacher_fixture):
    get_discipline = dis_teacher_fixture.get_discipline()
    assert get_discipline == "Python"


def test_get_job_title(dis_teacher_fixture):
    get_job_title = dis_teacher_fixture.get_job_title()
    assert get_job_title == "Директор вышки"


def test_get_teacher_data2(dis_teacher_fixture):
    get_teacher_data = dis_teacher_fixture.get_teacher_data()
    assert get_teacher_data == "Эйбел Херциг, образование Стэнфордский университет, опыт работы 4 года Предмет: Python, должность: Директор вышки"


def test_add_mark_2(dis_teacher_fixture):
    add_mark = dis_teacher_fixture.add_mark("Harry", 5)
    assert add_mark == "Эйбел Херциг поставил оценку 5 студенту Harry. Предмет: Python"


def test_remove_mark_2(dis_teacher_fixture):
    remove_mark = dis_teacher_fixture.remove_mark("Tom", 3)
    assert remove_mark == "Эйбел Херциг удалил оценку 3 студенту Tom. Предмет: Python"


def test_give_a_consultation_2(dis_teacher_fixture):
    give_a_consultation = dis_teacher_fixture.give_a_consultation("KC-15")
    assert give_a_consultation == "Эйбел Херциг провел консультацию в классе KC-15. По предмету Python как Директор вышки"
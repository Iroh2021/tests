from unique import get_unique_names, get_course_mentors, get_names_courses, get_top_names
import unittest

class TestFuncttions(unittest.TestCase):
    def test_get_unique_names(self):
        expected_result = ('Уникальные имена преподавателей:', 'Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий')
        self.assertEqual(get_unique_names(), expected_result)

    def test_get_top_names(self):
        top_names = get_top_names()
        names_count = len(top_names.split('раз(а)')) - 1 
        self.assertEqual(names_count, 3)

    def test_get_names_courses(self):
        mentors_names = get_names_courses()
        for names in mentors_names:
            for name in names:
                self.assertEqual(len(name.split()), 1)

    def test_get_course_mentors(self):
        result = get_course_mentors()
        self.assertEqual(result, 6)

if __name__=='__tests1__':
    unittest.main()
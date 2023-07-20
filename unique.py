from collections import Counter

courses = ["Python-разработчик с нуля", "Java-разработчик с нуля", "Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]

mentors = [
	["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

def get_unique_names():
	all_list = mentors[0]+mentors[1]+mentors[2]+mentors[3]
	all_names_list = []
	for mentor in all_list:
		name = mentor.split()[0]
		all_names_list.append(name)
	unique_names = set(all_names_list)
	unique_names = list(unique_names)
	all_names_sorted = sorted(unique_names)
	finale_names = ', '.join(all_names_sorted)
	return ('Уникальные имена преподавателей:', finale_names)

def get_top_names():
	names = []
	for mentor_group in mentors:
		names += [name.split()[0] for name in mentor_group]
		counter = Counter(names)
		top_names = counter.most_common(3)
		result = 'Топ 3 популярных имен:\n'
	for name, count in top_names:
		result += f'{name}: {count} раз(а) '
	return result

def get_names_courses():
	mentors_names = []
	for m in mentors:
		course_names = []
		for name in m:
			n, f = name.split()
			course_names.append(n)
		mentors_names.append(course_names)
	return mentors_names

def get_course_mentors():
	pairs = []
	count = 0
	for id1 in range(len(mentors)):
		for id2 in range(len(courses)):
			if id1 == id2:
				continue
			else:
				set1 = set(get_names_courses()[id1])
				set2 = set(get_names_courses()[id2])
				inter = set1.intersection(set2)
				inter = list(sorted(inter))
				if inter:
					if inter not in pairs:
						pairs.append(inter)
						print(f"На курсах '{courses[id1]}' и '{courses[id2]}' преподают: {', '.join(inter)}")	
						count += 1
	return count
print(get_course_mentors())
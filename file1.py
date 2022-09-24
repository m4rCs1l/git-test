def get_date():
	date = input('Введите дату текущего дня (формат: день.месяц.год): ')
	clndr = date.split('.')
	print(clndr)
get_date()

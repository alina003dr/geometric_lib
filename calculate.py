import circle
import square '''Импортируем модули для фигур круг и квадрат'''

figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {} '''Списки доступных фигур и функций'''

def calc(fig, func, size): '''Вычисляет указанную функцию (периметр или площадь) для заданной фигуры (круг или квадрат)'''
	assert fig in figs '''Проверяем, что фигура и функция являются допустимыми'''
	assert func in funcs

	result = eval(f'{fig}.{func}(*{size})') '''Вычисляем результат с помощью eval'''
	print(f'{func} of {fig} is {result}')

if __name__ == "__main__":
	func = '' '''переменная для хранения названия функции'''
	fig = '' '''переменная для хранения названия фигуры'''
	size = list() '''список для хранения размеров фигуры'''
    
	while fig not in figs: '''Запрашиваем у пользователя название фигуры'''
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs: '''Запрашиваем у пользователя название функции'''
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1): '''Запрашиваем у пользователя размеры фигуры'''
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size) '''Вызываем функцию calc с введенными данными'''




import circle
import square
import triangle

figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']
sizes = {
    'circle-area': 1,
    'circle-perimeter': 1,
    'square-area': 1,
    'square-perimeter': 1,
    'triangle-area': 3,
    'triangle-perimeter': 3
}


def calc(fig, func, size):
    # Проверка наличия передаваемого аргумента fig in figs
    assert fig in figs

    # Проверка наличия передаваемого аргумента func in funcs
    assert func in funcs

    # Проверка на соответсвие количества аргументов
    key = f'{fig}-{func}'
    expected_args = sizes.get(key)
    assert expected_args is not None
    assert len(size) == expected_args

    # Проверка аргумента на неотрицание
    assert all(s >= 0 for s in size)

    # Проверка существование тругольника
    if fig == 'triangle':
        a, b, c = size
        assert a + b > c and a + c > b and c + b > a

    # Вызов функции
    module = globals()[fig]
    result = getattr(module, func)(*size)
    return result

if __name__ == "__main__":
	func = ''
	fig = ''
	size = list()
    
	while fig not in figs:
		fig = input(f"Enter figure name, avaliable are {figs}:\n")
	
	while func not in funcs:
		func = input(f"Enter function name, avaliable are {funcs}:\n")
	
	while len(size) != sizes.get(f"{func}-{fig}", 1):
		size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
	
	calc(fig, func, size)
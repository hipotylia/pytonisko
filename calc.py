def add(_a: float, _b: float) -> float:
    return _a + _b


def subtract(_a: float, _b: float) -> float:
    return _a - _b


def multiply(_a: float, _b: float) -> float:
    return _a * _b


def divide(_a: float, _b: float) -> float:
    return _a / _b


def power(_a: int, _b: int) -> int:
    return _a ** _b


def input_num(_txt: str) -> float:
    return float(input(_txt))


print('Hi')
print('Look - I can calculate :)')
print(f'10 + 15 = {add(10, 15)}')
print(f'30 - 15 = {subtract(30, 15)}')
print(f'5 * 9 = {multiply(5, 8)}')
print(f'42 / 7 = {divide(42, 7)}')
print(f'3 ^ 2 = {power(3, 2)}')
print('Everything is OK, right?')
print()

print('Now I will calculate on difrent numbers, and..')
print('..its gonna be numbers with decimals!')
print('15.67 + 6.789 = ', add(15.67, 6.789))
print('4.12 - 10.555 = ', subtract(4.12, 10.555))
print('2.5 * 3.8 = ', multiply(2.5, 3.8))
print('100.23 / 3.12 =', divide(100.23, 3.12))
print()

print('I can do also one thing. I think you gonna be suprised ;)')
print("i'm gonna calculate any number that you want! If you want to see this just give me numbers to count")
num1 = input_num('Input first number: ')
num2 = input_num('Input second number: ')
print(num1, '+', num2, '=', add(num1, num2))
print(num1, '-', num2, '=', subtract(num1, num2))
print(num1, '*', num2, '=', multiply(num1, num2))
print(num1, ':', num2, '=', divide(num1, num2))
print('I hope you like it! Have a nice day:D')

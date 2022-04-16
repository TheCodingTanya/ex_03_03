# 1
def func(x) :
    print(x)

func(10)
func(20)

# 2
def stuff():
    print('Hello')
    return
    print('World')

stuff()

# 3
def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')

# 4
def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

# ex_04_06
def computepay(h, r):
    if h == 40:
        return h * r
    elif h >= 40:
        return 40 * r + (h - 40) * (1.5 * r)
h = input("Enter Hours:")
r = input("Enter Rate:")
h = float(h)
r = float(r)

p = computepay(h, r)
print("Pay", p)

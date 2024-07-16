a = float(input())
b = float(input())
x_x = (a + b) / 2
S = (b - a) / 2
n = 0
i = 0
e=pow(10,-5)
x = x_x + (e / 2)
x1 = x_x - (e  / 2)
def f(x):
    return -3.43 * x - 4.82 * x**3 + 6.14 * x**4 #There should be a function here that you are using
while S > e:
    n+=1
    S = (b - a) / 2
    print(i + 1,"|", format(a, '.7f'), "|", format(f(a), '.7f'), "|", format(x1, '.7f'), "|", format(f(x1), '.7f'), "|",format(x_x, '.7f'), "|", format(f(x_x), '.7f'), "|", format(x, '.7f'), "|", format(f(x), '.7f'), "|",format(b, '.7f'), "|", format(f(b), '.7f'), "|", format(f(x) - f(x1), '.7f'), "|", format(b - a, '.7f'))
    if (f(x) - f(x1)) <0:
	    a=x_x
    elif (f(x) - f(x1)) > 0:
	    b=x_x
    else:
	    break
    x_x = (a+b) / 2
    x= x_x+ (e/2)
    x1=x_x-(e/2)
i+=1
print("Dichotomy")
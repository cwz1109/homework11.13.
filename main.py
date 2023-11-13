#define the fomula because we need to know how many roots the quadratic will have
def root():
    y=b**2-4*a*c
    return y
#define the two fomula to solve the real roots
def quadratic1():
    y=(-b+(((b**2)-(4*a*c))**(0.5)))/(2*a)
    return str(y.real)
def quadratic2():
    y=(-b-((b**2-4*a*c)**(0.5)))/(2*a)
    return str(y.real)
#ask for the numbers of a, b, and c
a=float(input("What is a?"))
b=float(input("What is b?"))
c=float(input("What is c?"))

#discuss every possibilities
if root()<0:
    print("There is no root.")

elif root()>0:
    print("There are 2 real roots,","they are the",quadratic1(),"and",quadratic2())

else:
    print("There is only 1 real root, it is",quadratic1())

quit()

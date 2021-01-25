from sympy import *
#Question1
#for what value of k is the following function continous at given point
#f(x)={k*x+1 : x<=5}
#f(x)={3*x-5 : x>5}
x=symbols('x')
k=symbols('k')
init_printing(use_unicode=True)
def f(a):
    if(a<=5):
        return k*x+1
    elif(a>5):
        return 3*x-5
#solution
# Being polynomial function the function will be continous at all points except for 5 where we have to check. 
#here we will find the left and right hand limits at 5
delta=0.000001
LHL=limit(f(5-delta),x,5,'-')
RHL=limit(f(5+delta),x,5,'+')
eq1=Eq(LHL,RHL)
q=solve((eq1),k)
print(f"therefore the vlue of k at which the function is continous at 5 is: {q[0]}")

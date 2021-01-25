from sympy import *
#Question2
#
#f(x)={x-1 : x>=1}
#f(x)={-x+1 : x<1}
x=symbols('x')
init_printing(use_unicode=True)
def f(a):
    if(a<1):
       return -a+1
    else:
        return a-1
#solution
#here we will check wheather the function is continous or not for that we will check left hand and right hand limit of function at 1
delta=0.000001
LHL=round(limit(f(1-delta),x,1,'-'))
RHL=round(limit(f(1+delta),x,1,'+'))
if(LHL==RHL):
    #function is continous and we will check for defferentiablity that is left hand and right hand derivative
    LHD=round(limit((f(1-delta)-f(1))/(-1*delta),x,1,'-'))
    RHD=round(limit((f(1+delta)-f(1))/delta,x,1,'+'))
    if(LHD==RHD):
        print("the function is differentiable at x=1")
    else:
        print("the function is continous but  not differentiable at x=1")

else:
    print("the function is not differentiable at x=1")

from sympy import *
#Question2
#
#f(x)={0 : 0<x<1}
#f(x)={1 : 1<=x<2}
#f(x)={2 : 2<=x<3
x=symbols('x')
init_printing(use_unicode=True)
def f(a):
    if(0<a<1):
       return 0
    elif(1<=a<2):
        return 1
    elif(2<=a<3):
        return 2
#solution
#for x=1
#here we will first check continuty for that we will check left hand limit and right hand limit  of function at x=1
delta=0.000001
LHL=limit(f(1-delta),x,1,'-')
RHL=limit(f(1+delta),x,1,'+')
if(LHL==RHL):
    #function is continous and we will check for defferentiablity that is left hand and right hand derivative
    LHD=limit((f(1-delta)-f(1))/(-1*delta),x,1,'-')
    RHD=limit((f(1+delta)-f(1))/delta,x,1,'+')
    if(LHD==RHD):
        print("the function is differentiable at x=1")
    else:
        print("the function is continous but not differentiable at x=1")

else:
    print("the function is not differentiable at x=1")
#for x=2
#here we will first check continuty for that we will check left hand limit and right hand limit  of function at x=2
delta=0.000001
LHL=limit(f(2-delta),x,2,'-')
RHL=limit(f(2+delta),x,2,'+')
if(LHL==RHL):
    #function is continous and we will check for defferentiablity that is left hand and right hand derivative
    LHD=limit((f(2-D)-f(2))/(-1*D),x,2,'-')
    RHD=limit((f(2+D)-f(2))/D,x,2,'+')
    if(LHD==RHD):
        print("the function is differentiable at x=2")
    else:
        print("the function is continous but not differentiable at x=2")

else:
    print("the function is not differentiable at x=2")

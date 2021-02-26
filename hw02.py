#HW 2

_author_ = "Avery Brinkman"
_credits_ = [""]
_email_ = "brinkmae@mail.uc.edu"

from math import sin, cos



def approx_fixed_point(f,x):
    if abs(f(x) - x) < 1e-15:
        return True
    else:
        return False 

def fixed_point_iteration(f, x=1.0):
    step = 0
    while not approx_fixed_point(f,x):
        x = f(x)
        step += 1
    return x, step 



def approx_newton_zero(f, df, x):
    return (x - f(x) / df(x))

def newton_find_zero(f, df,x):
    step = 0
    while not abs(f(x)) < 1.0e-15:
        x = approx_newton_zero(f,df,x)
        step += 1
    return x, step



assert fixed_point_iteration(lambda x: sin(x) + x, 3.0)==(3.141592653589793, 3), "\n\nfp pi is wrong\ngot:" + str(fixed_point_iteration(lambda x: sin(x) + x, 3.0))+"\n"
assert fixed_point_iteration(lambda x: cos(x), 1.0)==(0.7390851332151611, 86), "\n\nfp dot wrong\ngot:" + str(fixed_point_iteration(lambda x: cos(x), 1.0)) + "\n"
assert newton_find_zero(lambda x: sin(x) , lambda x: cos(x), 3.0)==(3.141592653589793, 3), "\n\nnewt pi wrong\ngot:"+str(newton_find_zero(lambda x: sin(x) , lambda x: cos(x), 3.0))+"\n"
assert newton_find_zero(lambda x: cos(x) - x , lambda x: -sin(x)-1, 1.0)==(0.7390851332151607, 4), "\n\nnewt dot wrong\ngot:" + str(newton_find_zero(lambda x: cos(x) - x , lambda x: -sin(x)-1, 1.0)) + "\n"



# By using the fixed_point_iteration method to find pi accurate to 15 digits, it only takes 3 iterations.
# Using newton_find_zero method to find pi accurate to 15 digits, it also only takes 3 iterations.
#   Therefore, they are equally effective
# On the other hand, the newton method is far more efficient in finding the dottie number as it only 
#   takes 4 iterations to get to sthe same number that the fixed point method gets to in 86 iterations.
#   This means that it takes the fixed point method 182.22% more iterations.

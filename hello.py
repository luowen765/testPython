'''
@Descripttion:
@version:
@Author: luowen
@Date: 2020-07-23 22:29:54
@LastEditTime: 2020-07-24 21:46:29
@FilePath: /python/testPython/hello.py
'''


""" # example square root
# real numbers
import cmath
numb = float(input("input a real number: "))
num_sqrt = numb ** 0.5
print('square root of  %0.2f is %.2f' % (numb, num_sqrt))
# complex numbers or negative number
numb2 = int(input("input a complex number: "))
num_sqrt2 = cmath.sqrt(numb2)
print('square of {0} is {1:0.2f}+{2:0.2f}'.format(numb2,
                                                  num_sqrt2.real, num_sqrt2.imag))

 """


""" # example sum
# format
numb1 = input("input first：")
numb2 = input("input second: ")
sum = float(numb1) + float(numb2)  # input return a string!
print('first value {0} + second value {1} = {2:.3f}'.format(numb1, numb2, sum))

# %
print('sum of two values is %.3f' %
      (float(input("input first: "))+float(input("input second: ")))) """

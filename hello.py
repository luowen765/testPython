'''
@Descripttion: 
@version: 
@Author: luowen
@Date: 2020-07-25 10:32:48
@LastEditTime: 2020-07-27 14:55:11
'''

with open(r"oblivious words for IELTS.txt") as f:
    print(len(f.readlines()))
""" with open("out.txt","w") as f1:
      with open("oblivious words for IELTS.txt") as f2:
             for count, line in enumerate(f2):
                   count += 1
                    print(count) """
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

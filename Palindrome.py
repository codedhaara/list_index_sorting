
"""
import time
str = input("enter the string:")
l = len(str)
for i in range(l):
  if str[i]!=str[l-1-i]:
   print("it is not a palindrome")
   break
  if (i==(l-1)/2 or i==(l-3)/2):
   print("it is a palindrome")
   print(f'number of iterrations is: {i+1}')
   break

"""

import time
str = input("enter the string:")
l = len(str)
for i in range(l):
  if str[i]!=str[l-1-i]:
   print("it is not a palindrome")
   break
  if (i==((l-1)/2) or i==(l/2-1)):
   print("it is a palindrome")
   print(f'number of iterrations is: {i+1}')
   break




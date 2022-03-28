# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?
import time
start = time.time()

def deconstruct(num): #turns number into a list of its digits
    digits = [int(k) for k in str(num)]
    return digits

def convert(list): #turns digit list into a number
    num = sum(digit * pow(10,i) for i, digit in enumerate(list[::-1]))
    return num
def palindrome_check(num):
    if str(num)[::] == str(num)[::-1]:
        return True
    else:
        return False

not_lychrel = []

def lychrel_check(num):
    iterations = 0
    while iterations < 50:
        reverse_num = convert(deconstruct(num)[::-1])
        if palindrome_check(num + reverse_num) is True:
            not_lychrel.append(num)
            break
        else:
            num += reverse_num
            iterations += 1

for k in range(1,10001):
    lychrel_check(k)

print(10000 - len(not_lychrel))

stop = time.time()
print(stop-start, "seconds")
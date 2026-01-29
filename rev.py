
''' write a program to find the reverse of number '''

def reverse(num):
    rev=0
    while num>0:
     rev= rev*10+num%10
     num//=10
     return rev

def isPalindrome(num):
    return num==reverse(num)


<<<<<<< HEAD
print(reverse(1236))
=======
print(reverse(1239))
>>>>>>> 2c1afe4aaf858e873692a3a647ba1c809618ebf7
print(isPalindrome(123))

print(reverse(121))
print(isPalindrome(121))

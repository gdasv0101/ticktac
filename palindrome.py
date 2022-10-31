#this is a python program to check whether the given string is a palindrome or not.


def isPalindrome(s):
	return s == s[::-1]


# Driver code
n=input("Enter string :  ")#declaring
ans = isPalindrome(n)
print("computing result")

if ans:
	print("Yes,the given string is paliendrome") #if_condition_true
else:
	print("No,the given string is not paliendrome )#false 
#EOF

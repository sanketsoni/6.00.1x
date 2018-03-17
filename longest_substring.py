"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
"""

s = 'abcabc'
maxlength = 0
string1 = s[0]
string2 = s[0]

for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        string1 += s[i+1]
        if len(string1) > maxlength:
            string2 = string1
            maxlength = len(string1)

    else:
        string1 = s[i+1]
    i += 1
print("Longest substring in alphabetical order is:{}".format(string2))

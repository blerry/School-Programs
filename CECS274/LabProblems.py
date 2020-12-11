a = [ 1, 2, 3, 4, 5]
#reverse this array

def reverse_array(array):
    for i in range(len(array)//2):
        a = array[i]
        array[i] = array[len(array) -i -1]
        array[len(array) -i -1] = a

#reverse_array(a)
#print(a)

#PROBLEM 3
#function Anagram that takes 2 strings and returns true is s1 and s2 are anagra
    #we sort
def isAnagram(s1, s2):
    if(sorted(s1) == sorted(s2)):
        print("Both strings form a Anogram")
    else:
        print("Both strings do not form a Anogram")

s1 = "EARTH"
s2 = "HEART"
#isAnagram(s1, s2)

#PROBLEM 4
#Two Sum, return true if 2 numbers add up to target

def twoSum(list):
    for num in list:
            diff = target - num
            if diff in seen: return True
            else:
                seen.append(num)
            return False

seen ={} #Hash Set
target = 9
a = [2, 11, 7, 3 ,15]

#PROBLEM 5
#Palindrome: reads same forward and backward
#Given a lowercase string, function that returns true if string
#is Palindrome. Ignore spaces.

def isPalindrome(s):
    reverse == s[::-1] #reverse string returns

    if(reverse == s):
        return True
    else:
        return False
reverse = ""    
input = "race car"
#isPalindrome(input)


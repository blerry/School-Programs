# function name: shift_cipher_encode
# inputs: string - string to encode (str)
		# n - amount to shfit by (int)
# output: the encoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
			#  Should be able to accommodate upper and lower case letters
# restrictions:  DO NOT USE A DICTIONARY TO ENCODE YOUR LETTERS
def shift_cipher_encode(string, n):
    string2 = ""
    for letter in string:
        if letter == " " or letter.isalpha() == False:
            string2 += letter
        elif letter.isalpha() == True:
            if letter.islower() == True:
                letter = ord(letter) + n
                if letter > 122:
                    #letter = number - max mod number
                    diff = letter - (122 % letter)
                    letter = 96 + diff
                    string2 += chr(letter)
                else:
                    string2 += chr(letter)
            
            elif letter.isupper() == True:
                letter = ord(letter) + n
                if letter > 90:
                    diff = letter - (90 % letter)
                    letter = 64 + diff
                    string2 += chr(letter)
                else:
                    string2 += chr(letter)
    return string2
        

# function name: shift_cipher_decode
# inputs: string - string to encode (str)
		# n - amount to shfit by (int)
# output: the decoded string
# assumptions: There can be non-alphabet characters. You must leave these alone
			#  Should be able to accommodate upper and lower case letters
# restrictions:  DO NOT USE A DICTIONARY TO ENCODE YOUR LETTERS

#ASCII A = 65, Z = 90 a = 97, z = 122
# add 65 to shift number and subtract that by the current letter then mod and shift that number
def shift_cipher_decode(string, n):
    string2 = ""
    for letter in string:
        if letter == " " or letter.isalpha() == False:
            string2 += letter
        elif letter.isalpha() == True:
            if letter.islower() == True:
                shift = 97 + n
                letter = ord(letter) - shift
                if letter < 0:
                    letter = (letter + 123) % 122
                    string2 += chr(letter)
                elif letter >=0:
                    letter = (letter + 97) % 122
                    string2 += chr(letter)
            elif letter.isupper() == True:
                shift = 65 + n
                letter = ord(letter) - shift
                if letter < 0:
                    letter = (letter + 91) % 90
                    string2 += chr(letter)
                elif letter >=0:
                    letter = (letter + 65) % 90
                    string2 += chr(letter)
            
    return string2


# test cases
# These MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
'''
# Wmfauw ak yjwsl! :)
print(shift_cipher_encode("Eunice is great! :)", 18)) 
# Qobkbny sc qbokd dyy!!!
print(shift_cipher_encode("Gerardo is great too!!!", 10)) 
# Gjwsfwit nx fqxt lwjfy! :I
print(shift_cipher_encode("Bernardo is also great! :D", 5)) 
# WYWM229 cm nby vymn wfumm un WMOFV
print(shift_cipher_encode("CECS229 is the best class at CSULB", 20))

# This is the 2nd lab.
print(shift_cipher_decode("Qefp fp qeb 2ka ixy.", 23))
# ThErE r m@ny m0rE Labs 2 come!
print(shift_cipher_decode("KyViV i d@ep d0iV Crsj 2 tfdv!", 17))
# s0 B prepared!
print(shift_cipher_decode("y0 H vxkvgxkj!", 6))
# pineapples
print(shift_cipher_decode("buzqmbbxqe", 12))
'''


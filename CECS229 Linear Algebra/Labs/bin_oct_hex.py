# funtion name: to_decimal
# input: num (a non-negative non-decimal int as string)- ex: 11101, 7712, ABC
		#base (the number system you're converting from as an int)- ex: 2, 8, 16
# output: decimal representation of num AS INTEGER 
# restrictions: you are NOT allowed to use the Python int function
				# that will convert it to decimal for you. You should use
				# implement the algorithm discussed in class
# assumptions: num will always be non-negative
			#  num will always be a valid number ex: 31112 (base2) won't be an input
			#. if num has letters, they will always be captialized
			#  base will be 2, 8, or 16
def to_decimal(num, base):
#hexi = 16 octal = 8 binary = 2
    answer = 0
    length = (len(num) -1 )
    if base == 2:
        for binary in num:
            if binary == '1':
                answer += 1 * pow(base, length)
                length = length - 1
            elif binary == '0':
                answer += 0 * pow(base, 0)
                length = length - 1
        return answer 
    elif base == 8:
        while((length+1) %3 != 0):
           num =  '0' + num
           length = length + 1
        for octal in num:
            answer += int(octal) * pow(base, length)
            length = length - 1
        return answer     
    elif base == 16:
        while((length +1) %4 != 0):
            num =  '0' + num
            length = length + 1
            for hexi in num:
                if hexi == 'A':
                    hexi =  '10'
                elif hexi == 'B':
                    hexi = '11'
                elif hexi == 'C':
                    hexi = '12'
                elif hexi == 'D':
                    hexi = '13'
                elif hexi == 'E':
                    hexi = '14'
                elif hexi == 'F':
                    hexi = '15'
                
                answer +=  int(hexi) * pow(base, length)
                length = length - 1
        return answer

# funtion name: to_base
# input: dec_num (a positive decimal integer)- ex: 1, 6, 10, 68, 102...
		#base (the number system you're converting from as an int)- ex: 2, 8, 16
# output: non-base-10 representation of dec_num AS STR
# restrictions: you are NOT allowed to use the Python int function
				# that will convert it for you. You should use
				# implement the algorithm discussed in class
# assumptions: dec_num will always be non-negative
			#  base will be 2, 8, or 16				
def to_base(dec_num, base):
    answer = ''
    num = 0
    #divide until number < 1 keep remainders
    if base == 2 or base == 8:
        while (dec_num >= 1):
            num = int(dec_num % base)
            answer += str(num)
            dec_num = dec_num / base
        answer = answer[::-1]
        return answer
    elif base == 16:
        while (dec_num >= 1):
            num = int(dec_num % base)

            if num == 10:
                num = str(num)
                num = 'A'
            elif num == 11:
                num = str(num)
                num = 'B'
            elif num == 12:
                num = str(num)
                num = 'C'
            elif num == 13:
                num = str(num)
                num = 'D'
            elif num == 14:
                num = str(num)
                num = 'E'
            elif num == 15:
                num = str(num)
                num = 'F'
            answer += str(num)

            dec_num = dec_num / base
        answer = answer[::-1]
            
        return answer

# test cases
# These MUST be commented out or deleted in your submission
# otherwise the grading script will pick it up! You WILL lose points!
# please note that these are not the only test cases that will be run
print(to_decimal('101', 2)) # 5
print(to_decimal('1110', 2)) #14
print(to_decimal('642', 8)) #418
print(to_decimal('1342', 8)) #738
print(to_decimal('65', 16)) #101
print(to_decimal('57A', 16)) #1402

print(to_base(123, 2)) # '1111011'
print(to_base(400, 2)) # '110010000'
print(to_base(3424, 8)) # '6540'
print(to_base(5212, 8)) # '12134'
print(to_base(16423, 16)) # '4027'
print(to_base(15967, 16)) # '3E5F'






.data
.text
#1
#addi $s0, $zero, 5 #A
#addi $s1, $zero, 12 #B
#add $s2, $s0, $s1 #C
#2
#addi $s0, $zero, -15 #A
#addi $s1, $zero, -26 #B
#sub $s3, $s0, $s1 #D
#3
#addi $s0, $zero, 10 #A
#addi $s1, $zero, 30 #B
#addi $s2, $zero, 60 #C
#addi $s3, $zero, -75 #D
#addi $s4, $zero, -100 #E
#add $t0, $s0, $s1, #temp A+B
#sub $t1, $s2, $t0, #temp A+B-C
#sub $t2, $s4, $s3, #temp D-E
#sub $s5, $t2, $t1 #F = (A+B-C) - ((D-E)
#4
#addi $s0, $zero, 10 #A
#addi $s1, $zero, 30 #B
#addi $s2, $zero, 60 #C
#addi $s3, $zero, -75 #D
#addi $s4, $zero, -100 #E
#add $t0, $s0, $s1, #temp A+B
#sub $t1, $s2, $t0, #temp A+B-C
#sub $t2, $s4, $s3, #temp D-E
#sub $s5, $t2, $t1 #F = (A+B-C) - ((D-E)
#sub $t3, $s5, $s0 #F - A
#add $s5, $s1 ,$t3 #F = F-A +B
#5
addi $s0, $zero, 0x89ab, #A
addi $s1, $zero, 0x98b3, #B
add $s6, $s0, $s1, #G
#6
#addi $s1, $zero, 0x0d, #B
#addi $s0, $zero, 4, #temp
#addi $s7, $zero, 1, #H
#mul $s7, $s0, $s1 #H
#7
#addi $s0, $zero, 10, #A
#sub $s0, $s0, 0x1c #A = A- 0x1c

#8
#addi $s2, $zero, 20 #B
#addi $s5, $zero, 50 #E
#addi $s6, $zero, 35 #F
#addi $s7, $zero, 120 #G
#sub $t0, $s7, $s5 #temp G-E
#addi $t0, $t0, 100 #temp (G-E) + 100
#sub $t1, $s6, $s2 #temp F - B
#subi $t1, $t1,45  #temp (F-B)-45
#sub $s3, $t0, $t1 #D = [(G-E) + 100] - [(F - B) - 45]
#9
#addi $s3, $zero, 456, #D
#addi $s4, $zero, 123, #F
#addi $s5, $zero, 0x44, #G
#sub $t0, $s3, 0x44, #temp D-G
#add $s0, $t0, $s4 #A = F+(D-G)
#10
#A=3; B=50; F=0; for (H=0; H! = B; H++) F = F + A.
#addi $s0, $zero, 3 #A
#addi $s1, $zero, 50 #B
#addi $s6, $zero, 0 #F
#addi $s7, $zero, 0 #H
#LOOP: 
	#beq $t0,$s1, DONE #H $t0
	#add $s6, $s6, $s0,
	#add $t0, $t0, 1,
	#j LOOP
DONE:
syscall

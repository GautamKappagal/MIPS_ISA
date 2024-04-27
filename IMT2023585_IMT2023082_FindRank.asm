.data
	next_line: .asciiz "\n"
	n: .asciiz "\nEnter the number of integers in your array: "
	in_address: .asciiz "Enter the starting address where you want to store the input array: "
	out_address: .asciiz "Enter the starting address where you want to store the output array: "
	rank_address: .asciiz "Enter the address where you want to store the rank: "
	integers: .asciiz "Enter the integers in your array:\n"
	rank: "Enter the number whose rank you want to find: "
	print_rank: "\nRank: "
	no_rank: "\nNumber not found in the array!"
	sorted_array: "\nSorted array:\n"

.text
	#Inputting: Lines 7 - 34

	#Input number of integers - n
	jal enter_n
	jal input_int
	move $s1, $t4

	#Input starting address of input numbers
	jal enter_in_address
	jal input_int
	move $s2, $t4

	#Input starting address of output numbers
	jal enter_out_address
	jal input_int
	move $s3, $t4

	#Input numbers
	move $t1, $s2
	move $t2, $zero #iterator t2
	jal enter_integers

	inputLoop: 
	    beq $t2, $s1, exitInput
	    jal input_int
	    sw $t4, 0($t1)
	    addi $t1, $t1, 4
	    addi $t2, $t2, 1
	    j inputLoop

	exitInput:

	#Input address of output rank
	jal enter_rank_address
	jal input_int
	move $s4, $t4

	#Input number whose rank needs to be found
	jal enter_rank
	jal input_int
	move $s5, $t4

	#Copying: Lines 38 - 55

	move $t0, $zero # Iterator i = 0
	move $t1, $s2 # Temporarily storing the starting input address
	move $t2, $s3 # Temporarily storing the starting output address

	copyLoop:
	    beq $t0, $s1, exitCopy
    
	    #Copying each number from the input address to the output address
	    lw $t3, 0($t1)
	    sw $t3, 0($t2)

	    #Now incrementing the addresses and the iterator
	    addi $t1, $t1, 4
	    addi $t2, $t2, 4
	    addi $t0, $t0, 1
	    j copyLoop

	exitCopy:

	#Bubble Sorting: Lines 59 - 90

	move $t0, $zero #Outer iterator i = 0
	addi $t2, $s1, -1 #t2 = n - 1

	outerLoop:
	    beq $t0, $t2, exitOuterLoop
	    move $t1, $zero     # Inner iterator j = 0
	    addi $t4, $t0, 1    # t4 = i + 1
	    sub $t5, $s1, $t4   # t5 = n - i - 1
	    move $t6, $s3       # Temporarily storing the output starting address

	    innerLoop:
	        beq $t1, $t5, exitInnerLoop
	        addi $t7, $t6, 4   # t7 = t6 + 4, storing the next memory location temporarily
        	lw $t8, 0($t6)     # t8 = M[t6 + 0]
	        lw $t9, 0($t7)     # t9 = M[t7 + 0]
	        slt $t3, $t8, $t9  # If t8 < t9, t3 = 1, else, t3 = 0
        	beq $t3, $zero, swap

	        remSort:
        	    addi $t6, $t6, 4
        	    addi $t1, $t1, 1
	            j innerLoop

        	swap: #Swaps t8 and t9
	            sw $t9, 0($t6)
        	    sw $t8, 0($t7)
	            j remSort

	    exitInnerLoop:
        	addi $t0, $t0, 1    # i++
	        j outerLoop

	exitOuterLoop:

	move $t7, $zero	# i = 0
	move $t8, $s3	# Temporarily storing the starting address of the sorted array
	jal print_sorted

	printSortedLoop:
		beq $t7, $s1, exitPrintSort
    	lw $t4, 0($t8)
      	jal print_int
      	jal print_line
      	addi $t8, $t8, 4
      	addi $t7, $t7, 1
      	j printSortedLoop
	
	exitPrintSort:

	#Finding rank

	move $t0, $s1 		# t0 = n + 1
	move $t1, $zero 	# Iterator i = 0
	move $t4, $s3 		# Temporarily storing the output starting address

	rankLoop:
		beq $t1, $s1, exitRank
		lw $t3, 0($t4)	# t3 = M[s3 + 0] = sortedArr[0]
		beq $t3, $s5, returnRank

		remRank:
			addi $t4, $t4, 4
        	addi $t1, $t1, 1
			j rankLoop

		returnRank:
			sub $t6, $t0, $t1 	# t6 = n + 1 - i
			sw $t6, 0($s4)
			lw $t4, 0($s4)
			jal display_rank
			jal print_int
			jal print_line
			j finish
		
		exitRank:
			addi $t5, $zero, -1
			sw $t5, 0($s4)
			lw $t4, 0($s4)
			jal print_no_rank
			jal print_line
		
		finish:

	#Printing: Lines 94 - 106

	move $t0, $zero     #Iterator i = 0
	printRankLoop:
	    beq $t0, $s1, exitPrint
	    lw $t4, 0($s3)
	    addi $t0, $t0, 1
	    addi $s3, $s3, 4
	    j printRankLoop

	exitPrint:
	    li $v0, 10
	    syscall

	#Input Procedure: Lines 110 - 115

	#Inputs integers into $t4
	input_int:
	    li $v0, 5
	    syscall
	    move $t4, $v0
	    jr $ra

	#Output Procedure: Lines 118 - 131

	#Prints integer from t4
	print_int:
		li $v0, 1
		move $a0, $t4
		syscall
		jr $ra

	#Prints newline '\n'
	print_line:
	    li $v0, 11
		la $a0, 10
		syscall
		jr $ra

	enter_n:
	    li $v0, 4
		la $a0, n
		syscall
		jr $ra

	enter_in_address:
	    li $v0, 4
		la $a0, in_address
		syscall
		jr $ra

	enter_out_address:
	    li $v0, 4
		la $a0, out_address
		syscall
		jr $ra

	enter_rank_address:
	    li $v0, 4
		la $a0, rank_address
		syscall
		jr $ra

	enter_integers:
	    li $v0, 4
		la $a0, integers
		syscall
		jr $ra

	enter_rank:
	    li $v0, 4
		la $a0, rank
		syscall
		jr $ra
	
	display_rank:
	    li $v0, 4
		la $a0, print_rank
		syscall
		jr $ra
	
	print_no_rank:
	    li $v0, 4
		la $a0, no_rank
		syscall
		jr $ra

	print_sorted:
	    li $v0, 4
		la $a0, sorted_array
		syscall
		jr $ra

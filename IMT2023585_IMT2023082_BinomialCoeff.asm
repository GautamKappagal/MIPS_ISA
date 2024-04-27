.data
    next_line: .asciiz "\n"
    n_input: .asciiz "Enter n: "
    n_address: .asciiz "Enter the address where you want to store n: "
    out_address: .asciiz "Enter the starting address where you want to store the coefficients: "
    fact_output: .asciiz "\nBinomial expansion of (1 + x)^"
    x: .asciiz "x^"
    plus: .asciiz " + "

.text
    
    # Inputting address of n
    jal enter_n_address
    jal input_int
    move $s0, $t4

    # Inputting n
    jal enter_n
    jal input_int
    move $s1, $t4
    sw $t4, 0($s0)  # Storing n in the address for n

    # Inputting starting address of output
    jal enter_out_address
    jal input_int
    move $s4, $t4
    move $t9, $s4           # Storing s4 into t9 for printing later

    move $t1, $s1           # t1 = n
    addi $t1, $t1, 1        # t1 = n + 1
    addi $t0, $zero, 1      # Iterator t0 = 1
    addi $s6, $zero, 1      # s6 = 1, this is where we store n!

    factN:
        beq $t0, $t1, exitN
        mul $s6, $s6, $t0
        addi $t0, $t0, 1
        j factN

    exitN:                  # s6 now holds n!

    move $t6, $zero         # Iterator j = 0
    addi $t7, $s1, 1        # t7 = n + 1


    outerLoop:
        beq $t6, $t7, exitOuterLoop
        
        nCj:
            move $s5, $zero         # Loop counter
            addi $t5, $zero, 1      # Constant t5 = 1 (for counter)
            j check

        check:
            beq $s5, $zero, secondLoop
            beq $s5, $t5, thirdLoop
            j exit

         secondLoop:
            addi $t0, $zero, 1      # Iterator i = 1
            addi $t1, $t6, 1        # t1 = j + 1
            addi $t4, $zero, 1      # t4 = 1, j! is stored here
            addi $s5, $s5, 1        # Increment loop counter by 1
            j fact

         thirdLoop:
            move $s7, $t4           # Moving j! into s7
            addi $t0, $zero, 1      # Iterator i = 1
            sub $t1, $s1, $t6       # t1 = n - j
            addi $t1, $t1, 1        # t1 = n - j + 1
            addi $t4, $zero, 1      # t4 = 1, (n - j)! is stored here
            addi $s5, $s5, 1        # Increment loop counter by 1
            j fact

        fact:
            beq $t0, $t1, check     # Check i == j + 1 or i == (n - j + 1)
            mul $t4, $t4, $t0
            addi $t0, $t0, 1
            j fact

    exit:
        move $s2, $t4           # Moving (n - j)! into s2
        move $s5, $zero         # Reset loop counter to 0

    mul $t8, $s7, $s2           # t8 = (j!)*(n - j)!
    div $s6, $t8                # lo = nCk
    mflo $t4
    sw $t4, 0($s4)              # Storing nCj in s4[0]
    addi $s4, $s4, 4            # Increment s4 by 4
    addi $t6, $t6, 1            # Increment j by 1
    j outerLoop

    exitOuterLoop:

    move $t1, $s1           # t1 = n
    addi $t1, $t1, 1        # t1 = n + 1
    move $t0, $zero         # Iterator t0
    addi $s6, $zero, 1      # s6 = 1, this is where we store n!

    jal print_fact
    move $t4, $s1             # Moving n into t4 for printing
    jal print_int
    jal print_colon
    jal print_space

    printLoop:
        beq $t0, $t1, exitPrint
        lw $t4, 0($t9)
        jal print_int
        jal print_x
        move $t4, $t0
        jal print_int
        bne $t0, $s1, printPlus

    remPrint:
        addi $t9, $t9, 4
        addi $t0, $t0, 1
        lw $t4, 0($t9)
        j printLoop
    
    printPlus:
        jal print_plus
        j remPrint

    exitPrint:

    input_int:
    	li $v0, 5
    	syscall
    	move $t4, $v0
    	jr $ra

    #Prints newline '\n'
    print_line:
    	li $v0, 11
    	la $a0, 10
    	syscall
    	jr $ra

    # Prints space
    print_plus:
    	li $v0, 4
	la $a0, plus
    	syscall
    	jr $ra  

    #Prints integer from t4
	print_int:
		li $v0, 1
		move $a0, $t4
		syscall
		jr $ra

    enter_n_address:
    	    li $v0, 4
    		la $a0, n_address
    		syscall
    		jr $ra  

    enter_out_address:
    	    li $v0, 4
    		la $a0, out_address
    		syscall
    		jr $ra 

    enter_n:
    	    li $v0, 4
    		la $a0, n_input
    		syscall
    		jr $ra

    print_fact:
    	    li $v0, 4
    		la $a0, fact_output
    		syscall
    		jr $ra

    print_colon:
    	li $v0, 11
    	la $a0, 58
    	syscall
    	jr $ra

    print_space:
    	li $v0, 11
    	la $a0, 32
    	syscall
    	jr $ra

    print_x:
    	li $v0, 4
    	la $a0, x
		syscall
		jr $ra

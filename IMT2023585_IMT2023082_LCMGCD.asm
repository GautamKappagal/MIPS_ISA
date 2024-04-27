.data
    next_line: .asciiz "\n"
    num1_address: .asciiz "Enter the address where you want to store the first number: "
    num2_address: .asciiz "Enter the address where you want to store the second number: "
    lcm_address: .asciiz "Enter the address where you want to store the LCM: "
    gcd_address: .asciiz "Enter the address where you want to store the GCD: "
    num1_input: "Enter the first number: "
    num2_input: "Enter the second number: "
    gcd_print: "\nGCD: "
    lcm_print: "LCM: "

.text
    #Inputting:

    #Inputting address of num1
    jal enter_num1_address
    jal input_int
    move $s0, $t4
    
    #Input num1
    jal enter_num1
    jal input_int
    move $s4, $t4
    sw $t4, 0($s0)  # Storing num1 in the address for num1

    #Inputting address of num2
    jal enter_num2_address
    jal input_int
    move $s1, $t4

    #Input num2
    jal enter_num2
    jal input_int
    move $s5, $t4
    sw $t4, 0($s1)  # Storing num2 in the address for num2


    #Inputting GCD address
    jal enter_gcd_address
    jal input_int
    move $s2, $t4
    
    #Inputting LCM address
    jal enter_lcm_address
    jal input_int
    move $s3, $t4

    move $t2, $s4   # Temporarily storing num1 in t2
    move $t6, $s5   # Temporarily storing num2 in t6

    gcd:
        beq $t6, $zero, exitGCD
        div $t2, $t6   # t4 = a % b
        mflo $t3
        mul $t9, $t6, $t3
        sub $t4, $t2, $t9
        move $t5, $t6       # t5 = b
        move $t6, $t4       # b = a % b
        move $t2, $t5
        j gcd

    exitGCD:
        sw $t2, 0($s2)  # Storing GCD in s2
        lw $t4, 0($s2)  # Loading GCD into t4 for printing
        jal print_gcd
        jal print_int
        jal print_line

    # Calculating LCM using GCD

    move $t7, $s4   # Temporarily storing num1 in t7
    move $t8, $s5   # Temporarily storing num2 in t8

    lw $t2, 0($s2)      # Temporarily loading GCD into t2
    mul $t0, $t7, $t8  # t0 = a*b
    div $t0, $t2
    mflo $t1      # t1 = a*b/GCD = LCM
    sw $t1, 0($s3)      # Storing LCM in the required address
    lw $t4, 0($s3)      # Loading LCM into t4 for printing
    jal print_lcm
    jal print_int
    jal print_line

    #Inputs integers into $t4
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

    #Prints integer from t4
	print_int:
		li $v0, 1
		move $a0, $t4
		syscall
		jr $ra

    enter_num1_address:
    	li $v0, 4
    	la $a0, num1_address
    	syscall
    	jr $ra

    enter_num2_address:
    	li $v0, 4
    	la $a0, num2_address
    	syscall
    	jr $ra      

    enter_gcd_address:
        li $v0, 4
    	la $a0, gcd_address
    	syscall
    	jr $ra

    enter_lcm_address:
	    li $v0, 4
		la $a0, lcm_address
		syscall
		jr $ra

    enter_num1:
    	li $v0, 4
    	la $a0, num1_input
    	syscall
    	jr $ra
    
    enter_num2:
        li $v0, 4
    	la $a0, num2_input
    	syscall
    	jr $ra

    print_gcd:
	    li $v0, 4
		la $a0, gcd_print
		syscall
		jr $ra

    print_lcm:
    	li $v0, 4
    	la $a0, lcm_print
    	syscall
    	jr $ra
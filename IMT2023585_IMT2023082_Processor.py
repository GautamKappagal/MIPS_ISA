# Instruction memory for each program
instrMemRank = {
    4194348: "00000000000000000100000000100001",
    4194352: "00000000000100100100100000100001",
    4194356: "00000000000100110101000000100001",
    4194360: "00010001000100010000000000000110",
    4194364: "10001101001010110000000000000000",
    4194368: "10101101010010110000000000000000",
    4194372: "00100001001010010000000000000100",
    4194376: "00100001010010100000000000000100",
    4194380: "00100001000010000000000000000001",
    4194384: "00001000000100000000000000001110", # Changed jump target here
    4194388: "00000000000000000100000000100001",
    4194392: "00100010001010101111111111111111", # Changed -1 to 0 here (back to -1)
    4194396: "00010001000010100000000000010010",
    4194400: "00000000000000000100100000100001",
    4194404: "00100001000011000000000000000001", # Changed 1 to 0 here (back to 1)
    4194408: "00000010001011000110100000100010",
    4194412: "00000000000100110111000000100001",
    4194416: "00010001001011010000000000001011", # Changed beq imm value (beq $t1, $t5, 11)
    4194420: "00100001110011110000000000000100",
    4194424: "10001101110110000000000000000000", # Make changes
    4194428: "10001101110110010000000000000100", # Make changes
    4194432: "00000011000110010101100000101010",
    4194436: "00010001011000000000000000000011",
    4194440: "00100001110011100000000000000100",
    4194444: "00100001001010010000000000000001",
    4194448: "00001000000100000000000000011100", # Changed jump target here (j innerLoop)
    4194452: "10101101110110010000000000000000",
    4194456: "10101101111110000000000000000000",
    4194460: "00001000000100000000000000100010", # Changed jump target here (j remSort)
    4194464: "00100001000010000000000000000001",
    4194468: "00001000000100000000000000010111", # Changed jump target here (j outerLoop)
    4194472: "00000000000100010100000000100001",
    4194476: "00000000000000000100100000100001",
    4194480: "00000000000100110110000000100001",
    4194484: "00010001001100010000000000001100",
    4194488: "10001101100010110000000000000000",
    4194492: "00010001011101010000000000000011",
    4194496: "00100001100011000000000000000100",
    4194500: "00100001001010010000000000000001",
    4194504: "00001000000100000000000000101101",
    4194508: "00000001000010010111000000100010",
    4194512: "10101110100011100000000000000000"
}

instrMemLG = {
    4194348: "00000000000101000101000000100001",
    4194352: "00000000000101010111000000100001",
    4194356: "00010001110000000000000000001000",
    4194360: "00000001010011100000000000011010",
    4194364: "00000000000000000101100000010010",
    4194368: "01110001110010111100100000000010",
    4194372: "00000001010110010110000000100010",
    4194376: "00000000000011100110100000100001",
    4194380: "00000000000011000111000000100001",
    4194384: "00000000000011010101000000100001",
    4194388: "00001000000100000000000000001101",
    4194392: "10101110010010100000000000000000",
    4194396: "10001110010011000000000000000000",
    4194400: "00000000000101000111100000100001",
    4194404: "00000000000101011100000000100001",
    4194408: "10001110010010100000000000000000",
    4194412: "01110001111110000100000000000010",
    4194416: "00000001000010100000000000011010",
    4194420: "00000000000000000100100000010010",
    4194424: "10101110011010010000000000000000"
}

instrMemBinomial = {
    4194348: "00000000000100010100100000100001",
    4194352: "00100001001010010000000000000001",
    4194356: "00100000000010000000000000000001",
    4194360: "00100000000101100000000000000001",
    4194364: "00010001000010010000000000000011",
    4194368: "01110010110010001011000000000010",
    4194372: "00100001000010000000000000000001",
    4194376: "00001000000100000000000000001111", # Changed j-address for j factN
    4194380: "00000000000000000111000000100001",
    4194384: "00100010001011110000000000000001",
    4194388: "00010001110011110000000000011111",
    4194392: "00000000000000001010100000100001",
    4194396: "00100000000011010000000000000001",
    4194400: "00001000000100000000000000011001", # Changed j-address for j check
    4194404: "00010010101000000000000000000010",
    4194408: "00010010101011010000000000000110",
    4194412: "00001000000100000000000000101100", # Changed j-address for j exit
    4194416: "00100000000010000000000000000001",
    4194420: "00100001110010010000000000000001",
    4194424: "00100000000011000000000000000001",
    4194428: "00100010101101010000000000000001",
    4194432: "00001000000100000000000000101000", # Changed j-address for j fact
    4194436: "00000000000011001011100000100001",
    4194440: "00100000000010000000000000000001",
    4194444: "00000010001011100100100000100010",
    4194448: "00100001001010010000000000000001",
    4194452: "00100000000011000000000000000001",
    4194456: "00100010101101010000000000000001",
    4194460: "00001000000100000000000000101000", # Changed j-address for j fact
    4194464: "00010001000010011111111111110000",
    4194468: "01110001100010000110000000000010",
    4194472: "00100001000010000000000000000001",
    4194476: "00001000000100000000000000101000", # Changed j-address for j fact
    4194480: "00000000000011001001000000100001",
    4194484: "00000000000000001010100000100001",
    4194488: "01110010111100101100000000000010",
    4194492: "00000010110110000000000000011010",
    4194496: "00000000000000000110000000010010",
    4194500: "10101110100011000000000000000000",
    4194504: "00100010100101000000000000000100",
    4194508: "00100001110011100000000000000001",
    4194512: "00001000000100000000000000010101"
}

# Data memory
dataMem = {
    268500992: 0, 268500996: 0, 268501000: 0, 268501004: 0, 268501008: 0, 268501012: 0, 268501016: 0, 268501020: 0, 268501024: 0, 268501028: 0,268501032: 0, 268501036: 0, 268501040: 0, 268501044: 0, 268501048: 0, 268501052: 0, 268501056: 0, 268501060: 0, 268501064: 0, 268501068: 0,268501072: 0, 268501076: 0, 268501080: 0, 268501084: 0, 268501088: 0, 268501092: 0, 268501096: 0, 268501100: 0, 268501104: 0, 268501108: 0, 268501112: 0, 268501116: 0, 268501120: 0, 268501124: 0, 268501128: 0, 268501132: 0, 268501136: 0, 268501140: 0, 268501144: 0, 268501148: 0, 268501152: 0, 268501156: 0, 268501160: 0, 268501164: 0, 268501168: 0, 268501172: 0, 268501176: 0, 268501180: 0, 268501184: 0, 268501188: 0, 268501192: 0, 268501196: 0, 268501200: 0, 268501204: 0, 268501208: 0, 268501212: 0, 268501216: 0, 268501220: 0, 268501224: 0, 268501228: 0, 268501232: 0, 268501236: 0, 268501240: 0, 268501244: 0, 268501248: 0, 268501252: 0, 268501256: 0, 268501260: 0, 268501264: 0, 268501268: 0, 268501272: 0, 268501276: 0, 268501280: 0, 268501284: 0, 268501288: 0, 268501292: 0, 268501296: 0, 268501300: 0, 268501304: 0, 268501308: 0, 268501312: 0, 268501316: 0, 268501320: 0, 268501324: 0, 268501328: 0, 268501332: 0, 268501336: 0, 268501340: 0, 268501344: 0, 268501348: 0, 268501352: 0, 268501356: 0, 268501360: 0, 268501364: 0, 268501368: 0, 268501372: 0, 268501376: 0, 268501380: 0, 268501384: 0, 268501388: 0, 268501392: 0, 268501396: 0, 268501400: 0, 268501404: 0, 268501408: 0, 268501412: 0, 268501416: 0, 268501420: 0, 268501424: 0, 268501428: 0, 268501432: 0, 268501436: 0, 268501440: 0, 268501444: 0, 268501448: 0, 268501452: 0, 268501456: 0, 268501460: 0, 268501464: 0, 268501468: 0, 268501472: 0, 268501476: 0, 268501480: 0, 268501484: 0, 268501488: 0, 268501492: 0, 268501496: 0, 268501500: 0, 268501504: 0, 268501508: 0, 268501512: 0, 268501516: 0, 268501520: 0, 268501524: 0, 268501528: 0, 268501532: 0, 268501536: 0, 268501540: 0, 268501544: 0, 268501548: 0, 268501552: 0, 268501556: 0, 268501560: 0, 268501564: 0, 268501568: 0, 268501572: 0, 268501576: 0, 268501580: 0, 268501584: 0, 268501588: 0, 268501592: 0, 268501596: 0, 268501600: 0, 268501604: 0, 268501608: 0, 268501612: 0, 268501616: 0, 268501620: 0, 268501624: 0, 268501628: 0, 268501632: 0, 268501636: 0, 268501640: 0, 268501644: 0, 268501648: 0, 268501652: 0, 268501656: 0, 268501660: 0, 268501664: 0, 268501668: 0, 268501672: 0, 268501676: 0, 268501680: 0, 268501684: 0, 268501688: 0, 268501692: 0, 268501696: 0, 268501700: 0, 268501704: 0, 268501708: 0
}

def binToInt (binStr):
    if binStr[0] == '1':
        binStr = ''.join('1' if b == '0' else '0' for b in binStr)
        return -1 * (int(binStr, 2) + 1)
    else :
        return int(binStr, 2)

# Control signals

RegDst = 0
Branch = 0
MemRead = 0
MemtoReg = 0
ALUOp = 00
MemWrite = 0
ALUSrc = 0
RegWrite = 0
Jump = 0
    
# Register numbers

regMap = {
    "zero": 0, "v0": 2, "v1": 3, "a0": 4, "a1": 5, "a2": 6, "a3": 7, "t0": 8, "t1": 9, "t2": 10, "t3": 11, "t4": 12, "t5": 13, "t6": 14, "t7": 15, "s0": 16, "s1": 17, "s2": 18, "s3": 19, "s4": 20, "s5": 21, "s6": 22, "s7": 23, "t8": 24, "t9": 25, "ra": 31
}

reg = [0]*32
PC = 4194348
clk_cycles = 0

def control(opcode):
    global RegDst, Branch, MemRead, MemtoReg, ALUOp, MemWrite, ALUSrc, RegWrite, Jump

    if (opcode == "000000"): # R-Type
        RegDst = 1
        Branch = 0
        MemRead = 0
        MemtoReg = 0
        ALUOp = 10
        MemWrite = 0
        ALUSrc = 0
        RegWrite = 1
        Jump = 0

    elif (opcode == "000010"): # j
        RegDst = 0
        Branch = 0
        MemRead = 0
        MemtoReg = 0
        ALUOp = 00
        MemWrite = 0
        ALUSrc = 0
        RegWrite = 0
        Jump = 1

    elif (opcode == "001000" ): # addi
        RegDst = 0
        Branch = 0
        MemRead = 0
        MemtoReg = 0
        ALUOp = 00
        MemWrite = 0
        ALUSrc = 1
        RegWrite = 1
        Jump = 0

    elif (opcode == "000100"): # beq
        RegDst = 0
        Branch = 1
        MemRead = 0
        MemtoReg = 0
        ALUOp = 1
        MemWrite = 0
        ALUSrc = 0
        RegWrite = 0
        Jump = 0

    elif (opcode == "100011"): # lw
        RegDst = 0
        Branch = 0
        MemRead = 1
        MemtoReg = 1
        ALUOp = 00
        MemWrite = 0
        ALUSrc = 1
        RegWrite = 1
        Jump = 0

    elif (opcode == "101011"): # sw
        RegDst = 0
        Branch = 0
        MemRead = 0
        MemtoReg = 0
        ALUOp = 00
        MemWrite = 1
        ALUSrc = 1
        RegWrite = 0
        Jump = 0

    elif (opcode == "011100"): # mul
        RegDst = 1
        Branch = 0
        MemRead = 0
        MemtoReg = 0
        ALUOp = 10
        MemWrite = 0
        ALUSrc = 0
        RegWrite = 1
        Jump = 0

def ALUControl(ALUOp, func):
    if (ALUOp == 00):   # lw, sw, addi
        return "010"
    
    elif (ALUOp == 1):  # beq
        return "011"
    
    elif (ALUOp == 10): # R-Type
        if (func == "100000" or func == "100001" or func == "010010"):      # add or addu or move or mflo
            return "010"
        
        elif (func == "100010"):    # sub
            return "011"
        
        elif (func == "101010"):    # slt
            return "100"
        
        elif (func == "000010"):    # mul
            return "101"
        
        elif (func == "011010"):    # div
            return "110"
        
def fetch(instrMem):
    # Fetches the instruction from instruction memory and returns it

    global PC 
    global clk_cycles
    clk_cycles += 1
    instr = instrMem[PC]
    PC += 4
    return instr

def decode(instr):
    # Decodes the instructions and returns the opcode, rs, rt, rd, shamt, funct, target, imm

    global clk_cycles
    opcode, rs, rt, rd, shamt, funct, target, imm = "", "", "", "", "", "", "", ""
    opcode = instr[0:6]

    control(opcode)     # The values for control flags are set here.
    clk_cycles += 1
    
    if (opcode == "000000" or opcode == "011100"):    # R-Type
        rs = instr[6:11]
        rt = instr[11:16]
        rd = instr[16:21]
        shamt = instr[21:26]
        funct = instr[26:32]

        if (funct == "011010"):
            rd = "01011"
        
        if (funct == "010010"):
            rs = "00000"
            rt = "01011"

        return (opcode, rs, rt, rd, shamt, funct, target, imm)
    
    elif (opcode == "000010"):  # J-Type
        target = "0000" + instr[6:32] + "00"
        return (opcode, rs, rt, rd, shamt, funct, target, imm)

    else:                       # I-Type
        rs = instr[6:11]
        rt = instr[11:16]
        imm = instr[16:32]
        return (opcode, rs, rt, rd, shamt, funct, target, imm)
    
def execute(rs, rt, imm, funct, target):
    global clk_cycles, PC, ALUSrc, ALUOp, Branch, Jump, RegDst, reg
    clk_cycles += 1
    ALUOutput = 0
    ALUFlag = ALUControl(ALUOp, funct)

    if (Jump == 1):         # J-Type
        PC = int(target, 2)
        return 0
    
    if (ALUSrc == 0):
        if (rt != ""):
            if (funct == "010010"):
                rs = "00000"
                rt = "01011"

            ALUInput2 = reg[int(rt,2)] # R-Type

    else:
        ALUInput2 = binToInt(imm) # I-Type

    ALUInput1 = reg[int(rs, 2)]
    
    if (ALUFlag == "010"):       # add or addu or move or mflo
        ALUOutput = ALUInput1 + ALUInput2

    elif (ALUFlag == "011"):     # sub
        ALUOutput = ALUInput1 - ALUInput2

    elif (ALUFlag == "100"):     # slt
        if(ALUInput1 < ALUInput2):
            ALUOutput = 1

        else:
            ALUOutput = 0
    
    elif (ALUFlag == "101"):     # mul
        ALUOutput = ALUInput1 * ALUInput2

    elif (ALUFlag == "110"):     # div
        rd = "01011"
        ALUOutput = ALUInput1//ALUInput2

    if (ALUOutput == 0 and Branch == 1): # beq
        PC += 4*binToInt(imm)

    return ALUOutput

def memory(ALUOutput, targetReg):
    global clk_cycles, MemRead, MemWrite, MemtoReg, dataMem
    clk_cycles += 1

    if (MemRead == 1):      # lw
        return dataMem[ALUOutput]
    
    elif (MemWrite == 1):   # sw
        dataMem[ALUOutput] = reg[int(targetReg, 2)]

    if (MemtoReg == 0):
        return ALUOutput
    
    elif (MemtoReg == 1):
        return dataMem[ALUOutput]
    
def writeBack(rt, rd, data):
    global clk_cycles, RegWrite, RegDst, reg
    clk_cycles += 1
    
    if (RegWrite == 1):
        if (RegDst == 1):
            reg[int(rd, 2)] = data

        else:
            reg[int(rt, 2)] = data
    else:
        pass

def main():
    choice = int(input("Enter 1 for the Find Rank program, 2 for the LCM GCD program, 3 for the Binomial Expansion program.\nEnter your choice: "))

    if (choice == 1):       # Find Rank
        print("\nThis program inputs an array of integers and another integer. It then bubble sorts the array and finds the rank of the given integer in the sorted array.")

        n = int(input("\nEnter the number of integers in your array: "))    # s1
        in_address = int(input("Enter the starting address where you want to store the input array: "))     # s2
        out_address = int(input( "Enter the starting address where you want to store the output array: "))  # s3

        print("Enter the integers in your array:")
        for i in range(n):
            dataMem[in_address + 4*i] = int(input())

        rank_address = int(input("\nEnter the address where you want to store the rank: "))
        rank = int(input("Enter the number whose rank you want to find: "))
            
        reg[regMap["s1"]] = n
        reg[regMap["s2"]] = in_address
        reg[regMap["s3"]] = out_address
        reg[regMap["s4"]] = rank_address
        reg[regMap["s5"]] = rank

        while (PC <= 4194512):
            instr = fetch(instrMemRank)
            (opcode, rs, rt, rd, shamt, func, target, imm) = decode(instr)
            
            print(f"\nCURRENT INSTRUCTION: ", end = "")
            if (opcode == "000000"):
                if (func == "100000"):
                    print("ADD")
                elif (func == "100001"):
                    print("ADDU")
                elif (func == "100010"):
                    print("SUB")
                elif (func == "101010"):
                    print("SLT")
                elif (func == "000010"):
                    print("MUL")
                elif (func == "011010"):
                    print("DIV")
                elif (func == "010010"):
                    print("MFLO")
            
            elif opcode == "011100":
                print("MUL")
    
            elif (opcode == "000010"):
                print("JUMP")

            elif (opcode == "001000"):
                print("ADDI")

            elif (opcode == "000100"):
                print("BEQ")
                
            elif (opcode == "100011"):
                print("LW")
                
            elif (opcode == "101011"):
                print("SW")
                
            print(f"PC: {PC-4}\nOpcode: {opcode}, rs: {rs}, rt: {rt}, rd: {rd}, imm: {imm}, shamt: {shamt}, funct: {func}, target: {target}\n")

            ALUOutput = execute(rs, rt, imm, func, target)
            data = memory(ALUOutput, rt)
            writeBack(rt, rd, data)
                
            for k in range(len(reg)):
                if k == (len(reg)-1):
                    print(f"{k}: {reg[k]}", end = "")
                else:
                    print(f"{k}: {reg[k]}", end = ", ")
            
            print("\n")
        
        print("FINAL RESULT:")
        print("Sorted array:")
        for i in range(n):
            print(dataMem[out_address + 4*i])

        if dataMem[rank_address] == 0:
            print("\nNumber not found in the array!")
        else:
            print("\nRank: ", dataMem[rank_address])
    
    elif (choice == 2):     # GCD LCM
        print("\nThis program inputs two integers and finds their GCD and LCM.")

        n_add1 = int(input("\nEnter the address where you want to store the first number: ")) # s0
        n1 = int(input("Enter the first number: ")) # s4
        n_add2 = int(input("Enter the address where you want to store the second number: ")) # s1
        n2 = int(input("Enter the second number: ")) # s5
        GCD_add = int(input("Enter the address where you want to store the GCD: ")) # s2
        LCM_add = int(input("Enter the address where you want to store the LCM: ")) # s3

        reg[regMap["s0"]] = n_add1
        reg[regMap["s4"]] = n1
        reg[regMap["s1"]] = n_add2
        reg[regMap["s5"]] = n2
        reg[regMap["s2"]] = GCD_add
        reg[regMap["s3"]] = LCM_add

        while (PC <= 4194424):
            instr = fetch(instrMemLG)
            (opcode, rs, rt, rd, shamt, func, target, imm) = decode(instr)
            
            print(f"\nCURRENT INSTRUCTION: ", end = "")
            if (opcode == "000000"):
                if (func == "100000"):
                    print("ADD")
                elif (func == "100001"):
                    print("ADDU")
                elif (func == "100010"):
                    print("SUB")
                elif (func == "101010"):
                    print("SLT")
                elif (func == "000010"):
                    print("MUL")
                elif (func == "011010"):
                    print("DIV")
                elif (func == "010010"):
                    print("MFLO")
            
            elif opcode == "011100":
                print("MUL")
    
            elif (opcode == "000010"):
                print("JUMP")

            elif (opcode == "001000"):
                print("ADDI")

            elif (opcode == "000100"):
                print("BEQ")
                
            elif (opcode == "100011"):
                print("LW")
                
            elif (opcode == "101011"):
                print("SW")
            
            print(f"PC: {PC-4}\nOpcode: {opcode}, rs: {rs}, rt: {rt}, rd: {rd}, imm: {imm}, shamt: {shamt}, funct: {func}, target: {target}\n")

            ALUOutput = execute(rs, rt, imm, func, target)
            data = memory(ALUOutput, rt)
            writeBack(rt, rd, data)

            for k in range(len(reg)):
                if k == (len(reg)-1):
                    print(f"{k}: {reg[k]}", end = "")
                else:
                    print(f"{k}: {reg[k]}", end = ", ")
                
            print("\n")

        print("FINAL RESULT:")
        print(f"GCD of {n1} and {n2}: {dataMem[GCD_add]}")
        print(f"LCM of {n1} and {n2}: {dataMem[LCM_add]}")

    elif (choice == 3):     # Binomial Expansion
        print("\nThis program inputs an integer n and finds the binomial expansion of (1 + x)^n.")

        n_address = int(input("\nEnter the address where you want to store n: ")) # s0
        n = int(input("Enter n: ")) # s1
        out_address = int(input("Enter the starting address where you want to store the coefficients: ")) # s4
        dataMem[n_address] = n

        reg[regMap["s0"]] = n_address
        reg[regMap["s1"]] = n
        reg[regMap["s4"]] = out_address

        while (PC <= 4194512):
            instr = fetch(instrMemBinomial)
            (opcode, rs, rt, rd, shamt, func, target, imm) = decode(instr)
            
            print(f"\nCURRENT INSTRUCTION: ", end = "")
            if (opcode == "000000"):
                if (func == "100000"):
                    print("ADD")
                elif (func == "100001"):
                    print("ADDU")
                elif (func == "100010"):
                    print("SUB")
                elif (func == "101010"):
                    print("SLT")
                elif (func == "000010"):
                    print("MUL")
                elif (func == "011010"):
                    print("DIV")
                elif (func == "010010"):
                    print("MFLO")
            
            elif opcode == "011100":
                print("MUL")
    
            elif (opcode == "000010"):
                print("JUMP")

            elif (opcode == "001000"):
                print("ADDI")

            elif (opcode == "000100"):
                print("BEQ")
                
            elif (opcode == "100011"):
                print("LW")
                
            elif (opcode == "101011"):
                print("SW")

            print(f"PC: {PC-4}\nOpcode: {opcode}, rs: {rs}, rt: {rt}, rd: {rd}, imm: {imm}, shamt: {shamt}, funct: {func}, target: {target}\n")

            ALUOutput = execute(rs, rt, imm, func, target)
            data = memory(ALUOutput, rt)
            writeBack(rt, rd, data)

            for k in range(len(reg)):
                if k == (len(reg)-1):
                    print(f"{k}: {reg[k]}", end = "")
                else:
                    print(f"{k}: {reg[k]}", end = ", ")
        
            print("\n")
        
        print("FINAL RESULT:")
        print(f"\nBinomial expansion of (1 + x)^{n}:", end = " ")
        for i in range(n+1):
            if (i == n):
                print(f"{dataMem[out_address + 4*i]}x^{i}")
            else:
                print(f"{dataMem[out_address + 4*i]}x^{i}", end = " + ")

    else:
        print("Invalid input!")

main()
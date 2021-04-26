

def get_txt(myfile):
    list_instruction = []
    for line in myfile:
        instruction_line = line.strip()
        instruction_line = instruction_line.replace(",", " ")
        instruction_line = instruction_line.replace("(", " ")
        instruction_line = instruction_line.replace(")", " ")
        instruction_line = instruction_line.replace(":", " ")
        instruction_line = instruction_line.split()
        list_instruction.append(instruction_line)
    return list_instruction

def decimalToBinary(n, size):
    n = n.replace("x", "")
    dec2binary = bin(int(n)).replace("0b", "")
    while (len(dec2binary) < size): dec2binary = '0' + dec2binary
    return dec2binary

def bindigits(n, bits):
    s = bin(int(n) & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

def R_type(list_instruction, i):
    if list_instruction[i][0] == "add":
        funct5 = "00000"
        funct2 = "00"
        funct3 = "000"
        opcode = "0110011"
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rs2 = decimalToBinary(list_instruction[i][3], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return funct5 + funct2 + rs2 + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "sub":
        funct5 = "01000"
        funct2 = "00"
        funct3 = "000"
        opcode = "0110011"
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rs2 = decimalToBinary(list_instruction[i][3], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return funct5 + funct2 + rs2 + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "sll":
        funct5 = "00000"
        funct2 = "00"
        funct3 = "001"
        opcode = "0110011"
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rs2 = decimalToBinary(list_instruction[i][3], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return funct5 + funct2 + rs2 + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "slt":
        funct5 = "00000"
        funct2 = "00"
        funct3 = "010"
        opcode = "0110011"
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rs2 = decimalToBinary(list_instruction[i][3], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return funct5 + funct2 + rs2 + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "sltu":
        funct5 = "00000"
        funct2 = "00"
        funct3 = "011"
        opcode = "0110011"
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rs2 = decimalToBinary(list_instruction[i][3], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return funct5 + funct2 + rs2 + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "xor":
        funct5 = "00000"
        funct2 = "00"
        funct3 = "100"
        opcode = "0110011"
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rs2 = decimalToBinary(list_instruction[i][3], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return funct5 + funct2 + rs2 + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "srl":
        funct5 = "00000"
        funct2 = "00"
        funct3 = "101"
        opcode = "0110011"
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rs2 = decimalToBinary(list_instruction[i][3], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return funct5 + funct2 + rs2 + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "sra":
        funct5 = "01000"
        funct2 = "00"
        funct3 = "101"
        opcode = "0110011"
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rs2 = decimalToBinary(list_instruction[i][3], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return funct5 + funct2 + rs2 + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "or":
        funct5 = "00000"
        funct2 = "00"
        funct3 = "110"
        opcode = "0110011"
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rs2 = decimalToBinary(list_instruction[i][3], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return funct5 + funct2 + rs2 + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "and":
        funct5 = "00000"
        funct2 = "00"
        funct3 = "111"
        opcode = "0110011"
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rs2 = decimalToBinary(list_instruction[i][3], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return funct5 + funct2 + rs2 + rs1 + funct3 + rd + opcode

    else:
        print("R_type wrong!")

def I_type(list_instruction, i):
    if list_instruction[i][0] == "addi":
        funct3 = "000"
        opcode = "0010011"
        imm = bindigits(list_instruction[i][3], 12)
        #simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "slti":
        funct3 = "010"
        opcode = "0010011"
        imm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "sltiu":
        funct3 = "011"
        opcode = "0010011"
        imm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "xori":
        funct3 = "100"
        opcode = "0010011"
        imm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "ori":
        funct3 = "110"
        opcode = "0010011"
        imm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "andi":
        funct3 = "111"
        opcode = "0010011"
        imm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode
    elif list_instruction[i][0] == "lb":
        funct3 = "000"
        opcode = "0000011"
        imm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "lh":
        funct3 = "001"
        opcode = "0000011"
        imm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode


    elif list_instruction[i][0] == "lw":
        funct3 = "010"
        opcode = "0000011"
        imm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode


    elif list_instruction[i][0] == "lbu":
        funct3 = "100"
        opcode = "0000011"
        imm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "lhu":
        funct3 = "100"
        opcode = "0000011"
        imm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode
    elif list_instruction[i][0] == "jalr":
        funct3 = "000"
        opcode = "1100111"
        target_label = find_label(list_instruction, list_instruction[i][3], i)
        label = (target_label - i) * 2
        imm = bindigits(label, 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return imm + rs1 + funct3 + rd + opcode

    else:
        print("I_type wrong!")

def S_type(list_instruction, i):
    if list_instruction[i][0] == "sb":
        funct3 = "000"
        opcode = "0100011"
        imm = decimalToBinary(list_instruction[i][2], 12)
        rs1 = decimalToBinary(list_instruction[i][3], 5)
        rs2 = decimalToBinary(list_instruction[i][1], 5)
        return imm[0:7] + rs2 + rs1 + funct3 + imm[7:12] + opcode
    elif list_instruction[i][0] == "sh":
        funct3 = "001"
        opcode = "0100011"
        imm = decimalToBinary(list_instruction[i][2], 12)
        rs1 = decimalToBinary(list_instruction[i][3], 5)
        rs2 = decimalToBinary(list_instruction[i][1], 5)
        return imm[0:7] + rs2 + rs1 + funct3 + imm[7:12] + opcode

    elif list_instruction[i][0] == "sw":
        funct3 = "010"
        opcode = "0100011"
        imm = decimalToBinary(list_instruction[i][2], 12)
        rs1 = decimalToBinary(list_instruction[i][3], 5)
        rs2 = decimalToBinary(list_instruction[i][1], 5)
        return imm[0:7] + rs2 + rs1 + funct3 + imm[7:12] + opcode

    else:
        print("I_type wrong!")

def U_type(list_instruction, i):
    if list_instruction[i][0] == "lui":
        opcode = "0110111"
        rd = decimalToBinary(list_instruction[i][1], 5)
        simm = decimalToBinary(list_instruction[i][2],20)
        return simm + rd + opcode
    elif list_instruction[i][0] == "auipc":
        opcode = "0010111"
        rd = decimalToBinary(list_instruction[i][1], 5)
        simm = decimalToBinary(list_instruction[i][2],20)
        return simm + rd + opcode
    else:
        print("U_type wrong!")

def SB_type(list_instruction, i):
    if list_instruction[i][0] == "bne":
        opcode = "1100011"
        funct3 = "001"
        target_label = find_label(list_instruction, list_instruction[i][3], i)
        label = (target_label - i)*2
        imm = bindigits(label, 12)
        rs1 = decimalToBinary(list_instruction[i][1], 5)
        rs2 = decimalToBinary(list_instruction[i][2], 5)
        return imm[0] + imm[2:8] + rs2 + rs1 + funct3 + imm[8:12] + imm[1] +opcode
    elif list_instruction[i][0] == "beq":
        opcode = "1100011"
        funct3 = "000"
        target_label = find_label(list_instruction, list_instruction[i][3], i)
        label = (target_label - i)*2
        imm = bindigits(label, 12)
        rs1 = decimalToBinary(list_instruction[i][1], 5)
        rs2 = decimalToBinary(list_instruction[i][2], 5)
        return imm[0] + imm[2:8] + rs2 + rs1 + funct3 + imm[8:12] + imm[1] +opcode
    elif list_instruction[i][0] == "blt":
        opcode = "1100011"
        funct3 = "100"
        target_label = find_label(list_instruction, list_instruction[i][3], i)
        label = (target_label - i)*2
        imm = bindigits(label, 12)
        rs1 = decimalToBinary(list_instruction[i][1], 5)
        rs2 = decimalToBinary(list_instruction[i][2], 5)
        return imm[0] + imm[2:8] + rs2 + rs1 + funct3 + imm[8:12] + imm[1] +opcode
    elif list_instruction[i][0] == "bge":
        opcode = "1100011"
        funct3 = "101"
        target_label = find_label(list_instruction, list_instruction[i][3], i)
        label = (target_label - i)*2
        imm = bindigits(label, 12)
        rs1 = decimalToBinary(list_instruction[i][1], 5)
        rs2 = decimalToBinary(list_instruction[i][2], 5)
        return imm[0] + imm[2:8] + rs2 + rs1 + funct3 + imm[8:12] + imm[1] +opcode
    elif list_instruction[i][0] == "bltu":
        opcode = "1100011"
        funct3 = "110"
        target_label = find_label(list_instruction, list_instruction[i][3], i)
        label = (target_label - i)*2
        imm = bindigits(label, 12)
        rs1 = decimalToBinary(list_instruction[i][1], 5)
        rs2 = decimalToBinary(list_instruction[i][2], 5)
        return imm[0] + imm[2:8] + rs2 + rs1 + funct3 + imm[8:12] + imm[1] +opcode
    elif list_instruction[i][0] == "bgeu":
        opcode = "1100011"
        funct3 = "111"
        target_label = find_label(list_instruction, list_instruction[i][3], i)
        label = (target_label - i)*2
        imm = bindigits(label, 12)
        rs1 = decimalToBinary(list_instruction[i][1], 5)
        rs2 = decimalToBinary(list_instruction[i][2], 5)
        return imm[0] + imm[2:8] + rs2 + rs1 + funct3 + imm[8:12] + imm[1] +opcode
    else:
        print("SB_type wrong!")

def UJ_type(list_instruction, i):
    if list_instruction[i][0] == "jal":
        opcode = "1101111"
        rd = decimalToBinary(list_instruction[i][1], 5)
        target_label = find_label(list_instruction, list_instruction[i][2], i)
        label = (target_label - i) * 2
        imm = bindigits(label, 20)
        return imm[0] + imm[10:20] + imm[9] + imm[1:9] + rd + opcode
    else:
        print("UJ_type wrong")

def swap(list_instruction, i):
    j = 0
    temp = list_instruction[i][j]
    for line in list_instruction[i]:
        j = j+1
    j = j-1
    k = 0
    while k < j:
        list_instruction[i][k] = list_instruction[i][k+1]
        k = k+1
    list_instruction[i][j] = temp

def find_label(list_instruction, label, index):
    i = 0
    while i < length:
        j = 0
        for line in list_instruction[i]:
            if list_instruction[i][j] == label:
                if list_instruction[i][0] == "beq" or list_instruction[i][0] == "bne" or \
                    list_instruction[i][0] == "blt" or list_instruction[i][0] == "bge" or \
                    list_instruction[i][0] == "bltu" or list_instruction[i][0] == "bgeu" or \
                    list_instruction[i][0] == "jalr":
                    if j == 3:
                        break
                    else:
                        return i
                elif list_instruction[i][0] == "jal":
                    if j == 2:
                        break
                    else:
                        return i
                else:
                    return i 

            elif i == index:
                break
            else:
                j = j+1
        i = i+1
    return 1000


def main():
    with open("project.txt", "r") as myfile:
        list_instruction = get_txt(myfile)
        print(list_instruction)
    global length
    length = len(list_instruction)

    i = 0
    while i < length:
        if list_instruction[i][0] == "add" or list_instruction[i][0] == "sub" or \
            list_instruction[i][0] == "sll" or list_instruction[i][0] == "slt" or \
            list_instruction[i][0] == "sltu" or list_instruction[i][0] == "xor" or \
            list_instruction[i][0] == "srl" or list_instruction[i][0] == "sra" or \
            list_instruction[i][0] == "or" or list_instruction[i][0] == "and" or\
            list_instruction[i][0] == "addi" or list_instruction[i][0] == "slti" or \
            list_instruction[i][0] == "sltiu" or list_instruction[i][0] == "xori" or \
            list_instruction[i][0] == "ori" or list_instruction[i][0] == "andi" or \
            list_instruction[i][0] == "slli" or list_instruction[i][0] == "srli" or \
            list_instruction[i][0] == "srai" or list_instruction[i][0] == "lb" or \
            list_instruction[i][0] == "lh" or list_instruction[i][0] == "lw" or \
            list_instruction[i][0] == "lbu" or list_instruction[i][0] == "lhu" or \
            list_instruction[i][0] == "beq" or list_instruction[i][0] == "bne" or \
            list_instruction[i][0] == "blt" or list_instruction[i][0] == "bge" or \
            list_instruction[i][0] == "bltu" or list_instruction[i][0] == "bgeu" or \
            list_instruction[i][0] == "sb" or list_instruction[i][0] == "sh" or \
            list_instruction[i][0] == "sw" or list_instruction[i][0] == "lui" or \
            list_instruction[i][0] == "auipc" or list_instruction[i][0] == "jal" or \
            list_instruction[i][0] == "jalr":
            i = i+1
        else:
            swap(list_instruction, i)
            i = i+1
    print(list_instruction)
    i = 0

    while i < length:
        if list_instruction[i][0] == "add" or list_instruction[i][0] == "sub" or \
            list_instruction[i][0] == "sll" or list_instruction[i][0] == "slt" or \
            list_instruction[i][0] == "sltu" or list_instruction[i][0] == "xor" or \
            list_instruction[i][0] == "srl" or list_instruction[i][0] == "sra" or \
            list_instruction[i][0] == "or" or list_instruction[i][0] == "and" :
            machine_code = R_type(list_instruction, i)
            print(machine_code)
            i = i + 1
        elif list_instruction[i][0] == "addi" or list_instruction[i][0] == "slti" or \
            list_instruction[i][0] == "sltiu" or list_instruction[i][0] == "xori" or \
            list_instruction[i][0] == "ori" or list_instruction[i][0] == "andi" or \
            list_instruction[i][0] == "slli" or list_instruction[i][0] == "srli" or \
            list_instruction[i][0] == "srai" or list_instruction[i][0] == "lb" or \
            list_instruction[i][0] == "lh" or list_instruction[i][0] == "lw" or \
            list_instruction[i][0] == "lbu" or list_instruction[i][0] == "lhu" or \
            list_instruction[i][0] == "jalr":
            machine_code = I_type(list_instruction, i)
            print(machine_code)
            i = i + 1
        elif list_instruction[i][0] == "sb" or list_instruction[i][0] == "sh" or \
            list_instruction[i][0] == "sw":
            machine_code = S_type(list_instruction, i)
            print(machine_code)
            i = i + 1
        elif list_instruction[i][0] == "beq" or list_instruction[i][0] == "bne" or \
            list_instruction[i][0] == "blt" or list_instruction[i][0] == "bge" or \
            list_instruction[i][0] == "bltu" or list_instruction[i][0] == "bgeu":
            machine_code = SB_type(list_instruction,i)
            print(machine_code)
            i = i + 1
        elif list_instruction[i][0] == "lui" or list_instruction[i][0] == "auipc":
            machine_code = U_type(list_instruction, i)
            print(machine_code)
            i = i+1
        else:
            print("have no instruction")
            i = i + 1
    print("done")



main()

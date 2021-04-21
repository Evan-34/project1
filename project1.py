
def get_txt(myfile):
    list_instruction = []
    for line in myfile:
        instruction_line = line.strip()
        instruction_line = instruction_line.replace(",", " ")
        instruction_line = instruction_line.replace("(", " ")
        instruction_line = instruction_line.replace(")", " ")
        instruction_line = instruction_line.split()
        list_instruction.append(instruction_line)
    return list_instruction

def decimalToBinary(n, size):
    n = n.replace("x", "")
    dec2binary = bin(int(n)).replace("0b", "")
    while (len(dec2binary) < size): dec2binary = '0' + dec2binary
    return dec2binary

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
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "slti":
        funct3 = "010"
        opcode = "0010011"
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "sltiu":
        funct3 = "011"
        opcode = "0010011"
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "xori":
        funct3 = "100"
        opcode = "0010011"
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "ori":
        funct3 = "110"
        opcode = "0010011"
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "andi":
        funct3 = "111"
        opcode = "0010011"
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode
    elif list_instruction[i][0] == "lb":
        funct3 = "000"
        opcode = "0000011"
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "lh":
        funct3 = "001"
        opcode = "0000011"
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode


    elif list_instruction[i][0] == "lw":
        funct3 = "010"
        opcode = "0000011"
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode


    elif list_instruction[i][0] == "lbu":
        funct3 = "100"
        opcode = "0000011"
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode

    elif list_instruction[i][0] == "lhu":
        funct3 = "100"
        opcode = "0000011"
        simm = decimalToBinary(list_instruction[i][3], 12)
        rs1 = decimalToBinary(list_instruction[i][2], 5)
        rd = decimalToBinary(list_instruction[i][1], 5)
        return simm + rs1 + funct3 + rd + opcode

    else:
        print("I_type wrong!")

def S_type(list_instruction, i):
    if list_instruction[i][0] == "sb":
        funct3 = "000"
        opcode = "0000011"
        simm = decimalToBinary(list_instruction[i][2], 12)
        rs1 = decimalToBinary(list_instruction[i][3], 5)
        rs2 = decimalToBinary(list_instruction[i][1], 5)
        return simm[0:7] + rs2 + rs1 + funct3 + simm[7:12] + opcode
    elif list_instruction[i][0] == "sh":
        funct3 = "001"
        opcode = "0000011"
        simm = decimalToBinary(list_instruction[i][2], 12)
        rs1 = decimalToBinary(list_instruction[i][3], 5)
        rs2 = decimalToBinary(list_instruction[i][1], 5)
        return simm[0:7] + rs2 + rs1 + funct3 + simm[7:12] + opcode

    elif list_instruction[i][0] == "sw":
        funct3 = "010"
        opcode = "0000011"
        simm = decimalToBinary(list_instruction[i][2], 12)
        rs1 = decimalToBinary(list_instruction[i][3], 5)
        rs2 = decimalToBinary(list_instruction[i][1], 5)
        return simm[0:7] + rs2 + rs1 + funct3 + simm[7:12] + opcode

    else:
        print("I_type wrong!")

def swap(list_instruction, i):
    temp = list_instruction[i][0]
    list_instruction[i][0] = list_instruction[i][1]
    list_instruction[i][1] = list_instruction[i][2]
    list_instruction[i][2] = list_instruction[i][3]
    list_instruction[i][3] = list_instruction[i][4]
    list_instruction[i][4] = temp

def main():
    with open("project.txt", "r") as myfile:
        list_instruction = get_txt(myfile)
        print(list_instruction)

    lenth = len(list_instruction)
    i = 0

    while i < lenth:
        if list_instruction[i][0] == "add" or list_instruction[i][0] == "sub" or \
            list_instruction[i][0] == "sll" or list_instruction[i][0] == "slt" or \
            list_instruction[i][0] == "sltu" or list_instruction[i][0] == "xor" or \
            list_instruction[i][0] == "srl" or list_instruction[i][0] == "sra" or \
            list_instruction[i][0] == "or" or list_instruction[i][0] == "and":
            machine_code = R_type(list_instruction, i)
            print(machine_code)
            i = i + 1
        elif list_instruction[i][0] == "addi" or list_instruction[i][0] == "slti" or \
            list_instruction[i][0] == "sltiu" or list_instruction[i][0] == "xori" or \
            list_instruction[i][0] == "ori" or list_instruction[i][0] == "andi" or \
            list_instruction[i][0] == "slli" or list_instruction[i][0] == "srli" or \
            list_instruction[i][0] == "srai" or list_instruction[i][0] == "lb" or \
            list_instruction[i][0] == "lh" or list_instruction[i][0] == "lw" or \
            list_instruction[i][0] == "lbu" or list_instruction[i][0] == "lhu":
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
            i = i + 1
            print("none")

        else:
            swap(list_instruction, i)
    print("done")
main()

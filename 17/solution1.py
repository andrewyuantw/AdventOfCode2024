with open('input.txt') as file:
    grid = []
    counter = 0
    A, B, C = 0, 0, 0
    op_codes = []
    operands = []
    ret = ""

    def getComboVal(operand):
        if operand <= 3:
            return operand
        elif operand == 4:
            return A
        elif operand == 5:
            return B
        elif operand == 6:
            return C
        else:
            return 1

    for line in file.readlines():
        line = line.rstrip("\n")
        if counter == 0:
            A = int(line[len("Register A: "):])
        elif counter == 1:
            B = int(line[len("Register B: "):])
        elif counter == 2:
            C = int(line[len("Register C: "):])
        elif counter == 4:
            ops = line[len("Program: "):].split(",")
            for index, val in enumerate(ops):
                if index % 2 == 0:
                    op_codes.append(int(val))
                else:
                    operands.append(int(val))
            print(op_codes)
            print(operands)
        counter += 1
    instr_pointer = 0
    while instr_pointer < len(op_codes):
        hasJumped = False
        curr_op_code = op_codes[instr_pointer]
        curr_operand = operands[instr_pointer]
        if curr_op_code == 0:
            A = int(A / (2 ** getComboVal(curr_operand)))
        elif curr_op_code == 1:
            B = B ^curr_operand
        elif curr_op_code == 2:
            B = getComboVal(curr_operand) % 8
        elif curr_op_code == 3:
            if A != 0:
                instr_pointer = curr_operand
                hasJumped = True
        elif curr_op_code == 4:
            B = B ^ C
        elif curr_op_code == 5:
            ret += str(getComboVal(curr_operand)  % 8) + ","
        elif curr_op_code == 6:
            B = int(A / (2 ** getComboVal(curr_operand)))
        elif curr_op_code == 7:
            C = int(A / (2 ** getComboVal(curr_operand)))
        if not hasJumped:
            instr_pointer += 1
    print(ret[:-1])
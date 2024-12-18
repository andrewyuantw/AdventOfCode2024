with open('input.txt') as file:
    counter = 0
    initB, initC = 0, 0
    op_codes = []
    operands = []

    correct_output = ""
    for line in file.readlines():
        line = line.rstrip("\n")
        if counter == 1:
            initB = int(line[len("Register B: "):])
        elif counter == 2:
            initC = int(line[len("Register C: "):])
        elif counter == 4:
            ops = line[len("Program: "):].split(",")
            for index, val in enumerate(ops):
                correct_output += val + ","
                if index % 2 == 0:
                    op_codes.append(int(val))
                else:
                    operands.append(int(val))
        counter += 1
    correct_output = correct_output[:-1]

    # Turn part 1 into a helper function
    def helper(a_val):
        register = [a_val, initB, initC]
        def getComboVal(operand):
            if operand <= 3:
                return operand
            elif operand == 4:
                return register[0]
            elif operand == 5:
                return register[1]
            elif operand == 6:
                return register[2]
            else:
                return 1
        ret = ""
        instr_pointer = 0
        while instr_pointer < len(op_codes):
            hasJumped = False
            curr_op_code = op_codes[instr_pointer]
            curr_operand = operands[instr_pointer]
            if curr_op_code == 0:
                register[0] = int(register[0] / (2 ** getComboVal(curr_operand)))
            elif curr_op_code == 1:
                register[1] = register[1] ^ curr_operand
            elif curr_op_code == 2:
                register[1] = getComboVal(curr_operand) % 8
            elif curr_op_code == 3:
                if register[0] != 0:
                    instr_pointer = curr_operand
                    hasJumped = True
            elif curr_op_code == 4:
                register[1] = register[1] ^ register[2]
            elif curr_op_code == 5:
                ret += str(getComboVal(curr_operand)  % 8) + ","
            elif curr_op_code == 6:
                register[1] = int(register[0] / (2 ** getComboVal(curr_operand)))
            elif curr_op_code == 7:
                register[2] = int(register[0] / (2 ** getComboVal(curr_operand)))
            if not hasJumped:
                instr_pointer += 1
        return(ret[:-1])
    
    guesses = [0]
    new_guesses = []
    untouched_guess = []
    counter = 0
    '''
    On the very last digit, A HAS to be between 0 and 7
    since it terminates immediately after
    so of the 8 options (0 - 7), what actually produces the final digit in my pattern?
    I used part 1 as my helper and ran it 8 times. 
    In my example, I found only 4 produced my desired final digit.

    Now I can reverse engineer it, for the second to last iteration
    int(A / 8) = 4
    so A's value in the second to last iteration is between 32 and 39
    Use part 1 helper to run through 32 to 39
    what produces my final two digits?
    In my case, both 37 and 39.

    Reverse engineer, the past iteration A must have been between 37 * 8 to 37 * 8 + 7
    and 39 * 8 and 39 * 8 + 7
    '''
    for i in range(len(correct_output)-1, -1, -2):
        output_to_match = correct_output[i:]
        for init_guess in guesses:
            for guess in range(init_guess, init_guess + 8):
                if helper(guess) == output_to_match:
                    new_guesses.append(guess * 8)
        guesses = new_guesses
        new_guesses = []
        counter += 1
    untouched = []
    for i in guesses:
        untouched.append(int(i / 8))
    untouched.sort()
    print(untouched)
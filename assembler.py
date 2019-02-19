"""

nand2tetris: Project 6: The Assembler

Objective:
* Write an Assembler program that translates programs 
  written in the symbolic Hack assembly language 
  into binary code that can execute on the Hack hardware platform 
  built in the previous projects.

Usage:
* python3 assembler.py ...
                    ...add/Add.asm

"""

"""

Instructions:
* A-instruction: @value
    0vvv vvvv vvvv vvvv
    * v: binary address to write to A-register
* C-instruction: dest=comp;jump
    111a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3
    * a: use M instead of A
    * c1-6: comp
    * d1-3: dest
    * j1-3: jump

"""

import sys


arguments = sys.argv[1:] # Ignore first element (the name of the module)

# Open the file that will be translated
file_to_translate_path = arguments[0]
paths = file_to_translate_path.split("/")
file_to_translate = open(file_to_translate_path)

print("Opened file:", file_to_translate_path)


# Create the binary file
translated_file_path = "/".join(paths[0:-1]) + "/" + paths[-1].strip(".asm") + ".hack"
translated_file = open(translated_file_path, "w+")

print("Created/opened file:", translated_file_path)


# Translation
for l, line in enumerate(file_to_translate):
    # Remove comments and whitespace from the line
    line = line.split("//")[0].strip()
    print(line)

    instruction_type = 1 # 0=a, 1=c
    v = 0b0 # A-instruction address

    a, c, d, j = "0", "000000", ["0"] * 3, ["0"] * 3
    
    # Skip empty lines
    if len(line) == 0: continue

    # Read the line to determine the instruction
    if line[0] == "@":
        instruction_type = 0 # A-instruction
        print("A-instruction")

        address_dec = int(line[1:])
        
        if address_dec > 2 ** 15: # max 15-bit integer (32767)
            raise Exception("Address " + str(address_dec) + " exceeds the maximum capacity.")
        if address_dec < 0: # Address cannot be negative
            raise Exception("Address cannot be negative.")
        
        v = format(address_dec, "015b")
    else:
        instruction_type = 1 # C-instruction
        print("C-instruction")

        comp, dest, jump = None, None, None
        if "=" in line:
            dest = line.split("=")[0]
        if ";" in line: # dest, jump
            jump = line.split(";")[1]
        comp = line
        temp = comp.split("=")
        if len(temp) > 1:
            comp = temp[1]
        temp = comp.split(";")
        if len(temp) > 0:
            comp = temp[0]

        print("dest:", dest, "| comp:", comp, "| jump:", jump)

        # Parse comp
        if comp == "0":
            c = "101010"
        elif comp == "1":
            c = "111111"
        elif comp == "-1":
            c = "111010"
        elif comp == "D":
            c = "001100"
        elif comp == "A":
            c = "110000"
        elif comp == "!D":
            c = "001101"
        elif comp == "!A":
            c = "110001"
        elif comp == "-D":
            c = "001111"
        elif comp == "-A":
            c = "110011" # TODO finish hardcoding cause im a bad coder

        # Parse dest
        if dest is not None:
            if "A" in dest: d[0] = "1"
            if "D" in dest: d[1] = "1"
            if "M" in dest: d[2] = "1"

        # Parse jump
        if jump is not None:
            if jump[0:2] == "JG": 
                if jump[2] == "T" or jump[2] == "E": 
                    j[2] = "1"
                    if jump[2] == "E": j[1] = "1"
                else:
                    raise Exception("Invalid jump command: " + jump)
            elif jump[0:2] == "JL":
                if jump[2] == "T" or jump[2] == "E": 
                    j[0] = "1"
                    if jump[2] == "E": j[1] = "1"
                else:
                    raise Exception("Invalid jump command: " + jump)
            elif jump == "JMP": j[0:3] = ["1"] * 3
            elif jump == "JNE": 
                j[0], j[2] = "1", "1"
            elif jump == "JEQ": 
                j[1] = "1"
            else:
                raise Exception("Invalid jump command: " + jump)

    # Construct the instruction
    if instruction_type == 0:
        translated_file.write("0" + v + "\n")
    elif instruction_type == 1:
        translated_file.write("111" + a + c + "".join(d) + "".join(j) + "\n")

    print("\n")

# Close opened files
file_to_translate.close()
translated_file.close()


print("Done.")
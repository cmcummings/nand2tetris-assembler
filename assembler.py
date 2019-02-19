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
binary_lines = []
for l, line in enumerate(file_to_translate):
    # Remove comments and whitespace from the line
    line = line.split("//")[0].strip()
    print(line)

    instruction_type = 1 # 0=a, 1=c
    v = 0b0 # A-instruction address

    a, c, d, j = "0", ["0"] * 6, ["0"] * 3, ["0"] * 3
    
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
        if dest is not None:
            comp = comp.split("=")[1]
            if jump is not None:
                comp = comp.split(";")[0]

        print("dest:", dest, "| comp:", comp, "| jump:", jump)

        # Parse comp
        

        # Parse dest
        if dest is not None:
            if "A" in dest: d[0] = "1"
            if "D" in dest: d[1] = "1"
            if "M" in dest: d[2] = "1"

        # Parse jump
        if jump is not None:
            if jump[0:2] == "JG": 
                j[2] = "1"
                if jump[2] == "E": j[1] = "1"
            elif jump[0:2] == "JL":
                j[0] = "1"
                if jump[2] == "E": j[1] = "1"
            elif jump == "JMP": j[0:3] = ["1"] * 3
            elif jump == "JNE": 
                j[0], j[2] = "1", "1"
            elif jump == "JEQ": 
                j[1] = "1"        

    # Construct the instruction
    if instruction_type == 0:
        print(str(v))
        binary_lines.append("0" + v)
    elif instruction_type == 1:
        binary_lines.append("111" + a + "".join(c) + "".join(d) + "".join(j))

    print("\n")


# Write the binary lines to the binary file
for line in binary_lines:
    translated_file.write(line + "\n")


# Close opened files
file_to_translate.close()
translated_file.close()


print("Done.")
"""

nand2tetris: Project 6: The Assembler

Objective:
* Write an Assembler program that translates programs 
  written in the symbolic Hack assembly language 
  into binary code that can execute on the Hack hardware platform 
  built in the previous projects.

Usage:
* python assembler.py ...
                   ...add/Add.asm

"""

"""

Instructions:
* A-instruction: @value
    0vvv vvvv vvvv vvvv
* C-instruction: dest=comp;jump
    111a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3

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
for line in file_to_translate:
    # Remove comments and whitespace from the line
    line = line.split("//")[0].strip()
    print(line)

    instruction_type = 1 # 0=a, 1=c
    v = 0 # A-instruction address
    

    # Read the line to determine the instruction
    if line[0] == "@":
        instruction_type = 0 # A-instruction
    else:
        instruction_type = 1 # C-instruction

    # Construct the instruction



# Write the binary lines to the binary file
for line in binary_lines:
    translated_file.write(line + "\n")


# Close opened files
file_to_translate.close()
translated_file.close()


print("Done.")
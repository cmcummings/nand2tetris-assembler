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

# assembler.py
# the main module

import sys, code, utils
from parser import Parser, A_COMMAND, C_COMMAND, L_COMMAND
from writer import Writer
from symboltable import SymbolTable


# Get arguments
arguments = sys.argv[1:] # Ignore first element (the name of the module)
path = arguments[0]

# Load files
asm_file = Parser(path) # Open the file that will be translated
hack_file = Writer(utils.get_path_with_different_extension(path, ".hack")) # Create/open the binary file that will be written to

# Translate!
while asm_file.has_more_commands():
    line = asm_file.advance()
    
    # Skip empty lines
    if len(line) == 0: continue

    print(line)

    # Determine the instruction type
    command_type = line.command_type()

    if command_type == A_COMMAND:
        print("A COMMAND")

        address = line.symbol()

        print(address)
    
    elif command_type == C_COMMAND:
        print("C COMMAND")
    

    
    elif command_type == L_COMMAND:
        print("L COMMAND")



    print("\n")
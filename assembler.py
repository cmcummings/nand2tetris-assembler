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

import sys, code, utils, comparer
from parser import Parser, A_COMMAND, C_COMMAND, L_COMMAND
from writer import Writer
from symboltable import SymbolTable


# Get arguments
arguments = sys.argv[1:] # Ignore first element (the name of the module)
path = arguments[0]

# Load files
asm_file = Parser(path) # Open the file that will be translated
hack_file_path = utils.get_path_with_different_extension(path, ".cack")
hack_file = Writer(hack_file_path) # Create/open the binary file that will be written to

# Translate!
while asm_file.has_more_commands():
    line = asm_file.advance()


    print(line)

    # Determine the instruction type
    command_type = asm_file.command_type()

    if command_type == A_COMMAND:
        print("A COMMAND")

        address = asm_file.symbol()
        print(address)

        hack_file.write_line(code.construct_a_instruction(address))
    
    elif command_type == C_COMMAND:
        print("C COMMAND")

        asm_comp = asm_file.comp()
        asm_dest = asm_file.dest()
        asm_jump = asm_file.jump()

        bin_comp = code.translate_comp(asm_comp)
        bin_dest = code.translate_dest(asm_dest)
        bin_jump = code.translate_jump(asm_jump)

        hack_file.write_line(code.construct_c_instruction(bin_comp, bin_dest, bin_jump))

    elif command_type == L_COMMAND:
        print("L COMMAND")

        address = asm_file.symbol()

        print(address)

    print("\n")


comparer.compare(hack_file_path, utils.get_path_with_different_extension(path, ".hack"))
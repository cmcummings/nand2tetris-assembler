# code.py
# Translates Hack assembly language mnemonics into binary codes
from exceptions import InvalidJumpCommandError

def translate_dest(mnemonic):
    """Returns the 3-bit binary code of the dest mnemonic (string)"""
    if "A" in mnemonic: d[0] = "1"
    if "D" in mnemonic: d[1] = "1"
    if "M" in mnemonic: d[2] = "1"


def translate_comp(mnemonic):
    """Returns the 7-bit binary code of the comp mnemonic (string)"""
    if mnemonic == "0":
       return "0101010"
    elif mnemonic == "1":
       return "0111111"
    elif mnemonic == "-1":
       return "0111010"
    elif mnemonic == "D":
       return "0001100"
    elif mnemonic == "A":
       return "0110000"
    elif mnemonic == "!D":
       return "0001101"
    elif mnemonic == "!A":
       return "0110001"
    elif mnemonic == "-D":
       return "0001111"
    elif mnemonic == "-A":
       return "0110011"
    elif mnemonic == "D+1" or mnemonic == "1+D":
       return "0011111"
    elif mnemonic == "A+1" or mnemonic == "1+A":
       return "0110111"
    elif mnemonic == "D-1":
       return "0001110"
    elif mnemonic == "A-1":
       return "0110010"
    elif mnemonic == "D+A" or mnemonic == "A+D":
       return "0000010"
    elif mnemonic == "D-A":
       return "0010011"
    elif mnemonic == "A-D":
       return "0000111"
    elif mnemonic == "D&A" or mnemonic == "A&D":
       return "0000000"
    elif mnemonic == "D|A" or mnemonic == "A|D":
       return "0010101"
    elif mnemonic == "M":
        return "1110000"
    elif mnemonic == "!M":
        return "1110001"
    elif mnemonic == "-M":
        return "1110011"
    elif mnemonic == "M+1" or mnemonic == "1+M":
        return "1110111"
    elif mnemonic == "M-1":
        return "1110010"
    elif mnemonic == "D+M" or mnemonic == "M+D":
        return "1000010"
    elif mnemonic == "D-M":
        return "1010011"
    elif mnemonic == "M-D":
        return "1000111"
    elif mnemonic == "D&M" or mnemonic == "M&D":
        return "1000000"
    elif mnemonic == "D|M" or mnemonic == "M|D":
        return "1010101"
        
    
def translate_jump(mnemonic):
    """Returns the 3-bit binary code of the jump mnemonic (string)"""
    j = ["0"] * 3
    if jump[0:2] == "JG": 
        if jump[2] == "T" or jump[2] == "E": 
            j[2] = "1"
            if jump[2] == "E": j[1] = "1"
        else:
            raise InvalidJumpCommandError("Invalid jump command: " + jump)
    elif jump[0:2] == "JL":
        if jump[2] == "T" or jump[2] == "E": 
            j[0] = "1"
            if jump[2] == "E": j[1] = "1"
        else:
            raise InvalidJumpCommandError("Invalid jump command: " + jump)
    elif jump == "JMP": 
        j[0:3] = ["1"] * 3
    elif jump == "JNE": 
        j[0], j[2] = "1", "1"
    elif jump == "JEQ": 
        j[1] = "1"
    else:
        raise InvalidJumpCommandError("Invalid jump command: " + jump)
    return "".join(j)
    

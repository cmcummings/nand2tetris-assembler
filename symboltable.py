# symboltable.py

PREDEFINED_SYMBOLS = [
    ("SP", 0),
    ("LCL", 1),
    ("ARG", 2),
    ("THIS", 3),
    ("THAT", 4),
    ("R0", 0),
    ("R1", 1),
    ("R2", 2),
    ("R3", 3),
    ("R4", 4),
    ("R5", 5),
    ("R6", 6),
    ("R7", 7),
    ("R8", 8),
    ("R9", 9),
    ("R10", 10),
    ("R11", 11),
    ("R12", 12),
    ("R13", 13),
    ("R14", 14),
    ("R15", 15),
    ("SCREEN", 16384),
    ("KBD", 24576)
]

class SymbolTable:
    """Keeps a correspondence between symbol labels and numeric addresses"""
    
    def __init__(self):
        # Table structure: [(symbol, address), (symbol2, address2), ...]
        self.table = [] 
        self.next_variable_address = 16
    
    def add_entry(self, symbol, address=None):
        """Adds the pair (symbol, address) to the table and returns it.
        Address is assigned automatically by this function."""
        if self.contains(symbol):
            return self.get_address(symbol)

        if address is None: # If no address specified, automatically assign it
            address = -1
            for predef in PREDEFINED_SYMBOLS:
                if symbol == predef[0]:
                    address = predef[1]
            if address == -1:
                address = self.next_variable_address
                self.next_variable_address += 1
            
        self.table.append((symbol, address))
        return self.get_address(symbol)

    def contains(self, symbol):
        """Returns if the symbol table contains the given symbol."""
        for elem in self.table:
            if elem[0] == symbol:
                return True
        return False

    def get_address(self, symbol):
        """Returns the address associated with the given symbol."""
        for elem in self.table:
            if elem[0] == symbol:
                return elem[1]
        return None
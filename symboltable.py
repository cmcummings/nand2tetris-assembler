# symboltable.py

class SymbolTable:
    """Keeps a correspondence between symbol labels and numeric addresses"""
    
    def __init__(self):
        # Table structure: [(symbol, address), (symbol2, address2), ...]
        self.table = [] 
    
    def add_entry(self, symbol, address):
        """Adds the pair (symbol, address) to the table."""
        self.table.append(symbol, address)

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
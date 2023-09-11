import pandas as pd

class LexicalAnalyzer:
    
    def __init__(self) -> None:
        self.final_state = [2, 4, 5, 7, 8,
                            10, 11, 12, 13,
                            14, 15, 17, 18,
                            19, 20, 21, 22]
        self.backtracking_state = [2, 4, 7, 10, 17, 22]
        self.symbols_list = []
        self.matriz = pd.read_excel("files/input/transition_table.xlsx")

    def getColumn(self, char: str):
        D = "0123456789"
        S = ''' /#*^:;=<>(\)"'''

        if char.isalpha():
            return self.matriz.columns.get_loc("L")
        
        elif char in D:
            return self.matriz.columns.get_loc("D")
        
        elif char in S:
            return self.matriz.columns.get_loc(char)

    def add_symbols_table(self, state, lexeme):
        if state == 21:
            return

        elif state == 22:
            for symbol in self.symbols_list:
                if symbol == lexeme:
                    self.symbols_list.pop(self.symbols_list.index(lexeme))

            self.symbols_list.append(lexeme)
            print(f"<{lexeme}, {self.symbols_list.index(lexeme)}>")

        elif self.is_reserved(lexeme):
            self.symbols_list.append(lexeme)

        elif self.is_special_char(lexeme):
            self.symbols_list.append(lexeme)

        elif self.is_digit(lexeme):
            self.symbols_list.append(lexeme)

        elif self.is_identifier(lexeme):
            self.symbols_list.append(lexeme)

        else:
            if lexeme in self.symbols_list:
                self.symbols_list.pop(self.symbols_list.index(lexeme))

            self.symbols_list.append(lexeme)
            print(f"<{lexeme}, {self.symbols_list.index(lexeme)}>")

    def is_reserved(self, lexeme):
        self.reserveds = ["DEFINICOES", 
                     "FIM", 
                     "INICIO", 
                     "LEIA", 
                     "IF", 
                     "PRINT", 
                     "ELSE"]
        
        if lexeme in self.reserveds:
            return True
        
        return False
    
    def is_identifier(self, lexeme):
        if lexeme == "var":
            return False
        
        elif lexeme.upper() in self.reserveds:
            return False

        elif len(lexeme) < 13:
            return True
        
        return False
    
    def is_digit(self, lexeme):
        if lexeme.isdigit():
            return True
        
        return False
        
    def is_special_char(self, lexeme):
        S = ''' /#*^:;=<>(\)"'''

        if lexeme in S:
            return True
        
        return False
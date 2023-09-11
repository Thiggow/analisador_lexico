import string, pandas as pd


class LexicalAnalyzer:
    
    def __init__(self) -> None:
        self.final_state = [2, 4, 5, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.backtracking_state = [2, 4, 7, 10, 11, 18]
        self.matriz = pd.read_excel("files/input/transition_table.xlsx")
        print(self.matriz)

    def getColumn(self, char: str):
        L = string.ascii_letters
        D = "0123456789"
        S = " /#^:;=<>(\)"

        if char in L:
            return self.matriz.columns.get_loc("L")
        
        elif char in D:
            return self.matriz.columns.get_loc("D")
        
        elif char in S:
            return self.matriz.columns.get_loc(char)

    def add_tokens_list(self):
        pass

    def is_reserevd(self):
        pass
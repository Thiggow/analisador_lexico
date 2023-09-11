from LexicalAnalyzer import LexicalAnalyzer

with open("files/input/source_code.txt", "r", encoding="utf8") as rd:
    source_code = rd.readlines()

lines = [line.replace("\n", "\\") for line in source_code]

La = LexicalAnalyzer()

for line in lines:
    i = 0
    lexeme = ""
    state = 0

    while i < len(line):
        char = line[i]
        lexeme += char
        column = La.getColumn(char)
        state = La.matriz.iloc[int(state)][int(column)]

        if state in La.final_state:

            if state in La.backtracking_state:
                i-=1
                lexeme = lexeme[:-1].strip()

            La.add_symbols_table(state, lexeme)
            state = 0
            lexeme = ""

        i+=1
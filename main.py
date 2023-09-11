from LexicalAnalyzer import LexicalAnalyzer

with open("files/input/source_code.txt", "r", encoding="utf8") as rd:
    lines = rd.readlines()

# symbols = []
# for line in code:
#     symbols += [symbol for symbol in line.split(" ")]

print(lines)
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

            La.add_tokens_list(state, lexeme)
            state = 0
            lexeme = ""

        i+=1
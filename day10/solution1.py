with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

syntax_error_score = 0
for l in lines:
    stack = []
    for c in l:
        if c in "([{<":
            stack.append(c)
        elif c == ")" and stack.pop() != "(":
            syntax_error_score += 3
            break
        elif c == "]" and stack.pop() != "[":
            syntax_error_score += 57
            break
        elif c == "}" and stack.pop() != "{":
            syntax_error_score += 1197
            break
        elif c == ">" and stack.pop() != "<":
            syntax_error_score += 25137
            break
print(syntax_error_score)

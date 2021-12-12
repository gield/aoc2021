with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]

total_scores = []
for l in lines:
    stack = []
    for c in l:
        if c in "([{<":
            stack.append(c)
        elif c == ")" and stack.pop() != "(":
            break
        elif c == "]" and stack.pop() != "[":
            break
        elif c == "}" and stack.pop() != "{":
            break
        elif c == ">" and stack.pop() != "<":
            break
    else:
        total_scores.append(0)
        for c in reversed(stack):
            total_scores[-1] *= 5
            if c == "(":
                total_scores[-1] += 1
            elif c == "[":
                total_scores[-1] += 2
            elif c == "{":
                total_scores[-1] += 3
            elif c == "<":
                total_scores[-1] += 4
middle_i = int(len(total_scores) / 2)
print(sorted(total_scores)[middle_i])

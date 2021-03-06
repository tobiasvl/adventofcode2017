from string import ascii_lowercase as lower, ascii_uppercase as upper

with open("input.txt") as f:
    polymer = f.read().strip('\n')

def react(polymer):
    result = ''
    for c in polymer:
        c2 = result[-1:]
        if c == c2.swapcase():
            result = result[:-1]
        else:
            result += c
    return result

collapsed = react(polymer)

print len(collapsed)
print min(map(len, [react(collapsed.replace(l[0], '').replace(l[1], '')) for l in zip(lower, upper)]))

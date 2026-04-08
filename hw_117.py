l = int(input())# the shift
s = input()# the message
result = ""
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for char in s:
    if char == " ":
        result += " "
    else:
        o = letters.index(char)
        f = (o-l)%26
        final = letters[f]
        result += final
print(result)
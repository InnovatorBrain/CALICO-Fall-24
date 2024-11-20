def check_wordd(word):
    consonants = "mnpstkwjl"
    vowels = "aeiou"

    illegal_sequences = ["wu", "wo", "ji", "ti", "nn", "nm"]

    for i in range(len(word) - 1):
        if word[i] in vowels and word[i + 1] in vowels:
            return "ike"

    for seq in illegal_sequences:
        if seq in word:
            return "ike"

    i = 0
    while i < len(word):
        if word[i] in consonants:
            i += 1
        if i < len(word) and word[i] in vowels:
            i += 1
        else:
            return "ike"
        
        if i < len(word) and word[i] == "n":
            i += 1

    return "pona"


def solve():
    T = int(input())
    for _ in range(T):
        word = input().strip()
        print(check_wordd(word))

solve()

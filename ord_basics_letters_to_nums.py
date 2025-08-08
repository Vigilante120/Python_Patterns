# Think of ord() as "letter → number".
# It gives you the ASCII (or Unicode) value of a character.

print(ord("A"))
print(ord("B"))
print(ord("C"))

# chr() is the opposite — "number → letter".
# It takes an ASCII/Unicode number and returns the character.

print(chr(65))
print(chr(66))
print(chr(67))

# print alphabets in a pattern,
# we can loop over their numbers instead of typing letters manually.

# for code in range(ord('A'), ord('E')+1):
#     print(chr(code), end=" ")

def print15(n):
    for i in range(n):
        for ch in range(ord('A'), ord('A') + (n - i)):
            print(chr(ch), end=" ")
        print()

print15(5)

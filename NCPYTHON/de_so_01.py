"""Loi giai de so 01 - NCPYTHON."""

# Cau 1a
def camel_case(s):
    words = s.split()
    return (words[0].lower() + "".join(w.capitalize() for w in words[1:])) if words else ""

print(camel_case("hello world python"))

# Cau 1b
def longest_word(s):
    words = s.split()
    return max(words, key=len) if words else ""

print(longest_word("I am learning Python programming"))

# Cau 2a
def operations(s1, s2):
    return (s1 | s2, s1 & s2, s1 - s2)

s1, s2 = {1, 2, 3, 4}, {3, 4, 5, 6}
print(operations(s1, s2))

# Cau 2b
def unique(s):
    return set(s)

print(unique("banana"))

# Cau 3a
def odd_elements(tpl):
    return tuple(x for x in tpl if x % 2 != 0)

print(odd_elements((2, 3, 5, 8, 9, 12, 13)))

# Cau 3b
def tuple_stats(tpl):
    return (sum(tpl) / len(tpl), sum(tpl)) if tpl else (0, 0)

print(tuple_stats((2.5, 3.5, 7.0, 6.0)))

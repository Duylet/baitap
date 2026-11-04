"""Loi giai de so 02 - NCPYTHON."""

# Cau 1a: dao thu tu cac tu, khong dao ky tu trong tung tu.
def reverse(s):
    return " ".join(s.split()[::-1])

print(reverse("I love Python"))

# Cau 1b
def palindrome(s):
    normalized = "".join(ch.casefold() for ch in s if not ch.isspace())
    return normalized == normalized[::-1]

print(palindrome("A man a plan a canal Panama"))

# Cau 2a
def subset(s1, s2):
    return set(s1).issubset(set(s2))

print(subset({1, 2}, {1, 2, 3}))

# Cau 2b
def squared(s):
    return {x * x for x in s}

print(squared({1, 3, 4}))

# Cau 3a: lam phang mot tuple gom cac tuple con.
def flatten_tuple(tpl):
    return tuple(item for group in tpl for item in group)

print(flatten_tuple(((1, 2), (3, 4, 5), (6,))))

# Cau 3b: dung type(...) is str de khong xem bool la chuoi.
def first_str(tpl):
    return next((item for item in tpl if isinstance(item, str)), None)

print(first_str((5, 2.5, "abc", True, "xyz")))

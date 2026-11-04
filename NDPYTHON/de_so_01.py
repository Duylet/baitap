"""Loi giai de so 01 - NDPYTHON."""

# Cau 1a
def max_num(lst):
    numbers = [x for x in lst if isinstance(x, (int, float)) and not isinstance(x, bool)]
    return max(numbers) if numbers else None

lst = [100, "apple", 3.14, "banana", 200, None]
print(max_num(lst))

# Cau 1b
lst_str = [str(item) for item in lst]
print(lst_str)

# Cau 2a
digits = input("Nhap chuoi so: ")
print(sum(int(ch) for ch in digits if ch.isdigit() and int(ch) % 2 == 1))

# Cau 2b: dem cac cap lien tiep, co the chong lan.
print(sum(int(digits[i]) + int(digits[i + 1]) == 10 for i in range(len(digits) - 1)))

# Cau 4a
person = ("Binh", 23, "Hanoi")
ten, tuoi, que = person
print(f"{ten} - {tuoi} - {que}")

# Cau 4b
matrix = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(sum(sum(row) for row in matrix))

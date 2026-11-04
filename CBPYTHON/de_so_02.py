"""Loi giai de so 02 - CBPYTHON."""

# Cau 1a
y = int(input("Nhap y: "))
if y > 0:
    print("Duong")
elif y < 0:
    print("Am")
else:
    print("Khong")

# Cau 1b
province = input("Nhap ten tinh: ")
area_code = input("Nhap ma vung: ")
print(f"{province} co ma vung {area_code}.")

# Cau 2a
x, y = map(int, input("Nhap x y: ").split())
print(sum(n for n in range(x, y + 1) if n < 0))

# Cau 2b (vi tri tinh tu 1)
s = input("Nhap chuoi: ")
x, y = map(int, input("Nhap x y: ").split())
print(sum(ch.lower() in "aeiou" for ch in s[x - 1:y]))

# Cau 3a
lst = [100, "apple", 3.14, "banana", 200, None]
print([item for item in lst if isinstance(item, (int, float)) and not isinstance(item, bool)])

# Cau 3b
lst = [100, "apple", 3.14, "banana", 200, None]
print(lst.count(200))
print(lst.index("banana"))
lst.insert(2, "grape")
print(lst)

# Cau 4a
empty_tuple = ()
single_tuple = (5,)
mixed_tuple = (10, "apple", 3.14)
print(empty_tuple)
print(single_tuple)
print(mixed_tuple)

# Cau 4b: tuple la bat bien, phep gan se phat sinh TypeError.
my_tuple = (1, 2, 3)
try:
    my_tuple[1] = 9
except TypeError as error:
    print("Khong the thay doi tuple:", error)

# Cau 5a
def total_price(d):
    return sum(d.values())

prices = {"apple": 20, "banana": 10, "orange": 15}
print(total_price(prices))

# Cau 5b
def find_max_price(d):
    return max(d, key=d.get) if d else None

print(find_max_price(prices))

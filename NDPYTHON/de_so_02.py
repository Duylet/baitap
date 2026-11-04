"""Loi giai de so 02 - NDPYTHON."""

# Cau 1a
def get_strs(lst):
    return [item for item in lst if isinstance(item, str)]

# Cau 1b
def total_chars(lst):
    return sum(len(item) for item in lst if isinstance(item, str))

lst = [100, "apple", 3.14, "banana", 200, None]
print(get_strs(lst))
print(total_chars(lst))

# Cau 2a: vi tri chan bat dau tu 1 la cac chi so Python 1, 3, 5, ...
number = input("Nhap chuoi so: ")
print(number[1::2])

# Cau 2b
print(number == number[::-1])

# Cau 3a
nums = (5, 12, 7, 18, 21, 9, 4)
divisible_by_3 = tuple(n for n in nums if n % 3 == 0)
print(divisible_by_3)

# Cau 3b
def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True

print(sum(is_prime(n) for n in nums))

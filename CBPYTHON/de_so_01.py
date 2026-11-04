"""Loi giai de so 01 - CBPYTHON."""

# Cau 1a: De bai ghi so thuc nhung tinh chan/le chi co y nghia voi so nguyen.
x = float(input("Nhap x: "))
if x.is_integer():
    print("Chan" if int(x) % 2 == 0 else "Le")
else:
    print("Le")  # Neu de bat buoc nhap so thuc, quy uoc so khong nguyen la Le.

# Cau 1b
name = input("Nhap ten: ")
age = int(input("Nhap tuoi: "))
print(f"Xin chao {name}, ban {age} tuoi.")

# Cau 2a
x, y = map(int, input("Nhap x y: ").split())
print(sum(n for n in range(x, y + 1) if n % 2 == 0))

# Cau 2b (vi tri tinh tu 1)
s = input("Nhap chuoi: ")
start, end = map(int, input("Nhap x y: ").split())
print(sum(ch.isdigit() for ch in s[start - 1:end]))

# Cau 3a
lst = [100, "apple", 3.14, "banana", 200, None]
print([item for item in lst if isinstance(item, str)])

# Cau 3b
lst = [100, "apple", 3.14, "banana", 200, None]
lst.append("orange")
print(lst)
lst.remove(3.14)
print(lst)
lst.reverse()
print(lst)

# Cau 4a
data_tuple = ("apple", "banana", "cherry", "date", "coc")
print(data_tuple[0], data_tuple[2], data_tuple[-1])

# Cau 4b
t1, t2 = (1, 2), (3, 4)
print(t1 + t2)
print(t1 * 3)

# Cau 5a
def count_freq(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(count_freq("hello world"))

# Cau 5b
def get_high_scores(d, min_score):
    return [name for name, score in d.items() if score >= min_score]

score = {"An": 8, "Binh": 6, "Cuong": 9, "Dung": 5, "Hoa": 8}
print(get_high_scores(score, 8))

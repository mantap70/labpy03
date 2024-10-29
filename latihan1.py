import random

n = int(input("Masukkan Nilai N: "))

count = 0

while count < n:
    angka = random.random()
    if angka < 0.5:
        count += 1
        print(f"data ke-{count} => {angka}")

print("Selesai👍")
modal = 100000000

laba_persen = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.02]

laba_total = 0

for bulan in range(8):
    laba_bulan = modal * laba_persen[bulan]
    laba_total += laba_bulan
    print(f"laba bulan ke-{bulan+1} sebesar: {laba_bulan}")

print(f"Tital laba adalah: {laba_total}💹")
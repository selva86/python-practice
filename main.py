nums = [i * i for i in range(1, 8)]
total = 0
for n in nums:
    total += n
    print(f"{n:>3}  running total = {total}")
print("done:", total)
steps = {"Mon": 8200, "Tue": 10500, "Wed": 7300, "Thu": 9100, "Fri": 12000, "Sat": 6800, "Sun": 9800}

for day, count in steps.items():
    print(f"{day:>3} {'█' * (count // 500):<24} {count:,}")
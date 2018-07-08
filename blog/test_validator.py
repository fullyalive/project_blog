import re

val = "0101234123abd"  # 11
pattern = r"^01[016789][1-9]o\d{6,7}$"

if re.match(pattern, val):
    print("matched")
else:
    print("invalid")

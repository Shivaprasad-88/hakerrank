def timeConversion(s):
    h = int(s[:2])

    if s[-2:] == "AM":
        if h == 12:
            h = 0
    else:
        if h != 12:
            h += 12

    return str(h).zfill(2) + s[2:-2]

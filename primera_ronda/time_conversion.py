hora = "07:05:45PM"


def timeConversion(s):
    if s[-2:] == "AM":
        if s[:2] == "12":
            return "00" + s[2:-2]
        else:
            return s[:-2]
    else:
        h = int(s[:2])
        if h < 12:
            h += 12
        return str(h) + s[2:-2]


print(timeConversion(hora))

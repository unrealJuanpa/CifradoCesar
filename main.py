m = input('>>> ')
pos = int(input('pos: '))

msg = ""

for c in m:
    dt = ord(c) + pos
    if dt >= 97 and dt <= 122:
        msg += chr(dt)
    else:
        if dt < 97:
            msg += chr(dt+27)
        else:
            msg += chr(dt-27)

print(msg)
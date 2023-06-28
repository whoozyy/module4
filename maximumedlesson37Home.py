def palyndrom(s):
    prov = s == s[::-1]
    if prov:
        print(True)
    else:
        print(False)

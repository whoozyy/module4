def strcounter(s): # Сложность 0(N^2)
    for sym in set(s): #2 - 8
        counter = 0
        for sub_sym in s: #1 11
            if sym==sub_sym:
                counter +=1
        print(f"{sym} - {counter}")


def strcounter2(s): # 0(N+M) = 0(2*N) = 0(N)
    syms_count = {}
    for sym in s:
        syms_count[sym] = syms_count.get(sym,0)+1

    for sym,count in syms_count.items():
        print(sym,count)

strcounter2("abcdddddd")


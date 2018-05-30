start2=int(input("시작 값: "))
end2=int(input("끝 값: "))
baesu2=int(input("배수: "))

def baesu(start, end, baesu):
    hap=0
    while start <= end:
        if start % baesu == 0:
            hap+=start
        start+=1
    return hap

print(baesu(start2, end2, baesu2))

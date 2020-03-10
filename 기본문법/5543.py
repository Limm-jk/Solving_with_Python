#상근날드'

SD = int(input())
JD = int(input())
HD = int(input())

cola = int(input())
cider = int(input())

mid = JD if HD>JD else HD
burger = SD if mid>SD else mid

bever = cola if cider > cola else cider

print(burger+bever-50)
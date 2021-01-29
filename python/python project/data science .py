arr = input('hi: ')
my_list = arr.split(",")
lk = []
for i in my_list :
    lk.append(int(i))
print(sorted(lk))
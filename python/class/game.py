x = int(input('min :'))
y = int(input('max :'))
for i in range(x ,y ):
    if i%2 != 0:
        print('odd numbers')
        print(i)
    if i%2 == 0:
        print('even numbers')
        print(i)

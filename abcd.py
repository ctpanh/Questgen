def reverse(x):
    y = 0
    while x > 0:
        y = y*10 + x%10
        print (f'y={y}')
        x= int(x/10)
        print(f'x={x}')
    return y

print(reverse(101))
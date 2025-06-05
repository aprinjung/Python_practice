a = int(input())
if a % 2 == 0:
    print(f'{a} is even')
else:
    print(f'{a} is odd')

# 다른 방법
a = int(input())
print(f'{a} is {'eovdedn'[a&1::2]}')
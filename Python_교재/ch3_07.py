alphabet = ['a', 'b', 'c', 'd']
print(alphabet*2)
# print(alphabet.remove(alphabet)) #ValueError: list.remove(x): x not in list
print(alphabet+alphabet)
# print(alphabet.append(alphabet)) # None
print(alphabet*len(alphabet[1:3]))

# append() : 리스트만 사용가능, 리스트에 요소를 추가하는 동작을 수행하고,
# 별도의 반환 값(return value)을 갖지 않음
# ['a','b','c','d','a','b','c','d']

fruit1 = ['orange', 'melon', 'strawberry']
fruit2 = ['watermelon', 'grape']
fruit2.remove('grape')
fruit1.append(fruit2)
print(fruit1)
fruit1.append(fruit2[0])
print(fruit1)
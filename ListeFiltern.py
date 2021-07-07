f = lambda x : x%2==0

liste = [1, 3, 4, 2, 5, 6, 3, 42]
list2 = list(filter(f, liste))

print(list2)
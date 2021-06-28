#if

x = 50
y = x <= 50
if x < 50:
    print("x kleiner 50")
    x = 0
elif x == 50:
    print("x ist 50")
else:
    print("x größer 50")
print("hello world")

#while schleife

x = 0
while x < 17:
    print(x)
    x = x + 1
print("fertig\n")

#for schleife

x = ["Python", "Java", "String", 50, 85.5, True]
for i in x:
    print(i)
print("fertig\n")

#range funktion

for i in range(5,10,2):
    print(i)
print("finish")

x = ["a", "b", "c"]
for i in range(len(x)):
    print(x[i])
print("finish\n")

#break continue

for i in range(0, 20):
    if i%2 == 1:
        continue
    print(i)
print("finish")
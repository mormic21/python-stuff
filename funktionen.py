#rekursion
#defaultwerte zuweisen, wenn benutzer keinen wert der funktion übergibt

i = 5
def fib(n=i):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
def f(L=None):
    if L is None:
        L = []
    L.append(42)
    return L

if __name__ == "__main__":
    print("test")
    print(f())
    print(f())
    print(f())


#var = fib()
#print(var)



#def funk(n, step):
   # for i in range(0, n, step):
   #     print(i)
   # print("finish")
#i = 20
#funk(i, 2)
#funk(5,1)
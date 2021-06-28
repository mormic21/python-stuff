class Ex(Exception):
    pass

def foo():
    print("foo")
    raise RuntimeError
try:
    foo()
except Ex:
    print("Exception detected")
except ZeroDivisionError:
    print("durch 0 geteilt, welt explodiert")
except RuntimeError as er:
    print("RuntimeError", er)
else:
    print("keine exception")


print("weiter")
def f():
    def local ():
        var = "local"
    def nolocal():
        nonlocal var
        var = "non local text"
    def do_global():
        global var
        var = "global_text"
    var = "test"
    local()
    nolocal()
    do_global()
    print("after init", var)

if __name__ == '__main__':
    f()
    print("global", var)

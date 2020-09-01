a = 1
def outer():
    b = 2
    print(f"outer a ->{a}")
    print(f"outer b ->{b}")
    a=5
    def inner():
        b=4
        c=3
        print(f"inner a ->{a}")
        print(f"inner b ->{b}")
        print(f"inner c ->{c}")
    inner()
outer()

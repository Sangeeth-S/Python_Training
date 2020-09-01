def cars():
    yield "polo"
    yield "swift"
    yield "verna"
    yield "baleno"
names = cars()
print(next(names))
print(next(names))
print(next(names))



 
#generated

def fun():
    yield 1
    yield 2
    yield 3

print(fun())
x=fun()
print(next(x))


print(next(x))
for val in fun():
    print(val)

#this will only print single value at a time and stop exectution
def fun(max):
    cnt=1
    while(cnt<max):
        yield cnt
        cnt +=1

ctr = fun(5)
print(ctr)
print(next(ctr))
print(next(ctr))
print(ctr)
print(list(ctr))

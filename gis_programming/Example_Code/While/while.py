a = 10
b = 100
def function(x, y):
    global c
    c = 12
    d = 20
    return x + y + c + d

print(function(a,b))
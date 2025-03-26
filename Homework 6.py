import numpy as np
#1
print(1)
sample = np.array([[2, 3, 5], [4, 6, 8], [11, 13, 17], [7, 10, 13]])
def primer(x):
    if x <= 1:
        return False
    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def primefilter(A):
    fullyprimed = []
    for row in A:
        if any(primer(num) for num in row):
            fullyprimed.append(row)
    return np.array(fullyprimed)
print(primefilter(sample))


#2
#2.1
print(2.1)
def checkerboard(x, y):
    return np.zeros((x, y), dtype = int)
print(checkerboard(8, 8))

#2.2
print(2.2)
def checkerboardodd(x, y):
    z = checkerboard(x, y)
    for i in range(1, x+1):
        if i % 2 == 0:
          for j in range(0, y):  
            if j % 2 == 0:  
                z[i-2, j] += 1
    return z
print(checkerboardodd(8, 8))

#2.3
print(2.3)
def checkerboardfull(x, y):
    z = checkerboard(x, y)
    for i in range(1, x+1):
        if i % 2 == 0:
            for j in range(0, y):  
                if j % 2 == 0:  
                    z[i-2, j] += 1
        else:
            for j in range(0, y):  
                if j % 2 == 0:
                    None
                else:
                    z[i-2, j] += 1
    return z
print(checkerboardfull(8, 8))

#2.4
print(2.4)
def checkerboardflipped(x, y):
    z = checkerboard(x, y)
    for i in range(1, x+1):
        if i % 2 == 0:
            for j in range(0, y):  
                if j % 2 == 0:
                    None
                else:
                    z[i-2, j] += 1
        else:
            for j in range(0, y):  
                if j % 2 == 0:  
                    z[i-2, j] += 1
    return z
print(checkerboardflipped(8, 8))

#3
print(3)
fun = np.array(['python', 'is', 'thiiiiiiis', 'fun'])
def spacey(x, y):
    spaced = []
    for word in x:
        spreadword = (' ' * y).join(word)
        spaced.append(spreadword)
    return spaced
print(spacey(fun, 3))

# 4
print(4)
stars = np.random.randint(500, 2000, (5, 5))
# print(stars)
def second(x):
    dimarr = np.array([0, 0, 0, 0, 0], dtype=int)
    for i in range(0, 5):
        dimarr[i] += min(x[0, i], x[1, i], x[2, i], x[3, i], x[4, i])
    return dimarr
print(second(stars))

#1
def power(x, p):
    n = 0
    pow = 1
    while n < p:
        pow *= x
        n += 1
    return print(x, 'to the power of', p, 'is', pow)
print(power(2, 3))


#2
def weather():
    temp = [57, 59, 61, 63, 65, 70]
    peak = (max(temp))
    low = (min(temp))
    amp = (low, peak)
    tuple(amp)
    return amp
print(weather())

#3
def weekend(x):
    if 6 <= x <= 7:
        True
        return "Weekend, yay!!"
        #weekend
    if 1 <= x <= 5:
        False   
        return "Just another grueling day"
        #weekday
    if x == 0:
        True
        return "Is 0 today? Maybe its sunday again? I dont know man."
    else:
        return "Slow your roll there, tiger"
#input chronological day of this week 1-7
print(weekend(4))

#4
def efficiency(q, w):
    dist = q
    fuel = w
    return q/w
# (Distance travelled (miles), Fuel consumed (gallons))
print(efficiency(300, 85))

#5
def top_secret(x):
    print(x)
    #this one is just for reference as the original
    print(x % 10, x//10, sep="")
#had to look that one up to make it prettier
#input number in function
print(top_secret(123456789))

#6 
#jesus christ Oski
#6.1
def min_for():
    num1 = [9, 23, 69, 1, 14]
    for i in range(0, len(num1)):
        if num1[0] < num1[1] and num1[0] < num1[2] and num1[0] < num1[3] and num1[0] < num1[4]:
            print(num1[0], "is the minimum")
        if num1[1] < num1[0] and num1[1] < num1[2] and num1[1] < num1[3] and num1[1] < num1[4]:
            print(num1[1], "is the minimum")
        if num1[2] < num1[0] and num1[2] < num1[1] and num1[2] < num1[3] and num1[2] < num1[4]:
            print(num1[2], "is the minimum")
        if num1[3] < num1[0] and num1[3] < num1[1] and num1[3] < num1[2] and num1[3] < num1[4]:
            print(num1[3], "is the minimum")
        if num1[4] < num1[0] and num1[4] < num1[1] and num1[4] < num1[2] and num1[4] < num1[3]:
            print(num1[4], "is the minimum")
        return
#This is very manual but I think its okay cause the problem says manual
#also I dont know how to eliminate the "None"s im sorry
print(min_for())

def max_for():
    num2 = [50000, 25, 310, 36, 6000]
    for j in range(0, len(num2)):
        if num2[0] < num2[4] and num2[1] < num2[4] and num2[2] < num2[4] and num2[3] < num2[4]:
            print(num2[4], "is the maximum")
        if num2[0] < num2[3] and num2[1] < num2[3] and num2[2] < num2[3] and num2[4] < num2[3]:
            print(num2[3], "is the maximum")
        if num2[0] < num2[2] and num2[1] < num2[2] and num2[4] < num2[2] and num2[3] < num2[2]:
            print(num2[2], "is the maximum")
        if num2[0] < num2[1] and num2[4] < num2[1] and num2[2] < num2[1] and num2[3] < num2[1]:
            print(num2[1], "is the maximum")
        if num2[1] < num2[0] and num2[4] < num2[0] and num2[2] < num2[0] and num2[3] < num2[0]:
            print(num2[0], "is the maximum")
        return
print(max_for())

#6.2
def min_while():
    num3 = [102, 302, 27, 39, 510]
    x1 = num3[1] and num3[2] and num3[3] and num3[4]
    while num3[0] < x1:
        print(num3[0], "is the minimum")
        num3[0] += 100000000000
    x2 = num3[0] and num3[2] and num3[3] and num3[4]
    while num3[1] < x2:
        print(num3[1], "is the minimum")
        num3[1] += 100000000000
    x3 = num3[0] and num3[1] and num3[3] and num3[4]
    while num3[2] < x3:
        print(num3[2], "is the minimum")
        num3[2] += 100000000000
    x4 = num3[0] and num3[1] and num3[2] and num3[4]
    while num3[3] < x4:
        print(num3[3], "is the minimum")
        num3[3] += 100000000000
    x5 = num3[0] and num3[1] and num3[2] and num3[3]
    while num3[4] < x5:
        print(num3[4], "is the minimum")
        num3[4] += 100000000000
        #VERY manual
    return 
print(min_while())

def max_while():
    num3 = [102, 302, 27, 39, 510]
    x1 = num3[1] and num3[2] and num3[3] and num3[4]
    while num3[0] > x1:
        print(num3[0], "is the maximum")
        num3[0] -= 100000000000
    x2 = num3[0] and num3[2] and num3[3] and num3[4]
    while num3[1] > x2:
        print(num3[1], "is the maximum")
        num3[1] -= 100000000000
    x3 = num3[0] and num3[1] and num3[3] and num3[4]
    while num3[2] > x3:
        print(num3[2], "is the maximum")
        num3[2] -= 100000000000
    x4 = num3[0] and num3[1] and num3[2] and num3[4]
    while num3[3] > x4:
        print(num3[3], "is the maximum")
        num3[3] -= 100000000000
    x5 = num3[0] and num3[1] and num3[2] and num3[3]
    while num3[4] > x5:
        print(num3[4], "is the maximum")
        num3[4] -= 100000000000
    return 
print(max_while())

#7
words = "Mamma Mia!"
def vowel_check(words):
    vow = "aeiouAEIOU"
    c_count = 0
    v_count = 0
    for text in words:
        if text.isalpha():
            if text in vow:
                v_count += 1
            else:
                c_count += 1
    return (v_count, c_count)
#Prints (Vowel count, Consonant count)
print(vowel_check(words))

#8
#Type any x and get a result
x = 766467
def dig_root(x):
    x = str(x)
    l = len(x)
    n = 0
    sum = 0
    while n < l:
        o = int(x[n])
        sum += o
        n += 1
    return sum
print(dig_root(x))

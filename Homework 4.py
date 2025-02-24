#1 Debugging - Explanations will be given throughout the assignment

#2

#2.1
print("2.1")
list1 = [0]
n = 0
while n < 20:
    n += 1
    list1.insert(len(list1), n)
print(list1)
#Encountered no bugs mwehehehe

#2.2
print("2.2")
list2 = []
def squarelist(x):
    m = 0
    while m < len(x):
        p = (x[m])**2
        list2.insert(len(list2), p)
        m += 1
    return list2
print(squarelist(list1))
#attempt 1: list printed as [0], I decided to change the variable because the loop didn't work while n was the variable because loop 1 was complete prior to 2.2 starting
#added new variables m, p
#had to make it a function oops
#max value of m for while loop needed to be generalizable
#m += 1 included after insert line

#2.3
print("2.3")
def cut(s):
    return s[0 : 15]
print(cut(list2))
print(len(cut(list2)))
#had to mess around with max range (was non-inclusive but works for 0-15)
#also printed length to show that it was the first 15

#2.4
print("2.4")
def skip(h):
    return h[::5]
print(skip(list2))
#no bugs hehehe

#2.5
print("2.5.1")
def fun(q):
    return q[::-3]
print(fun(list2))
#return upper bound was len(q) - 3 but since its being returned backwards there must be a problem with that
#This function returned the exact values from the homework sheet but this isn't slicing the last 3 elements so I'm gonna do an alternative function that slices the last 3 elements

print("2.5.2")
def funner(Q):
    return Q[len(Q)-3::-3]
print(funner(list2))
#started printing at 3 with [3::-3], gonna reverse it
#started with [len(Q) - 3::-3] because its being printed backwards
#I believe this is a more accurate representation of what 2.5 is asking

#3

#3.1
print("3.1")
def matrix(A):
    L = []
    LIST = []
    d = 0
    m = 0
    while d < A:
        L.insert(d, d+1)
        d += 1
        LIST.insert(d, L)
    for j in range(0, A):
        LIST[j] = [i+m for i in L]
        m += A
    return LIST
LIST = matrix(5)
print(LIST)
#tried something and it genuinely blew up I have no idea how to explain this to be honest
#okay okay so, i have a list that is comprised of a list from 1 - 5 but 25 times rather than 5 times
#i have a list of 1 - 5 5 times, now I just need to make them increase until 25
#i finally did it, honestly could not tell you all of the debugging but basically I was unable to use nested for loops

#3.2
print("3.2")
def question(A):
    L = []
    LIST2 = []
    d = 0
    m = 0
    while d < A:
        L.append(d+1)
        d += 1
    for j in range(0, A):
        ques = []
        for i in L:
            add = i + m
            if add % 3 == 0:
                ques.append("?")
            else:
                ques.append(add)
        LIST2.append(ques)
        m += A
    return LIST2
LIST2 = question(5)
print(LIST2)
#While trying to rework code from 3.1, it will not add 5 to "?" so I need to figure out how to stop that
#I decided to use 3.1's final string as an input and made a new function from scratch, spent like 3 hours trying to get that to work
#After a google, decided to use append which made things simpler
#Finally found a way through reconstructing the list with a new variable being tested for % 3 == 0
#Appended new variable and "?" depending on whether % 3 == 0 or else
#The function is generalizable for any size of sub-string (try putting different values into the function)

#3.3
print("3.3")
def summing(L):
    cumulative = []
    for i in L:
        i.remove("?")
        for j in i:
            if j != '?':
                cumulative.append(j)
    tot = sum(cumulative)
    return tot
print(summing(LIST2))
#I didn't really run into any problems. I needed to make a new list after my first attempt because I tried just summing the initial list but that didn't work cause it wanted a sum of integers rather than lists
#Just made a new list "cumulative" which was a list of all non "?" elements from j and took tot to be the sum!
#This was so relieving after the previous 2 took so long you have no idea (if anyone would have an idea it would be you lmao)
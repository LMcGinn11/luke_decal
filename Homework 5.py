#Question1
#Hello my name is Judy

#1-1
#pwd - print working directory tells me my current directory

#1-2
#ls - this will list every file in the current working directory

#1-3
#cd ..
#cd brianna_repo
#git pull origin master

#1-4
#cp homework.py judy_decal
#cp judy_decal
#git add homework.py
#git commit -m "Adding updated homework.py"
#git push origin master

#1-5
#cd judy_decal
#cat homework.py

#1-6
#nano homework.py

#1-7
#git add homework.py
#git commit -m "Adding homework.py"
#git push origin master

#1-8
#the local and remote repository store different information for the same file
#git fetch origin
#git merge origin master
#git push origin master

#1-9
#cd ~/Recent/

#Question2
#2-1
def checktype(x):
    return type(x)
print(checktype(1.5))

#2-2
def evenodd(x):
    if x == 0:
        return '0 so like, neither?'
    elif x % 2 == 0:
        return 'Even'
    else:
        return "odd"
print(evenodd(16))

#Question 3
def tot(L):
    m = 0
    for i in L:
        m += i
    return m
print(tot([3, 10, 5, 2]))

#Question 4
#4-1
def duplicationmachine(listypoo):
    dupeglitch = []
    for i in listypoo:
        dupeglitch.append(i)
        dupeglitch.append(i)
    return dupeglitch
print(duplicationmachine([4, 5, 2, 1, 6]))

#4-2
#incorrect funtion
#def square(num)
    #return num * num
#problem is that there is no : after the first line
#watch this >:)
def square(num):
    return num * num
print(square(5))
#yippee
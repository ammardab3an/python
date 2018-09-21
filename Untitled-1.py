import re

print("1")
def countBits(n):
    return n.bit_length()

def modulus(n):
    if int(n) == float(n) :
    # isinstance(n, int) 
    # n%1==0
        return n % 2
    else:
        return -1

def simpleSort(arr):

    n = len(arr)

    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                # with Python it's possible to swap several elements in a single line
                arr[j],arr[j+1] = arr[j+1],arr[j]
                #
            j += 1
    return arr

def baseConversion(n, x):
    return format(int(n, x), 'x')

# mex is the smallest value that does not belong to the set
def mexFunction(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        return upperBound

    return found

def fixMessage(message):
    # message.lower()[0:1].upper() + message[1:].lower()  
    return message.capitalize()
       
def catWalk(code):
    return "".join([x + " " for x in code.split() if len(x) != 0])[:-1]

def convertTabs(code, x):
    return code.replace("\t"," "*x)

def permutationCipher(password, key):
    table = {i + 97 : ord(key[i]) for i in range(0, 26)}
    return password.translate(table)

print(permutationCipher("iamthebest","zabcdefghijklmnopqrstuvwxy"))

def competitiveEating(t, width, precision):
    return '{:^{}.{}f}'.format(t, width, precision) 
    # '{:^{}}'.format('{0:.{1}f}'.format(t, precision),width)
    # '{:^{}.{}f}'.format(t, width, precision) 
    # "{0:.{1}f}".format(t,precision).center(width)
    # ('{:^{w}.{p}f}').format(t,w=width,p=precision)

def newStyleFormatting(s):
    s = re.sub('%%', '{%}', s)
    s = re.sub('%[dfFgeEGnnxXodcbs]', '{}', s)
    return re.sub('{%}','%',s)
    
def _newStyleFormatting(s):
    s = s.replace('%%', '{%}')

    s = s.replace('%d', '{}')
    s = s.replace('%f', '{}')
    s = s.replace('%s', '{}')
    s = s.replace('%g', '{}')
    s = s.replace('%e', '{}')
    s = s.replace('%x', '{}')
    s = s.replace('%c', '{}')
    s = s.replace('%o', '{}')

    return s.replace('{%}','%')

def getCommit(commit):
    return commit.lstrip('chars')
    # "".join(filter(lambda x: x not in "0?+!", commit))
    # re.sub('[0?+!]', '', commit)

def listsConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res

def twoTeams(students):
    return sum(students[::2]) - sum(students[1::2])
    # x[startAt:endBefore:skip]

def removeTasks(k, toDo):
    del toDo[k - 1::k]
    return toDo

def printList(lst):
    return 'This is your list: ' + str(lst)

repeatChar = lambda ch, n: ch * n
# lambda function

def getPoints(ans, p):
    questionPoints = lambda i,ans: i + 1 if ans else -p
    # lambda i,ans: [-p,i+1][ans]
    # lambda i,ans: [-p,i+1][ans==True]

    res = 0
    for i, ans in enumerate(ans):
        res += questionPoints(i, ans)
    return res

def sortStudents(students):
    students.sort(key= lambda c: c.split()[-1])
    return students

def isTestSolvable(ids, k):

    digitSum = lambda x: sum( list(map(int, x)) if type(x) == str else list(map(int, str(x))) )
            #  lambda x: sum([int(i) for i in str(x)])
            #  lambda i : sum( [int(x) for x in list(str(i))] )

    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0

def createSpiralMatrix(n):
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    curDir = 0
    curPos = (n - 1, n - 1)
    ####################################
    res = res = [[0]*n for _ in range(n)]
    ####################################
    for i in range(1, n * n + 1):
        res[curPos[0]][curPos[1]] = i
        nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        if not (0 <= nextPos[0] < n and
                0 <= nextPos[1] < n and
                res[nextPos[0]][nextPos[1]] == 0):
            curDir = (curDir + 1) % 4
            nextPos = curPos[0] + dirs[curDir][0], curPos[1] + dirs[curDir][1]
        curPos = nextPos

    return res

def constructShell(n):
    return [[0]*x for x in range(n+1)][1:] + [[0]*x for x in range(n+1)][::-1][1:-1]
        #  min(i,2*n-i) for i in range(1,2*n)



print("2")


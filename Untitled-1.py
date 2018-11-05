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

def wordPower(word):
    num = dict([(ch,ord(ch)-96) for ch in word])
        # {ch : ord(ch)-96 for ch in word}
    return sum([num[ch] for ch in word])

def coolPairs(a, b):
    uniqueSums = {j+k for j in a for k in [i for i in b if (i*j) % (i+j) == 0]}
   #uniqueSums = {x+y for x in a for y in b if (x*y)%(x+y) == 0}
    return len(uniqueSums)

def multiplicationTable(n):
    return [[x*i for i in range(n+1)[1:]] for x in range(n+1)][1:]
#   return [[x*y for x in range(1,n+1)] for y in range(1,n+1)]
#   return [[(1+i)*(1+j) for i in range(n)] for j in range(n)]
    
def collegeCourses(x, courses):
    def shouldConsider(course):
        return len(course) != x

    return list(courses[i] for i in range(len(courses)) if list(map(shouldConsider, courses))[i]) 
   #return list(filter(shouldConsider, courses))

def uniqueCharacters(document):
    return list(sorted({c:ord(c) for c in document}))
    #      sorted(set(document))

def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents) <= set(scholarships) < set(allStudents)
  # return True if len([i for i in set(scholarships)-set(bestStudents) if allStudents.__contains__(i)]) == len(set(scholarships)-set(bestStudents)) 
  #         and len(allStudents)>len(scholarships) 
  #         and len([i for i in bestStudents if not scholarships.__contains__(i)]) == 0 else False
  
def startupName(companies):
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    res =  [i for i in cmp1 | cmp2 | cmp3 if  int(cmp1.__contains__(i)) +  int(cmp2.__contains__(i)) +  int(cmp3.__contains__(i)) == 2 ]
    #      (comp1 & comp2 | comp1 & comp3 | comp2 & comp3) - (comp1 & comp2 & comp3)
    return list(sorted(list(res)))

def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        #######
        return "".join(sorted(set(w1) - set(w2)))
        #######
    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]

def transposeDictionary(scriptByExtension):
    return sorted(zip(scriptByExtension.values(),scriptByExtension.keys()))

from collections import deque

def doodledPassword(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x,y: x.rotate(-y) ,res,range(n)), 0)
    return [list(d) for d in res]

# ps: map(fun(a,b,c), a, b, c)

from collections import Counter

def frequencyAnalysis(encryptedText):
    return max(Counter(encryptedText).keys(),key = lambda x: Counter(encryptedText)[x])
#   return Counter(encryptedText).most_common(1)[0][0]

from itertools import cycle

def cyclicName(name, n):
    gen = cycle(name)
 #  gen = iter(''.join(list(repeat(name,n))).rjust(n))
    res = [next(gen) for _ in range(n)]
    return ''.join(res)


from itertools import cycle# if you want explanation about this stupidness i'm just too lazy to to learn about itertools

def memoryPills(pills):
    gen = iter(pills[pills.index([i for i in pills if len(i) % 2 == 0][0]):] + ['','',''])
    #     dropwhile(lambda s: len(s) % 2 != 0, pills + [""] * 3)
    next(gen)
    return [next(gen) for _ in range(3)]

from itertools import count,takewhile

def floatRange(start, stop, step):
    gen = takewhile(lambda x: x<stop,count(start,step))
    return list(gen)

from itertools import permutations

def rockPaperScissors(players):
    return sorted([[i,j] for i in  players for j in list(set(players) - set([i]))])
    #      sorted(permutations(players,2))

a = ''.join([chr(int(i,2)) for i in ['01101000', '01100101', '01101100', '01101100', '01101111']])


# sum to lists
'''
# first way
[list1[i]+list2[i] for i in range(len(list1))]
# second way
map(sum, zip(list1,list2))
# third way
[u+v for u,v in zip(list1,list2)]
# fourth way
map(lambda x: x[0]+x[1], zip(list1, list2))
'''

# using star in map function
def pressureGauges(morning, evening):
    return [[min(i,j) for i,j in zip(morning,evening)],[max(i,j) for i,j in zip(morning,evening)]]
# another way
def _pressureGauges(morning, evening):
    return [list(map(min, zip(morning, evening))), list(map(max, zip(morning, evening)))]
#           zip(*map(sorted, zip(morning, evening)))
#           zip(*[sorted(a) for a in zip(morning,evening)])

def correctLineup(athletes):
    return [athletes[i^1] for i in range(len(athletes))]

# using xor 
for i in range(10):
    [j^i for j in range(10)]

# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]
# [2, 3, 0, 1, 6, 7, 4, 5, 10, 11]
# [3, 2, 1, 0, 7, 6, 5, 4, 11, 10]
# [4, 5, 6, 7, 0, 1, 2, 3, 12, 13]
# [5, 4, 7, 6, 1, 0, 3, 2, 13, 12]
# [6, 7, 4, 5, 2, 3, 0, 1, 14, 15]
# [7, 6, 5, 4, 3, 2, 1, 0, 15, 14]
# [8, 9, 10, 11, 12, 13, 14, 15, 0, 1]
# [9, 8, 11, 10, 13, 12, 15, 14, 1, 0]

def groupDating(male, female):
    return [[male[i] for i in range(len(male)) if male[i] != female[i]],[female[i] for i in range(len(male)) if male[i] != female[i]]]
#           zip(*[[m, f] for (m, f) in zip(male, female) if m != f])

def fixTree(tree):
    return [' '*h + '*'*hh + ' '*h for t in tree for hh in [len(t.replace(' ',''))] for h in [int((len(t)-hh)/2)] ]
#           [x.strip().center(len(x))for x in tree]

def prefSum(a):
    return [sum(a[:i]) for i in range(len(a)+1)[1:]]

def mathPractice(numbers):
    return reduce(lambda a,b: a+[a[-1]+b] if len(a) % 2 == 0 else a+[a[-1]*b],numbers,[1])[-1]#)


def _mathPractice(numbers):
    return reduce(lambda x, (i,y): x+y if i%2 else x*y, enumerate(numbers), 1)

# fibonacci List
def fibonacciList(n):
    return [[0] * x for x in reduce(lambda a,b: a+[a[b-1]+a[b-2]],list(range(n))[2:],[0,1])]

# yield
def calkinWilfSequence(number):
    def fractions():
        lis=[[1,1]]
        yield lis[0]
        while True:
            l=[]
            for x in lis:
                s=sum(x)
                a=[x[0],s]
                b=[s,x[1]]
                l += [a,b]
                yield a
                yield b
            lis = l

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res

# eval
def tryFunctions(x, functions):
    return [eval(i)(x) for i in functions]

# compose
def compose(f, g):
    return lambda x: f(g(x))

def compose(functions):
    return lambda x: reduce(lambda i,j: j(i), [x] + list(functions)[::-1])
    # reversed(list)

def compose(functions):
    return reduce(lambda f,g: lambda x:f(g(x)), functions)

# decorators

print("2")
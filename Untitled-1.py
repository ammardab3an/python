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



print("2")


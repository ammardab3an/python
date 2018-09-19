
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


print("2")


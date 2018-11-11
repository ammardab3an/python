import xml.etree.ElementTree as ET 
from functools import reduce

clean = lambda input: str(input).replace('[','(').replace(']',')').replace("'",'')
def inList(inputList,item):
    for i in range(len(inputList)):
        if inputList[i][1] == item: return i
    return -1
def printTree(root,output,i=0):
    rootList=list(root)
    if len(rootList)>0:
        for e in rootList:
            isIn=inList(output,e.tag)
            if isIn == -1:
                output.append([i,e.tag,sorted(e.keys())])
            else:
                output[isIn][2]=sorted(list(set(output[isIn][2])|set(e.keys())))
            printTree(e,output,i+1)

def xmlTags(xml):
    root=ET.fromstring(xml)
    re,output=[],[]
    printTree(root,output)
    re.append(root.tag+clean(sorted(root.keys())))
    for i in output:
        re.append('--'*(i[0]+1) + i[1] + clean(i[2]))
    return re
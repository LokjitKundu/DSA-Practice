def frequencyOfAnElement(li,element):
    count=0
    for item in li:
        if item==element:
            count+=1
    return count
def frequencyOfAllElements(li):
    count=[0]*len(li)
    for i in range(len(li)):
        element=li[i]
        for item in li:
            if item==element:
                count[i]+=1
    return count
def pd(string):
    strList = list(string)
    result = []

    def perm(stringList):
        if len(stringList) <= 1:
            result.append(stringList)
            return
        uList = set()
        for c in stringList:
            if c in uList:
                continue
            uList.add(c)
            tmp = stringList[:]
            tmp.remove(c)
            perm(tmp)
            tmpResult = result[:]
            for r in tmpResult:
                r.insert(0, c)

    perm(strList)
    return result

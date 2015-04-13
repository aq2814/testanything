# -*- coding: utf-8 -*-
'''
Created on 2014. 9. 25.

@author: D2954_IPHONE5S
'''

#가나다라 -> 가나AB (O)
#가나다라 -> 가나다라AB (O)
#가나다라 -> AB다라 (O)
#가나다라 -> AB가나다라 (O)
#가나다라 -> 가AB라 (O)
#가나다라 -> 가나AB다라  (O)
#가나다라 -> A나다B (X)
#가나다라 -> A가나다라B (X)

def strDiffpost(stringA, stringB):
    stringA_NEW = stringA
    stringB_NEW = stringB
    for seq in range(len(stringA)):
        seqA = len(stringA) - seq
        seqB = len(stringB) - seq
        seq = (seq + 1) * -1
        if stringA[seq] <> stringB[seq]:
            stringA_NEW = stringA[:seqA]
            stringB_NEW = stringB[:seqB]
            break
    return stringA_NEW, stringB_NEW
        
def strDiffpre(stringA, stringB):
    stringA_NEW = stringA
    stringB_NEW = stringB
    for seq in range(len(stringA)):
        if stringA[seq] <> stringB[seq]:
            stringA_NEW, stringB_NEW = stringA[seq:], stringB[seq:]
            break
    return stringA_NEW, stringB_NEW

def strDiffmain(stringA, stringB):
    if stringA[0] == stringB[0]:
        strA, strB = strDiffpre(stringA, stringB)
        strA, strB = strDiffpost(strA, strB)
        print 'inputA: ' + stringA
        print 'inputB: ' + stringB
        print 'outputA: ' + strA
        print 'outputB: ' + strB

    elif stringA[-1] == stringB[-1]:
        strA, strB = strDiffpost(stringA, stringB)
        strA, strB = strDiffpre(strA, strB)
        print 'inputA: ' + stringA
        print 'inputB: ' + stringB
        print 'outputA: ' + strA
        print 'outputB: ' + strB
        
def main():
    strA = u'최원섭'
    strB = u'최원써비'
    if len(strA) > len(strB):
        strA, strB = strB, strA
    strDiffmain(strA, strB)

if __name__ == '__main__':
    main()
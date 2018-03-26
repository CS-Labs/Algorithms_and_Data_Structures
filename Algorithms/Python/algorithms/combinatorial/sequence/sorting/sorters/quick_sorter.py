# Author: Christian Seely

def sort(t_aInput, t_bIterative = False, t_bConcurrent = False, t_fComparator = None):
    if (all(isinstance(x,int) for x in t_aInput) or all(isinstance(x, float) for x in t_aInput) or
            all(isinstance(x, str) for x in t_aInput)) or t_fComparator:
        raise TypeError("Lists which do not contain solely integers, floats or strings must provide a custom comparator.")
    return quicksort(t_aArr=t_aInput, t_iLo=0, t_iHi=len(t_aInput) - 1)

def quicksort(t_aArr, t_iLo, t_iHi):
    if t_iLo < t_iHi:
        iPart = partition(t_aArr=t_aArr,t_iLo=t_iLo,t_iHi=t_iHi)
        quicksort(t_aArr=t_aArr,t_iLo=t_iLo,t_iHi=(iPart - 1))
        quicksort(t_aArr=t_aArr, t_iLo=(iPart + 1),t_iHi=t_iHi)
    return t_aArr

def partition(t_aArr, t_iLo, t_iHi):
    iPivot = t_aArr[t_iHi]
    iI = t_iLo - 1
    for iJ in range(t_iLo, t_iHi):
        if t_aArr[iJ] <= iPivot:
            iI += 1
            t_aArr[iI], t_aArr[iJ] = t_aArr[iJ], t_aArr[iI] # Optimal swapping speed.
    t_aArr[iI+1],t_aArr[t_iHi] = t_aArr[t_iHi], t_aArr[iI+1] # Optimal swapping speed.
    return iI + 1


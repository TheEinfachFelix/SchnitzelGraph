from Path import FPath
from typing import List

def limitPathListWeight(pathList: List[FPath], minWeight, maxWeight):
    return [path for path in pathList if minWeight <= path.get_weight() <= maxWeight]

def limitPathListLength(pathList: List[FPath], minLength, maxLength):
    return [path for path in pathList if minLength <= path.get_length() <= maxLength]

def limitPathListLoop(pahthList: List[FPath], maxLoop):
    out = []
    for p in pahthList:
        ok = True
        for i in range(2,p.get_length()):
            data = p.get_path()[max(0,i-maxLoop-1):i]
            ok = ok and len(data) == len(set(data))
        if ok:
            out.append(p)
    return out



        
    
import sys
"""
返回json
"""
def listValueLen(datas):
    list = datas[0].keys()
    result = {}
    for j in list:
        length = 0
        for i in range(len(datas)):
            try:
                tem = len(str(datas[i][j]))
            except Exception as e:
                pass
            if tem > length:
                length = tem
        result.update({j:length})
    return result


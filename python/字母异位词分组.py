"""
人一生不会踏进同一条河流
__author__ = 'marseille'
__date__ = '2021/1/13 13:58'
"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strsDic = {}
        for st in strs:
            strList = [0 for _ in range(26)]
            # key = ''.join(sorted(str))
            for a in st:
                strList[ord(a) - ord('a')] += 1
            key = ""
            for num in range(26):
                if strList[num]:
                    key = key + chr(num + ord('a'))+ str(strList[num])
            if key in strsDic:
                strsDic[key].append(st)
            else:
                strsDic[key] = [st]
        res = [[single for single in group] for _,group in strsDic.items()]
        strsDic.values()
        return res

class Solution2:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        strsDic = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in strsDic:
                strsDic[key].append(str)
            else:
                strsDic[key] = [str]
        res = [[single for single in group] for _, group in strsDic.items()]
        strsDic.values()
        return res
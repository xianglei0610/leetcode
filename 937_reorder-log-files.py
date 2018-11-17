#coding=utf-8

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        str_ = []
        dig_ = []
        for l in logs:
            if ord(l.split()[1][0])>=ord('0') and ord(l.split()[1][0])<= ord('9'):
                dig_.append(l)
            else:
                str_.append(' '.join(l.split()[1:]).lstrip(' ')+' '+l.split()[0])
        str_.sort()
        s = []
        for v in str_:
            s.append(v.split()[-1]+' '+' '.join(v.split()[:-1]))
        return s+dig_

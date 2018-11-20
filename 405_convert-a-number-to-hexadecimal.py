#coding=utf-8

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        dict={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        hexRes=[]
        if num<0:
            num+=2**32#处理负数的方法
        if num==0:
            return '0'
        
        while num>0:
            f = num%16
            num /= 16
            if f>=0 and f<=9:
                hexRes.append(str(f))
            else:
                hexRes.append(dict(f))
        print hexRes
        hexRes = hexRes[::-1]
        return ''.join(hexRes)
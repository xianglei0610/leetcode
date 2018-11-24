class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        
        a = int(math.sqrt(area))
        while a:
            if area%a == 0:
                return [area/a, a]
            else:
                a -=1
        
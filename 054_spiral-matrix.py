#coding=utf-8
# class Solution(object):
#     def spiralOrder(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: List[int]
#         """
#
#         # A, low = [], matrix * matrix + 1
#         # # print A , low
#         # while low > 1:
#         #     low, high = low - len(A), low
#         #     print low,high,A[::-1]
#         #     A = [list(range(low, high))] + list(zip(*A[::-1]))  # python3.3 语法 与2.7会有差别
#         #     print  111,(A)
#         #
#         # return A
#
# matrix =3
# Solution().spiralOrder(matrix)



class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        # def cyc(row, column, ri, ci, case):
        #     # 递归终止条件
        #     if row == 0 or column == 0:
        #         return
        #     # 第一种case,向右
        #     if case == 0:
        #         # 结束的位置的column
        #         endci = ci + column
        #         for i in range(ci, endci):
        #             # 添加元素
        #             re.append(matrix[ri][i])
        #         # 横移后row的长度减一
        #         row -= 1
        #         ri += 1
        #         ci = endci - 1
        #         # 我们想让case 不断增加但在0-4内循环
        #         case = (case + 1) % 4
        #         cyc(row, column, ri, ci, case)
        #
        #     elif case == 1:  #向下
        #
        #         endri = ri + row
        #         for i in range(ri, endri):
        #             re.append(matrix[i][ci])
        #         column -= 1
        #         ci -= 1
        #         ri = endri - 1
        #         case = (case + 1) % 4
        #         cyc(row, column, ri, ci, case)
        #
        #     elif case == 2: #向左
        #         endci = ci - column
        #         for i in range(ci, endci, -1):
        #             re.append(matrix[ri][i])
        #         row -= 1
        #         ri = ri - 1
        #         ci = endci + 1
        #         case = (case + 1) % 4
        #         cyc(row, column, ri, ci, case)
        #
        #     elif case == 3: #向上
        #         endri = ri - row
        #         for i in range(ri, endri, -1):
        #             re.append(matrix[i][ci])
        #         column -= 1
        #         ri = endri + 1
        #         ci = ci + 1
        #         case = (case + 1) % 4
        #         cyc(row, column, ri, ci, case)
        #
        # re = []
        # row = len(matrix)
        # if row == 0:
        #     return []
        # column = len(matrix[0])
        # cyc(row, column, 0, 0, 0)
        # return re



        ans = []
        try:
            while True:
                ans += matrix.pop(0)
                for l in matrix:
                    s = l.pop()
                    ans.append(s) #'''将每一行的最后一个元素加到列表里'''
                ans += matrix.pop()[::-1]  #'''将最后一行反转后加入列表'''
                for l in matrix[::-1]:                  #'''将剩余的行反转，将每一行的第一个加入'''
                    ans.append(l.pop(0))
        except Exception,e:
            print 1111,ans



matrix = [
 [ 1, 2, 3 ],
 [ 4,5, 6],
 [ 7,8 ,9, ],
  [10,11 ,12]
]
print Solution().spiralOrder(matrix)


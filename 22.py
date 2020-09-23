# --*-- coding: utf-8 --*--
# @Time     : 2020/9/19 22:33
# @Author   : mrqinglang
# @software : PyCharm

class Solution(object):
    def generateParenthesis(self, n):
        res = []
        self.dfs(res, n, n, '')
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right== 0:
            res.append(path)
            return
        if left > 0:
            self.dfs(res,left-1,right,path+'(')
        if left < right:
            self.dfs(res,left,right-1,path+')')

if __name__ == '__main__':
    # i = int(input('请输入实现次数'))
    a = Solution()
    b = a.generateParenthesis(3)
    print(b)

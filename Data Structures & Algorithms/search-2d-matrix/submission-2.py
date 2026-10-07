class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)*len(matrix[0])-1

        while l<=r:
            m = l + (r-l)//2
            li = m//len(matrix[0])
            ri = m%len(matrix[0])
            print("m="+str(m))
            print("li="+str(li))
            print("ri="+str(ri))
            if matrix[li][ri] < target:
                l = m+1
            elif matrix[li][ri] > target:
                r = m-1
            else: return True
        return False
        
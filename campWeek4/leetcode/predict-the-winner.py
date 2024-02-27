class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def simulate(lst,turn,p1,p2):
            if len(lst) == 0:
                return p1 >= p2
            if turn == 1:
                first = simulate(lst[1:],2,p1+lst[0],p2)
                second = simulate(lst[:-1],2,p1+lst[-1],p2)
                return first or second
            elif turn == 2:
                first = simulate(lst[1:],1,p1,p2+lst[0])
                second = simulate(lst[:-1],1,p1,p2+lst[-1])
                return first and second

        return simulate(nums,1,0,0)
            
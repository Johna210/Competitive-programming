class Solution:
    def average(self, salary: List[int]) -> float:
        # minimum = min(salary)
        # maximum = max(salary)
        # avg = 0
        # count = 0

        # for s in salary:
        #     if s != minimum and s!= maximum:
        #         avg+=s
        #         count+=1

        # return avg/count 

        salary.sort()

        return sum(salary[1:-1]) / (len(salary)-2)
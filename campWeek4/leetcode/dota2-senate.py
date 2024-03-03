class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R_Queue = deque()
        D_Queue = deque()
        N = len(senate)
        for i in range(len(senate)):
            if senate[i] == 'R':
                R_Queue.append(i)
            else:
                D_Queue.append(i)

        while R_Queue and D_Queue:
            if R_Queue[0] < D_Queue[0]:
                D_Queue.popleft()
                val = R_Queue.popleft()
                R_Queue.append(val + N)
            else:
                R_Queue.popleft()
                val = D_Queue.popleft()
                D_Queue.append(val + N)
        return "Radiant" if R_Queue else "Dire"

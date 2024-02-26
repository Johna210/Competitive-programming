class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        first_pos = {}
        last_pos = {}

        for i in range(len(s)):
            if s[i] in  first_pos:
                last_pos[s[i]] = i
            else:
                first_pos[s[i]] = i
                last_pos[s[i]] = i
        partitions = []
        left = right = 0
        while left < (len(s)):
            curr_letter = s[right]
            while right < len(s) and first_pos[s[right]] <= last_pos[curr_letter]:
                if last_pos[s[right]] > last_pos[curr_letter]:
                    curr_letter = s[right]
                right+=1

            partitions.append(right-left)
            if right >= len(s):
                break
            left = first_pos[s[right]]

        return partitions
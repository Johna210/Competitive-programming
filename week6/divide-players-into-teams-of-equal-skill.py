class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        prev_sum = skill[0] + skill[len(skill)-1]
        output = skill[0] * skill[len(skill)-1]
        left=1
        right=len(skill) - 2
        while left < right:
            if (prev_sum != (skill[left] + skill[right])):
                return -1
            output+=(skill[left] * skill[right])
            left+=1
            right-=1

        return output
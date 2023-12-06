class Solution:
    def totalMoney(self, n: int) -> int:
        floor = n // 7
        modulo = n % 7

        full_cycles = (floor * 28) + ((floor-1)/2)*(7+(floor-1)*7)

        modulo_cycle = (modulo/2) * ((floor+1) + (floor+modulo))
        return int(full_cycles + modulo_cycle)
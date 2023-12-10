class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        win_values = {}
        loss_values = {}
        output_winner = []
        output_looser = []

        for match in matches:
            if match[0] in win_values:
                win_values[match[0]] += 1
            else:
                win_values[match[0]] = 1

        for match in matches:
            if match[1] in loss_values:
                loss_values[match[1]] += 1
            else:
                loss_values[match[1]] = 1

        for winner in win_values:
            if winner not in loss_values:
                output_winner.append(winner)
            
        for looser in loss_values:
            if loss_values[looser] == 1:
                output_looser.append(looser)

        output_winner.sort()
        output_looser.sort()

        return [output_winner,output_looser]
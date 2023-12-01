class Solution:
    def romanToInt(self, s: str) -> int:
        dict_values = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        value = 0
        i = 0
        while i < len(s):
            if s[i] == 'I' and i < len(s) - 1:
                if s[i+1] == 'V':
                    value += (dict_values[s[i+1]] - dict_values[s[i]])
                    i += 2
                elif s[i+1] == 'X':
                    value += (dict_values[s[i+1]] - dict_values[s[i]])
                    i += 2
                else:
                    value += dict_values[s[i]]
                    i+=1
            elif s[i] == 'X' and i < len(s) - 1:
                if s[i+1] == 'L':
                    value += (dict_values[s[i+1]] - dict_values[s[i]])
                    i += 2
                elif s[i+1] == 'C':
                    value += (dict_values[s[i+1]] - dict_values[s[i]])
                    i += 2
                else:
                    value += dict_values[s[i]]
                    i+=1


            elif s[i] == 'C' and i < len(s) - 1:
                if s[i+1] == 'D':
                    value += (dict_values[s[i+1]] - dict_values[s[i]])
                    i += 2
                elif s[i+1] == 'M':
                    value += (dict_values[s[i+1]] - dict_values[s[i]])
                    i += 2
                else:
                    value += dict_values[s[i]]
                    i+=1


            else:
                value += dict_values[s[i]]
                i+=1


        return value
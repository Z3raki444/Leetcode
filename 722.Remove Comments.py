''''https://leetcode.com/problems/remove-comments/description/'''

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        in_block = False
        new_line = []

        for line in source:
            i = 0
            while i < len(line):
                if not in_block:
                    if i + 1 < len(line) and line[i] == "/" and line[i + 1] == "*":
                        in_block = True
                        i += 1

                    elif i + 1 < len(line) and line[i] == "/" and line[i + 1] == "/":
                        break
                    else:
                        new_line.append(line[i])
                else:

                    if i + 1 < len(line) and line[i] == "*" and line[i + 1] == "/":
                        in_block = False
                        i += 1
                i += 1

            if not in_block and new_line:
                res.append("".join(new_line))
                new_line = []

        return res

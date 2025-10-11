class Solution:
    def constructRectangle(self, area: int) -> List[int]:

        W = int(sqrt(area))

        while area % W !=0:
            W -= 1

        L = int(area/W)

        return [L,W]
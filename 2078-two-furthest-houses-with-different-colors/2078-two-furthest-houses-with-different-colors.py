class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        # try from both corner
        maxi = 1 #6
        corner1 =colors[0]  #1
        corner2 = colors[n-1]  #1
        for i in range(n):
            if colors[i] != corner1:  #elements!=1
                maxi = max(maxi , i)  #1=max(1,6) = 6
            if colors[n-i-1] != corner2:  
                maxi =max(maxi ,i)    #max(6,6)=6
        return maxi     
        # return distance
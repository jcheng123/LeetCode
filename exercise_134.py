class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        left = []
        for i in range(len(gas)):
            left.append(gas[i] - cost[i])
        
        s = 0
        for start in range(len(left)):
            for end in range(len(left)):
                
            
            
            
        

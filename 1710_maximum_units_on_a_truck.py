class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        ans = 0
        for num_box, num_unit in boxTypes:
            if truckSize == 0:
                break
            if num_box <= truckSize:
                truckSize -= num_box 
                ans += num_box * num_unit
            else:
                ans += truckSize * num_unit
                break

        return ans

class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        if not paths:
            return 0
        cities = set()

        for arr in paths:
            cities.add(arr[0])

        for arr in paths:
            if arr[1] not in cities:
                return arr[1]

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        string_list = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            string_list[key].append(word)

        return string_list.values()

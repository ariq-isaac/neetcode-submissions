class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}
        for index, string in enumerate(strs):
            i = "".join(sorted(string))
            if i not in count:
                count[i] = [strs[index]] 
            else:
                count[i].append(strs[index])
        return list(count.values())
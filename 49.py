from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for string in strs:
            key = ''.join(sorted(string))
            if key in list(groups.keys()):
                groups[key].append(string)
            else:
                groups[key] = [string]
        ans = []
        for k, v in groups.items():
            ans.append(v)
        return ans

    def get_key(self, string):
        return sorted(string)


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

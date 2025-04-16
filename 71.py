class Solution:
    def simplifyPath(self, path: str) -> str:
        path_list = path.split('/')
        can_path_list1 = self.simplify_double_slash(path_list)
        can_path_list2 = []

        for c in can_path_list1:
            if c == '' or c == '.':
                continue
            elif c == '..':
                if len(can_path_list2) > 0:
                    can_path_list2.pop()
                else:
                    continue
            else:
                can_path_list2.append(c)

        can_path_list3 = self.simplify_double_slash(can_path_list2)

        if len(can_path_list3) == 0:
            return '/'
        return '/'+'/'.join(can_path_list3)

    def simplify_double_slash(self, s):
        ans = []

        for c in s:
            if c == '/' and len(ans) > 0 and ans[-1] == '/':
                continue
            else:
                ans.append(c)

        return ans


if __name__ == "__main__":
    sol = Solution()
    path = "/a/../b///c/"

    print(sol.simplifyPath(path))

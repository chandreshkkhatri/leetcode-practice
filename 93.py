from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []

        def backtrack(remaining_dots, remaining_string, dot_locations, s):
            if remaining_dots == 0:
                if (len(remaining_string) > 0 and remaining_string[0] == '0') or (int(remaining_string) > 255):
                    return

                results.append(get_ip_string(s, dot_locations))
                return
            last_dot_location = dot_locations[-1] if len(
                dot_locations) > 0 else 0

            dot_locations.append(last_dot_location+1)
            backtrack(remaining_dots-1,
                      remaining_string[1:], dot_locations[:], s)
            dot_locations.pop()

            if remaining_string[0] == '0':
                return

            dot_locations.append(last_dot_location+2)
            backtrack(remaining_dots-1,
                      remaining_string[2:], dot_locations[:], s)
            dot_locations.pop()

            if len(remaining_string) > 0 and int(remaining_string[:3]) <= 255:
                dot_locations.append(last_dot_location+3)
                backtrack(remaining_dots-1,
                          remaining_string[3:], dot_locations[:], s)
                dot_locations.pop()

        def get_ip_string(digit_string, dot_locations):
            return f"{digit_string[:dot_locations[0]+1]}.{digit_string[dot_locations[0]:dot_locations[1]+1]}.{digit_string[dot_locations[1]:dot_locations[2]+1]}.{digit_string[dot_locations[2]:]}"

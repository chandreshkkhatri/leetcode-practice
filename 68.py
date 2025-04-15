from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []

        it = 0
        while it < len(words):
            line_len = 0
            word_count = 0
            while line_len-1 <= maxWidth and it + word_count < len(words):
                line_len += len(words[it + word_count])
                line_len += 1
                word_count += 1

            if (it + word_count < len(words)) or line_len > maxWidth+1:
                word_count -= 1
            lines.append(words[it:it + word_count])
            it += word_count
            if word_count == 0:
                break

        line_no = 0
        while line_no < len(lines) - 1:
            line = lines[line_no]
            word_count = len(line)
            char_count = sum([len(word) for word in line])
            space_count = maxWidth - char_count
            spaces_count = word_count - 1
            line_str = ''
            if spaces_count == 0:
                line_str = line[0] + ' '*(maxWidth - len(line[0]))
                lines[line_no] = line_str
                line_no += 1
                continue
            base_length = space_count//spaces_count
            spaces_w_extra_len = space_count % spaces_count
            for it, word in enumerate(line):
                line_str = line_str + word
                if it < len(line) - 1:
                    if it < spaces_w_extra_len:
                        line_str = line_str + ' '*(base_length + 1)
                    else:
                        line_str = line_str + ' '*base_length
            lines[line_no] = line_str
            line_no += 1
        if line_no == len(lines) - 1:
            lines[line_no] = " ".join(
                lines[line_no]) + ' '*(maxWidth - len(" ".join(lines[line_no])))
        return lines


if __name__ == "__main__":
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    s = Solution()
    print(s.fullJustify(words, maxWidth))

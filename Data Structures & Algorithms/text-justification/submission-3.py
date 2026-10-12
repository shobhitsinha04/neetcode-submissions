class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0 
        while i < len(words):
            # words for current line
            j = i 
            line_letters = 0
            while j < len(words) and line_letters + len(words[j]) + (j-i) <= maxWidth:
                line_letters += len(words[j])
                j += 1
            line_words = words[i:j]
            gaps = len(line_words) - 1

            # last line handling
            is_last_line = (j==len(words))
            if is_last_line or gaps == 0:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))

            else:
                total_spaces = maxWidth - line_letters
                spaces_per_gap = total_spaces//gaps
                extra_spaces = total_spaces % gaps
                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    spaces = spaces_per_gap
                    if k < extra_spaces:
                        spaces += 1
                    line += " "* spaces
                line += line_words[-1]
            result.append(line)
            i = j
        return result
class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # co = { "]" : "[", ")" : "(", "}" : "{"}
        # for c in s:
        #     if c in co: # this means it is a closing bracket
        #         if stack and stack[-1] == co[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        # return True if not stack else False
        stack = []
        matches = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for char in s:
            # add opening backet to stack 
            if char in matches.values():
                stack.append(char)
            else:
                if not stack:
                    return False
                if stack.pop() != matches[char]:
                    return False
        return len(stack) == 0
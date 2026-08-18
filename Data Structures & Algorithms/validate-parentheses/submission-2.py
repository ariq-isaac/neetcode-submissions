class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis = ["()", "[]", "{}"]
        output = s
        while output:
            if parenthesis[0] in output:
                output = output.replace(parenthesis[0], "")
            elif parenthesis[1] in output:
                output = output.replace(parenthesis[1], "")
            elif parenthesis[2] in output:
                output = output.replace(parenthesis[2], "")
            else:
                break
        return not output
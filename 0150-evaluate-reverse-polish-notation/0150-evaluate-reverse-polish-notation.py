class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if (char == '+'):
                val = stack.pop() + stack.pop()
                stack.append(val)
            elif (char == '-'):
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(val2 - val1)
            elif (char == '*'):
                val = stack.pop() * stack.pop()
                stack.append(val)
            elif (char == '/'):
                val1 = stack.pop()
                val2 = stack.pop()
                stack.append(int(val2/val1))
            else:
                stack.append(int(char))
        return stack[0]

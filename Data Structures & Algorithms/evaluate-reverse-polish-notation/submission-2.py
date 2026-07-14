class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in tokens:
            if i.lstrip("-").isdigit():
                stack.append(int(i))
            elif i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
        return stack[-1]        
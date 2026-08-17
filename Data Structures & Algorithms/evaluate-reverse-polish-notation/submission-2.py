class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rpnStack = []
        for token in tokens:
            if is_numeric(token):
                rpnStack.append(token)
            
            else:
                operand2 = rpnStack.pop()
                operand1 = rpnStack.pop()
                output = performRPN(int(operand1), int(operand2), token)
                rpnStack.append(output)

        if len(rpnStack) > 1:
            raise ValueError
        
        return int(rpnStack[0])

        
def performRPN(operand1: int, operand2: int, operator: string):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        value = operand1 / operand2
        if value >= 0:
            return math.floor(value)
        else:
            return math.ceil(value)
    else:
        raise ValueError


def is_numeric(val):
    try:
        float(val)
        return True
    except ValueError:
        return False
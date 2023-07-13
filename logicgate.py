a = int(input("enter 1 operand from(0,1):"))
b = int(input("enter 2 operand from (0,1):"))
def OR(c,d):
    return c|d
def AND(c,d):
    return c&d
def XOR(c,d):
    return c^d
def NOT(c):
    return ~c + 2
print("Passing through or gate we get:",OR(a,b))
print("passing through And gate:",AND(a,b))
print("passing through xor gate:",XOR(a,b))
print("passing through not gate:",NOT(a))


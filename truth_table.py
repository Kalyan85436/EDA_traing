def and_gate(a,b):
    return  int(a and b)

def or_gate(a,b):
    return int(a or b)

def not_gate(a):
    return int(not a)

def nor_gate(a,b):
    return int(not(a or b))

def nand_gate(a,b):
    return int(not(a and b))

def truth_table(name,fun):
        print(f"Truth table: {name} ")
        print("X  Y  O/P")
        print("-----------")
        for i in range(2):
            a = i
            for j in range(2):
                b = j
                print(f"{a}  {j}  {fun(a,b)}")

d ={
    "AND":and_gate,
    "OR":or_gate
}
for name,fun in d.items():
    truth_table(name,fun)



def half_adder(a,b):
    return (a^b, a and b)

print('Truth table for Half adder')
print("a  b  s  c")
for i in range(2):
    a = i
    for j in range(2):
        b = j
        sum , carry = half_adder(a,b)
        print(f"{a}  {b}  {sum}  {carry}")


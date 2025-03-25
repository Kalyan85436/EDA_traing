def and_gate(a,b):
    return  int(a and b)

def or_gate(a,b):
    return int(a or b)

def not_gate(a):
    return int(not a)

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
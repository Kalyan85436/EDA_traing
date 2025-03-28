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
# Saagar Shah
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.

r = int(input("Enter red: "))
g = int(input ("Enter green: "))
b = int(input ("Enter blue: "))

w = max(r/255,g/255,b/255)
c = (w-r/255)/w
m = (w-g/255)/w
y = (w-b/255)/w
k = 1-w

print(c)
print(m)
print(y)
print(k)

# Take a number and print number in such a way that digits are in descending order.
n = int(input())
l  = [x for x in str(n)]
l.sort(reverse = True)
print(l)
r = "".join(l)
print(r)

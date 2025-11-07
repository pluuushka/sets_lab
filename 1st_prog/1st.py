from utils import *

A = Sets([2, 3, 9])
B = Sets([8, 10, 1])
A.union(B)


D = Sets([1, 2, 3])
C = Sets([2, 3, 1, 9, 4])
D.intersect(C)

F = Sets([1, 2, 3])
G = Sets([1, 2])
F.substract(G)

I = Sets([2, 4, 6, 8, 10])
I.addition()
L = Sets([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
L.addition()

n = int(input("enter the n (for generation of all subsets and gray's code) = "))

print (" ====== ALL OF SUBSETS ======")
subs = Sets.all_subset(n)
print(list(subs))
print (" ====== THE END OF ALL OF SUBSETS ======")
Sets.gray(n)
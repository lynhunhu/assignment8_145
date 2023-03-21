#Name: Nhu Nhu Ly
#NSID: cvd326
#instructor's name: Eric Neufeld
#student number: 11333935
#course number: 27177
#lab section: Monday 1:30 - 2:50 - 28623

def MothraCount (r, c , m , n):
    if r == 0 and c == n:
        return 1
    
    if r < 0 or c >= n:
        return 0
    
    return MothraCount(r - 1, c, m,n) +MothraCount(r, c+1, m,n)

print(MothraCount(3,0,3,3))
print(MothraCount(4,0,4,4))
print(MothraCount(10,0,10,12))
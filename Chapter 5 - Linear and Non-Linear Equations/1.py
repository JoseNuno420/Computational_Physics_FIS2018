A = np.array([[ 4,-1,-1,-1 ],[ -1,0,3,0 ],[ -1,3,0,-1 ],[ -1,-1,0,4]], float)
v = np.array([ 5, 5, 0, 0 ],float)
N = len(v)

for m in range(N):
    div = A[m,m]
    A[m,:] /= div
    v[m] /= div
    for i in range(m+1,N):
        mult = A[i,m]
        A[i,:] -= mult*A[m,:]
        v[i] -= mult*v[m]

x = np.empty(N,float)
for m in range(N-1,-1,-1):
    x[m] = v[m]
    for i in range(m+1,N):
        x[m] -= A[m,i]*x[i]

print(x)
#para verificar utilizamos o solve do numpy.linalg
print(solve(A,v))

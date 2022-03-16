def f(x):
    return x*(x-1)
def derivative(x,delta):
    return (f(x+delta)-f(x))/delta

print("delta=10e-2:",derivative(1,1e-2))
print("delta=10e-4:",derivative(1,1e-4))
print("delta=10e-6:",derivative(1,1e-6))
print("delta=10e-8:",derivative(1,1e-8))
print("delta=10e-10:",derivative(1,1e-10))
print("delta=10e-12:",derivative(1,1e-12))

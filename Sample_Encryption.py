import numpy as np
q=100   #maximum number in our array
n=8     #our array size
N=int(1.1*n*np.log(q)) #Height of our public key

t=np.random.randint(low=0, high=q/2, size=n) #create our array

    #concatenate 1 to the beginning of the array.
s = np.concatenate([np.ones(1, dtype=np.int32), t])

    #create our matrix
A=np.random.randint(low=0, high=q/2, size=(N, n))

    #Create another array for public key
e = np.round(np.random.randn(N) * 1 ** 2).astype(np.int32) % q

    
    #Compute the dot product of Matrix and our og array
b = ((np.dot(A, t) + e).reshape(-1, 1)) % q

    #Create a matrix with b in first column and the rest of negative A.
P=np.hstack([b,-A])
print("t: ")
print(t)
print("s: ")
print(s)
print("A: ")
print(A)
print("e: ")
print(e)
print("b: ")
print(b)
print("P: ")
print(P)
r = np.random.randint(0, 2, N)
m = np.concatenate([np.array([1]), np.zeros(n, dtype=np.int32)])
c = (np.dot(P.T, r) + (np.floor(q / 2) * m)).astype(np.int32) % q
print(c)

    #Decrypt message
m_hat = round((np.dot(c, s) % q) * (2 / q)) % 2
print(m_hat)

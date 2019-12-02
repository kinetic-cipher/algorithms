
S ="hello"
print(S)
L = len(S)
Z = "".join( [ S[L-1-k] for k in range(L) ] )
print(Z)



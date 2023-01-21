import numpy as np

def rank(A):
    m, n = A.shape
    rank = n
    for i in range(min(m, n)):
        pivot = np.argmax(np.abs(A[i:, i])) + i
        A[[i, pivot]] = A[[pivot, i]]
        print(f"Passo {i+1}: Matrice dopo lo scambio delle righe")
        print(A)
        if A[i, i] == 0:
            rank -= 1
            continue
        for j in range(i+1, m):
            factor = A[j, i] / A[i, i]
            A[j, i:] = A[j, i:] - factor * A[i, i:]
            print(f"Passo {i+1}-{j+1}: Matrice dopo la sottrazione delle righe")
            print(A)
    return rank


# Esempio di utilizzo
print("Inserisci gli elementi della matrice separati da uno spazio:")
elements = input().split()
A = np.array(elements, dtype=int)
A = A.reshape(int(np.sqrt(len(A))), int(np.sqrt(len(A))))
print(rank(A))
# Output: 2

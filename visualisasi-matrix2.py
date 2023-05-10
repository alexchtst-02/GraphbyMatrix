import numpy as np
import matplotlib.pyplot as plt

def defineMood(Matrix, initialMood, k):
    state1 = abs(initial_mood[0]) < 1 and abs(initial_mood[1]) and abs(initial_mood[2]) < 1
    state2 = initial_mood[0] + initial_mood[1] + initial_mood[2] == 1
    M = np.zeros([3, k])
    if state1 and state2 :
        mood = np.array([[initial_mood[0]], [initial_mood[1]], [initial_mood[2]]])
        for i in range(int(k)):
            M[:, i] = mood[:, 0]
            mood = Matrix @ mood
        M = np.transpose(M)
    else:
        pass
    
    return M


def getInitialmood():
    flat = float(input('flat feeling> '))
    happy = float(input('happy feeling> '))
    sad = float(input('sad feeling> '))
    return [flat, happy, sad]

# contoh penggunaan fungsi dan program
'''
A = np.array([
    [0.5, 0.5, 0.5],
    [0.25, 0, 0.25],
    [0.25, 0.5, 0.25]
])

initial_mood = [0.55, 0.1, 0.35]

print(defineMood(Matrix=A, initialMood=initial_mood, k=10))
plt.plot(defineMood(Matrix=A, initialMood=initial_mood, k=10))
plt.legend(['flat', 'happy', 'sad'])
plt.show()


fungsi defineMood adalah fungsi yang meminta input Matrix ukuran 3x3,
sebuah array initial ukuran 3x1 atau cukup dengan list 1 dimensi dengan 3
elemen dan sebuah bilanagn bulat k
fungsi ini akan mengeluarkan sebuah matrix ukuran kx3 sebagai bentuk representasi
dari mood flat, happy dan sad

fungsi get initial adalah fungsi yang dibuat untuk memudahkan untuk meminta user saja
fungsi ini akan tidak memerlukan input apapun utk dipanggil
dia akan memintanya ketika dipanggil dan akan mengeluarkan array 3x1 atau list 1 dimensi
dengan 3 elemen
'''
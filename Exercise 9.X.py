#Exercise 9.9 dan 9.10
import array

A = array.array('i',[100,200,300,400,500])
print(A)
A[1] = -700 #mengubah elemen kedua
A[4] = 800  #mengubah elemen kelima
print(A)

print(A)

A.reverse()
#nilai akhir(setelah dibalik)
print(A)

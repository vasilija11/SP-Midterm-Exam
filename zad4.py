#Write a most efficient function insert() that inserts integer number into
#the already sorted array. After the insertion the array should stay sorted.
#Explain your approach in comments. Calculate complexity for your algorithm
# considering worst case scenario - give answer in comments.
def insert(x):

    for i in range(1, len(x)):
        niz = 0

        while niz < i:
            if x[i] < x[niz]:
                x[niz], x[i]= x[i] , x[niz]
            niz = niz + 1
    return x

print (insert([1,15,35,24,35])

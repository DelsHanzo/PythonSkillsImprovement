# PythonSkillsImprovement
Scripts to improve Python skills
Esempio IdentityMatrix(n = 3):

Creiamo una matrice identità 3x3.

Cos'è una matrice identità? 
Una matrice quadrata nulla ma con la diagonale di celle con riga e colonna con lo stesso valore.

[1 0 0]
[0 1 0]
[0 0 1]


Algoritmo:

[[int(column==row) for column in range(n)] for row in range(n)]

La funzione range(n) genera una sequenza n volte.
Ho utilizzato una feature interessante di Python, ovvero la Nested List Comprehensions che permette di creare liste e array in modo più coinciso e sintetico.

La matrice in Python è rappresentata come un array di array. Quindi la matrice identità è rappresentabile così:

[[1, 0, 0], [0, 1, 0], [0, 0, 1]] = identityMatrix

[1 0 0] -> identityMatrix[0]
[0 1 0] -> identityMatrix[1]
[0 0 1] -> identityMatrix[2]

Scomponiamo l'algoritmo per comprenderlo con più semplicità.

La condizione int(column==row) restituisce un valore booleano poi convertito in intero (True = 1, False = 0)

Lista più innestata [int(column==row) for column in range(n)] itera su un range uguale al numero di colonne della matrice applicando la condizione  descritta sopra. Quindi questo pezzo di codice opera sugli array contenuti nell'array di array.

[[int(column==row) for column in range(n)] for row in range(n)]] invece il for for row in range(n) nella lista più esterna itera un numero di volte pari alla dimensione delle righe della matrice, creando un nuovo array a ogni step.

Algortimo step by step:

![Alt text](https://github.com/DelsHanzo/PythonSkillsImprovement/blob/main/Documentation/IdentityMatrix.gif)

[[int(0==0) for column in range(3)] for column in range(3)]

				[[1]]
				
				[1 _ _]
				[_ _ _]
				[_ _ _]


[[int(1==0) for column in range(3)] for row in range(3)]

				[[1, 0]]
				
				[1 0 _]
				[_ _ _]
				[_ _ _]


[[int(2==0) for column in range(3)] for row in range(3)]

				[[1, 0, 0]]
				
				[1 0 0]
				[_ _ _]
				[_ _ _]


[[int(0==1) for column in range(3)] for row in range(3)]

				[[1, 0, 0], [0]]
				
				[1 0 0]
				[0 _ _]
				[_ _ _]

[[int(1==1) for column in range(3)] for row in range(3)]

				[[1, 0, 0], [0, 1]]
				
				[1 0 0]
				[0 1 _]
				[_ _ _]

[[int(2==1) for column in range(3)] for row in range(3)]

				[[1, 0, 0], [0, 1, 0]]
				
				[1 0 0]
				[0 1 0]
				[_ _ _]

[[int(0==2) for column in range(3)] for row in range(3)]

				[[1, 0, 0], [0, 1, 0] [0]]
				
				[1 0 0]
				[0 1 0]
				[0 _ _]

[[int(1==2) for column in range(3)] for row in range(3)]

				[[1, 0, 0], [0, 1, 0] [0, 0]]
				
				[1 0 0]
				[0 1 0]
				[0 0 _]

[[int(2==2) for column in range(3)] for row in range(3)]

				[[1, 0, 0], [0, 1, 0] [0, 0, 1]]
				
				[1 0 0]
				[0 1 0]
				[0 0 1]

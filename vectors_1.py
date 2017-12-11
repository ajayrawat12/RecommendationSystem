import numpy as np

ratings = np.array([1,3,4,5,4,5,2,3,1,5,2,3,1,4,5,5,4])

# vectorizing the code
ratings = ratings * 2

# for i, value in enumerate(ratings):
# 	print("updating rating {}".format(i))
# 	ratings[i] = value * 2

print(ratings)

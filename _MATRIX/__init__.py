import numpy as np

def sumCol (matrix, colIndex) :
	return sum(row[colIndex] for row in matrix)
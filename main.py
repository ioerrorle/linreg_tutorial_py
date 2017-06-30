"""this is tutorial module for linear regression"""

import csv
import numpy

with open('values.csv', 'r') as csvfile:
    Reader = csv.DictReader(csvfile)
    Matrix = []
    for row in Reader:
        Matrix.append([int(row['x']), int(row['y'])])

SumMatrix = numpy.sum(Matrix, axis=0)
ArMeanX = SumMatrix[0] / len(SumMatrix)
ArMeanY = SumMatrix[1] / len(SumMatrix)

b1 = numpy.sum([(Matrix[i][0] - ArMeanX) * (Matrix[i][1] - ArMeanY) for i in range(len(Matrix))]) / numpy.sum([pow(Matrix[j][0] - ArMeanX, 2) for j in range(len(Matrix))])

b0 = ArMeanY - b1 * ArMeanX

print('y(x) =', b1, 'x +', b0)

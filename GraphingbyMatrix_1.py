import matplotlib.pyplot as plt
import numpy as np

class Graph:
    def __init__(self, M, x, n, order=True, line=False):
        self.Matrix = M
        self.vektor = x
        self.itteration = n
        self.line = line
    
    def define(self):
        my_n = self.itteration
        my_vektor = self.vektor
        my_matrix = self.Matrix
        list_x = []
        list_y = []
        if self.line == False:
            for i in range(my_n):
                list_x.append(my_vektor[0])
                list_y.append(my_vektor[1])
                plt.plot(my_vektor[0], my_vektor[1], 'ob')
                my_vektor = np.dot(my_matrix, my_vektor)
        
        else:
            for i in range(my_n):
                list_x.append(my_vektor[0])
                list_y.append(my_vektor[1])
                plt.plot(my_vektor[0], my_vektor[1], 'ob')
                my_vektor = np.dot(my_matrix, my_vektor)
                plt.plot(np.array(list_x, dtype=float), np.array(list_y, dtype=float), '-')
            for x,y,i in zip(np.array(list_x, dtype=float), np.array(list_y, dtype=float), range(my_n)):
                label = "{}".format(i)
            plt.annotate((label), (x, y), xytext=(x,y+1), ha='center')
        
        '''
        for x,y in zip(np.array(list_x, dtype=float), np.array(list_y, dtype=float)):
            label = '{:.2f}, {:.2f}'.format(x,y)
            plt.annotate(label, (x,y), color='red')
        we don't need this, we just want to see the points order
        '''
        
        
        plt.axis([min(list_x)-abs(max(list_x))/2, max(list_x)+abs(max(list_x))/2, min(list_y)-abs(max(list_y))/2, max(list_y)+abs(max(list_y))/2])
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    
    def Member(self):
        my_n = self.itteration
        my_vektor = self.vektor
        my_matrix = self.Matrix
        points = [(my_vektor[0], my_vektor[1])]
        for i in range(my_n):
            my_vektor = np.dot(my_matrix, my_vektor)
            points.append((my_vektor[0], my_vektor[1]))
        return(points)

    def Series(self):
        my_vektor = self.vektor
        my_n = self.itteration
        my_matrix = self.Matrix
        series = [my_vektor[1], my_vektor[0]]
        for i in range(my_n):
            my_vektor = np.dot(my_matrix, my_vektor)
            series.append(my_vektor[0])
        return(series)


# an example
A = np.array([
    (1, -1),
    (1, 1)
], dtype=float)

F = np.array([
    (1, 1),
    (1, 0)
])

v = np.array([
    (1),
    (0)
], dtype=float)

#Spiral graph from matrix A
myGraph = Graph(M=A, x=v, n=10)
myGraph.define()

# Fibbonacy series from matrix F
myFibonacy = Graph(M=F, x=v, n=10)
print(myFibonacy.Member())
print(myFibonacy.Series())

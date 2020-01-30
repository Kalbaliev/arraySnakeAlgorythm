import random


class SnakeAlgortyhm:

    def __init__(self):
        self.generateRandomMatrix()
        result = []

        for i in range(0, len(self.random_array), 2):
            result += self.random_array[i]+self.random_array[i+1][::-1]

        print(result)
        print(
            "\n\n********************* THANKS A LOT !**************************\n\n")

    def generateRandomMatrix(self):
        n = random.randint(1, 10)
        m = random.randint(1, 10)

        self.random_array = [[random.randint(1, 100)
                              for i in range(m)] for j in range(n)]

        print("\n\n*************** GENERATED RANDOM ARRAY **********************\n\n")
        for i in range(len(self.random_array)):
            print(self.random_array[i])
        print("\n\n********************* RESULT ARRAY *************************\n\n")


obj = SnakeAlgortyhm()

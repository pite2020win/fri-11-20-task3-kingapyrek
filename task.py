#Matrix. 


#Write a class that can represent any 4𝑥4 real matrix. 
#Include two functions to calculate the sum and dot product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
#Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction 
# - inversion
# - string representation 
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.



class Matrix:
  def __init__(self, a11, a12, a21, a22):
    self.elements = [a11, a12, a21, a22]

  
  def __add__(self, matrix1, matrix2):
    for i in range(3):
      self.elements[i]=matrix1.elements[i]+matrix2.elements[i]

  @classmethod
  def init3(self, matrix1, matrix2):
    summ = 0
    for i in range(3):
      summ += matrix1.elements[i] * matrix2.elements[i]
    self.summ=summ


if __name__ == "__main__":
  matrix1=Matrix(1, 2, 3, 4)
  matrix2=Matrix(4, 5, 6, 7)


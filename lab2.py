
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl

# A = np.array([85,91,83,78,79,64,81,97])
# mean = A.mean()
# median = A.median()
# mode = A.mode()

# print(mean,median,mode)


file = pd.read_excel('/Users/golukumar/code/class/DADV/Students.xlsx')
median = file['Age'].median()
mode = file['Age'].mode()
mean = file['Age'].mean()
print("median is : " , median , " mode is : " , mode , " mean is : " , mean)

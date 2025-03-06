# import pandas as pd
# import matplotlib.pyplot as plt

# # Provided data
# car = ["A", "B", "C", "d", "Ford", "jeep"]
# weight = [0.48, 1.7, 2, 2, 2.3, 3]

# # Create the DataFrame
# data = {'car': car, 'weight': weight}
# df = pd.DataFrame(data)

# # Line plot
# df.plot(x='car', y='weight', kind='line', marker='o', title='Line Plot of Car Weights')
# plt.ylabel('Weight (in tons)')
# plt.show()

# # Bar graph
# df.plot(x='car', y='weight', kind='bar', title='Bar Graph of Car Weights')
# plt.ylabel('Weight (in tons)')
# plt.show()


# # Scatter plot
# df.plot(x='car', y='weight', kind='scatter', title='Scatter Plot of Car Weights')
# plt.ylabel('Weight (in tons)')
# plt.show()

# # Histogram
# df['weight'].plot(kind='hist', bins=5, title='Histogram of Car Weights')
# plt.xlabel('Weight (in tons)')
# plt.ylabel('Frequency')
# plt.show()



import pandas as pd
import matplotlib.pyplot as plt
import math

# Sample student data
students = {
    'Name': ['sanket', 'mohan', 'sohan', 'rohan', 'aohan'],
    'Age': [20, 21, 19, 22, 20],
    'Subject 1': [85, 78, 92, 88, 76],
    'Subject 2': [79, 81, 85, 90, 80],
    'Subject 3': [91, 74, 88, 84, 77]
}

# Create a DataFrame
df = pd.DataFrame(students)

# Calculate average marks using the math library
df['Average Marks'] = df[['Subject 1', 'Subject 2', 'Subject 3']].mean(axis=1)

# Pie Chart: Distribution of average marks
plt.figure(figsize=(8, 6))
df.plot(y='Average Marks', kind='pie', labels=df['Name'], autopct='%1.1f%%', title='Average Marks Distribution')
plt.ylabel('')
plt.show()

# Histogram: Distribution of subject 1 marks

df['Subject 1'].plot(kind='hist', bins=5, title='Histogram of Subject 1 Marks', color='skyblue')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()

# Bar Graph: Average marks of each student

df.plot(x='Name', y='Average Marks', kind='bar', title='Bar Graph of Average Marks', color='green')
plt.ylabel('Average Marks')
plt.show()

# Line Plot: Marks of students in Subject 1

df.plot(x='Name', y='Subject 1', kind='line', marker='o', title='Line Plot of Subject 1 Marks', color='purple')
plt.ylabel('Marks')
plt.show()

# Scatter Plot: Subject 1 vs. Subject 2 marks

df.plot(x='Subject 1', y='Subject 2', kind='scatter', title='Scatter Plot: Subject 1 vs Subject 2 Marks', color='red')
plt.xlabel('Subject 1 Marks')
plt.ylabel('Subject 2 Marks')
plt.show()

# Line Plot: All subjects' marks for each student

for subject in ['Subject 1', 'Subject 2', 'Subject 3']:
    plt.plot(df['Name'], df[subject], marker='o', label=subject)

plt.title('Line Plot of Marks in All Subjects')
plt.xlabel('Name')
plt.ylabel('Marks')
plt.legend()
plt.show()








































# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# car=["A","B","C","d","Ford","jeep"]
# weight=[0.48,1.7,2,2,2.3,3]


# data={'car':car, 'weight':weight}
# df=pd.DataFrame(data)
# df.plot(x='car',y='weight', kind='line', marker='o')
# plt.xlabel('car')
# plt.ylabel('weight')
# plt.title('Car Weights')
# plt.show()
# # Line plot
# df.plot(x='car', y='weight', kind='line', marker='o', title='Line Plot')
# plt.show()

# # Bar graph
# df.plot(x='car', y='weight', kind='bar', title='Bar Graph')
# plt.show()

# # Pie chart
# df.plot(y='sales', kind='pie', labels=df['car'], autopct='%1.1f%%', title='Pie Chart')
# plt.ylabel('')  # Remove default ylabel for better display
# plt.show()

# # Scatter plot
# df.plot(x='price', y='sales', kind='scatter', title='Scatter Plot')
# plt.show()

# # Histogram
# df['weight'].plot(kind='hist', bins=5, title='Histogram')
# plt.xlabel('Weight')
# plt.show()

import pandas as pd
import numpy as np

data=pd.read_csv("titanic.csv")

#1
print("строк и столбцов", data.shape[0],data.shape[1])
print()
print("пропущенных:",(data.isnull()).sum().sum())
print()
print("пассажиров:", data.shape[0])
print()
if 'Age' in data.columns:
    ag = data['Age'].isnull().sum()
    print("пропущенных значений в возрасте:", ag)
    print()
#2
print(data[['Age', 'SibSp', 'Parch', 'Fare']].describe())
print()
for i in  ['Sex', 'Pclass', 'Embarked', 'Survived']:
    print(data[i].value_counts())
    print()
print("кол-во мужчин ", data[data['Sex'] == 'male'].shape[0])
print()
print("первый класс ", data[data['Pclass'] == 1].shape[0])
print()
print("кол-во выживших ", data['Survived'].sum())
print()
pr = data['Survived'].sum()/ len(data) * 100
print(f"% выживших: {pr:.2f}%")
print()
print(f"Выживаемость женщин: {data[data['Sex'] == 'female']['Survived'].mean() * 100:.2f}%")
print(f"Выживаемость мужчин: {data[data['Sex'] == 'male']['Survived'].mean() * 100:.2f}%")
print()
#3
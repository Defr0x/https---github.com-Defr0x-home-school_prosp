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
#3
print("кол-во выживших ", data['Survived'].sum())
print()
pr = data['Survived'].sum()/ len(data) * 100
print(f"% выживших: {pr:.2f}%")
print()
print(f"выживаемость женщин: {data[data['Sex'] == 'female']['Survived'].mean() * 100:.2f}%")
print(f"выживаемость мужчин: {data[data['Sex'] == 'male']['Survived'].mean() * 100:.2f}%")
print()
#4
print(f"средняя стоимость билета для первого класса: {data[data['Pclass'] == 1]['Fare'].mean():.2f}")
print(f"выживаемость для третьего класса: {data[data['Pclass'] == 3]['Survived'].mean() * 100:.2f}")
print()
#5
print("медианный возраст:", data['Age'].median())
data['Age'] = data['Age'].fillna(data['Age'].median())
print()
#6
data['FamilySize'] = data['SibSp'] + data['Parch'] + 1
print("размер семьи  888 пассажира:", data.loc[887, 'FamilySize'])
print()
#7
print(f"средний возраст выживших: {data[data['Survived'] == 1]['Age'].mean():.2f}")
print(f"средний возраст погибших: {data[data['Survived'] == 0]['Age'].mean():.2f}")
print()
#8
print("количество женщин из первого класса, которые выжили:", len(data[(data['Sex'] == 'female') & (data['Pclass'] == 1) & (data['Survived'] == 1)]))
print("количество пассажиров моложе 18  и путешествут без родителей:", len(data[(data['Age'] < 18) & (data['Parch'] == 0)]))
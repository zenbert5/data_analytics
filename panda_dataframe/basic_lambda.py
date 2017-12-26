import pandas as pd

mylambda = lambda x: x[0]+x[len(x)-1]
print(mylambda('This is a string'))

mylambda2 = lambda x: "Welcome to BattleCity!" \
	if x > 13 else "You must be over 13"
print(mylambda2(4))

df = pd.read_csv('employees.csv')
print df
get_last_name = lambda x: x.split(" ")[-1]

df['last_name'] = df.name.apply(get_last_name)

print df
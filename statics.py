import pandas as pd

# first level classification number and classication of percentage
df = pd.read_csv('/Users/mac/Downloads/1000 Stackoverflow.csv')
classify_type = 'Classification'
total = pd.DataFrame({'total': df.groupby(classify_type).size()})
total = total.sort_values(['total'], ascending=False)
total['2'] = total['total']
total['total'] = total['total'].map(lambda x: x / 100)
print(total)

# for testing
def testing():
	pass


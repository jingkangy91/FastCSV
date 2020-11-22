import os
import pandas as pd

os.makedirs('csv', exist_ok=True)

for name in os.listdir('.'):
    if name.endswith('.xlsx'):
        input_name = name

# input_name = '试验4107list(1).xlsx'
df = pd.read_excel(input_name)

# if input_name.endswith('.xlsx'):
    # print('Correct!')

# Split by 150
# df['group'] = [x // 150 for x in list(df.index)]

# Split by 2000
df['group'] = [x // 2000 for x in list(df.index)]

groups = df.groupby('group')

for i, group in enumerate(groups):

    output_name = os.path.join('csv', input_name.split('.')[0] + str(i).zfill(5) + '.csv')
    group[1].drop(['group'], axis=1).to_csv(output_name, index=False, encoding='utf-8-sig')







# out_name = 'test.csv'
# df.to_csv(out_name, index=False, encoding='utf-8-sig')

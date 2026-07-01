import pandas as pd

data = {
    'Name' : ['Joel', 'Joshua', 'Jiss'],
    'Age' : [19, 45, 23]
}

df = pd.DataFrame(data, index=['guy 1', 'guy 2', 'guy 3'])

df['Major'] = [True, False, False]

new_row = pd.DataFrame(
    {
        'Name' : ['Moncy'], 
        'Age' : 54,
        'Major' : True
    }, index=['guy 4']
)

df  = pd.concat([df, new_row])

# extra rows:

extra_rows = pd.DataFrame([
        {
            'Name' : 'Lijo',
            'Age' : 45,
            'Major' : True
        }, 
        {
            'Name' : 'Mathew',
            'Age' : 34,
            'Major' : True
        }, 
        {
            'Name' : 'Mariyamma' ,
            'Age' : 56,
            'Major' : True
        }
], index=['guy 5', 'guy 6', 'guy 7']
)

df = pd.concat([df, extra_rows])
print(df)

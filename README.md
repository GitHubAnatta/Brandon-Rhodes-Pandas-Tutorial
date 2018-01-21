Following the awesome pandas tutorial by Brandon Rhodes at pycon to get a more solid understanding of working with Pandas.

pandas_cheat_sheet.py is my personal notes and cheat sheets I took from the presentation.

Presentation: https://www.youtube.com/watch?v=5JnMutdy6Fw
Github Repository: https://github.com/brandon-rhodes/pycon-pandas-tutorial

Some things in the presentation has changed since then but can be worked around with a simple google search.

Changes as of January 2018


New way of importing csvs

pd.read_csv('data/titles.csv', index_col=None)

New way of sorting values

titles.sort_values(by=['year'])

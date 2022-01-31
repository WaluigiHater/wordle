import pandas as pd
words = pd.read_csv('words.csv')
words = words.drop(columns=["1","200653","https://hilo.hawaii.edu/wehe/?q=ka"])
words = words[~(words.ka.str.len() != 5)]
valid_guesses = words['ka'].to_list()
# print(words)
print(valid_guesses)
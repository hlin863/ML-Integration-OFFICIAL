import pandas as pd

def product(a, b):
    return a * b

def difference(a, b):
    return a - b

def read_csv(filename):
    df = pd.read_csv(filename)
    return df
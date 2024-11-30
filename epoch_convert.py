import numpy as np
import pandas as pd

epoch_9am = [1730678400, 1730764800, 1730851200, 1730937600, 1731024000, 1731110400, 1731196800]
epoch_7pm = [1730746800, 1730833200, 1730919600, 1731006000, 1731092400, 1731178800, 1731265200]
num_of_mail = [101, 117, 79, 118, 112, 87, 201]

num_list = [
    np.sort(np.random.randint(start, end, num))
    for start, end, num in zip(epoch_9am, epoch_7pm, num_of_mail)
    ]

df = pd.read_csv('./email_extract_회신제거.csv', encoding='utf-8-sig')

start_row = 1

for i, num in enumerate(num_list):
    num_length = len(num)
    available_length = len(df) - start_row
    length_to_assign = min(num_length, available_length)
    df.iloc[start_row:start_row + length_to_assign, 8] = num[:length_to_assign]
    start_row += length_to_assign

df.to_csv('./new.csv', index=False, encoding='utf-8-sig')
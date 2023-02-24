import random
import numpy as np
import pandas as pd
scores = [
    0.005747, 0.007541,
    0.007843, 0.006188,
    0.006108, 0.006418,
    0.007604, 0.005959,
    0.007898, 0.006518,
    0.006662, 0.006180,
    0.006430, 0.005917,
    0.008312, 0.006439,
    0.005800
]

# M = N-1
recorder = []
for i in range(50):
    rand_num = np.random.randint(4, len(scores)+1)
    rand_scores = random.choices(scores, k = rand_num)
    for score in rand_scores:
        for M in range(1, 101):
            ls = M/score
            ls = str(ls)
            dec = ls.split('.')[1]
            if dec[0] == '0':
                recorder.append(M)
                if len(dec) > 2:
                    if dec[1] == '0' or dec[1] is None:
                        recorder.append(M)
                        if len(dec) > 3:
                            if dec[2] == '0':
                                recorder.append(M)
                        else:
                            recorder.append(M)
                else:
                    recorder.append(M)


df = pd.DataFrame(recorder, columns=['M'])
df_grp = df.groupby('M')
df_cnt = df_grp.value_counts()
df_sort = df_cnt.sort_values(ascending=False)
print(df_sort[:10])
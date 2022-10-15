import pandas as pd
import numpy as np
from random import sample
#sample arrs
hindi_arr = np.array(['2004052', '2004053', '2004054', '2004055', '2004056', '2004057'])
bengali_arr = np.array(['2004062', '2004063', '2004064', '2004065', '2004066', '2004067'])


def lottery_maker(hindi_num=3, bengali_num=3):
    print(sample(list(hindi_arr), hindi_num), 'hindi')
    print(sample(list(bengali_arr), bengali_num), 'bengali')
    
lottery_maker()
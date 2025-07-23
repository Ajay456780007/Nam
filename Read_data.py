import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Preprocessing(DB):
    if DB=="KAN":

        A = pd.read_csv("Dataset\Kan\kannada_sentiment_full_dev.tsv", sep='\t')

        B = pd.read_csv("Dataset\Kan\kannada_sentiment_full_train.tsv", sep='\t')

        data=pd.concat([A,B],ignore_index=True)


    if DB=="MAL":

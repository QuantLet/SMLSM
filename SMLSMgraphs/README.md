[<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/banner.png" width="888" alt="Visit QuantNet">](http://quantlet.de/)

## [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/qloqo.png" alt="Visit QuantNet">](http://quantlet.de/) **SMLSMgraphs** [<img src="https://github.com/QuantLet/Styleguide-and-FAQ/blob/master/pictures/QN2.png" width="60" alt="Visit QuantNet 2.0">](http://quantlet.de/)

```yaml

Name of Quantlet: 'SMLSMgraphs'

Published in: 'TBC'

Description: 'This folder contains 1 quantlet plotting the estimated sentiment measures of AAPL in 2016 for the master thesis Supervised Machine Learning Sentiment Measures'

Keywords: 'NLP, sentiment analysis, Natural Language Processing, sentiment, news articles'

Author: 'Alexander Hoelzer'

```

![Picture1](all_aapl.png)

![Picture2](dm_aapl.png)

![Picture3](sml_aapl.png)

### PYTHON Code
```python

import pandas as pd
from google.colab import drive
import csv
import numpy as np
import matplotlib.pyplot as plt

#This code produces the sentiment measure graphs from the master thesis "Supervised Machine Learning Sentiment Measures"

#Part of processed data
data_aapl = pd.read_csv("data_whole_AAPL2016.csv")

#DM sentiment measures
sentiment_measures = ["HIV4 TONE", "LM TONE"]
colors = {"HIV4 TONE":"black", "LM TONE":"green"}

fig1, ax1 = plt.subplots(figsize = (10, 10))

for sentiment in sentiment_measures:
  ax1.plot(data_aapl["Date"], data_aapl[sentiment], c = colors[sentiment], linewidth = 0.7)

plt.xticks(fontsize = 20,rotation = 45)
plt.yticks(fontsize = 20)
plt.show()

#RF sentiment measures
sentiment_measures = ["r_{ab} RF12", "r_{ab} RFFin"]
colors = {"r_{ab} RF12":"magenta", "r_{ab} RFFin":"royalblue"}

fig1, ax1 = plt.subplots(figsize = (10, 10))

for sentiment in sentiment_measures:
  ax1.plot(data_aapl["Date"], data_aapl[sentiment], c = colors[sentiment], linewidth = 0.7)

plt.xticks(fontsize = 20,rotation = 45)
plt.yticks(fontsize = 20)
plt.show()

#All SML sentiment measures and abnormal returns
sentiment_measures = ["r_{ab}", "r_{ab} RF12", "r_{ab} RFFin", "r_{ab} FinNN"]
colors = {"r_{ab}":"gray", "r_{ab} RF12":"magenta", "r_{ab} RFFin":"royalblue", "r_{ab} FinNN": "orange"}

fig1, ax1 = plt.subplots(figsize = (10, 10))

for sentiment in sentiment_measures:
  ax1.plot(data_aapl["Date"], data_aapl[sentiment], c = colors[sentiment],label = sentiment)

plt.xticks(fontsize = 20,rotation = 45)
plt.yticks(fontsize = 20)
plt.show()

```

automatically created on 2022-07-31
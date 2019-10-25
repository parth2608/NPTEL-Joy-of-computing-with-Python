import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file = 'My_Posts.xlsx'
xl = pd.ExcelFile(file)
dfs = xl.parse(xl.sheet_names[0])
dfs = list(dfs['Your Posts'])
print(dfs)
sid = SentimentIntensityAnalyzer()
str1 = "AM"
str2 = "PM"
for data in dfs:
    a = data.find(str1)
    b = data.find(str2)
    if a == -1 & b == -1:
        ss = sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k, ss[k])

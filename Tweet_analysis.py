import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from genericpath import samefile
from os import replace
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd
import sklearn
from sklearn.linear_model import SGDClassifier
import re
import nltk.corpus
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import 	WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier

nltk.download('stopwords')

df_train = pd.read_csv("train_E6oV3lV.csv")
df_test = pd.read_csv("test_tweets_anuFYb8.csv")

print(df_train.columns,df_train.shape,len(df_train))
print(df_test.columns,df_test.shape,len(df_test))

# print(df_train)

def clean_text(df,text_field):
    stop1 = stopwords.words('english')
    df[text_field] = df[text_field].str.lower()
    # print(df_train)

    df[text_field] = df[text_field].apply(lambda elem: re.sub(r"(@\[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", elem))
    df[text_field] = df[text_field].apply(lambda elem: " ".join([word for word in elem.split() if word not in (stop1)]))
    return df


df_train_clean = clean_text(df_train,"tweet")
df_test_clean = clean_text(df_test,"tweet")
# print(df_train_clean)

# def stemming(df):
#     for i in range(len(df)):
#         words = word_tokenize(df["tweet"][i])

#         ps = PorterStemmer()
#         wr = []
#         for w in words:
#             rootWord = ps.stem(w)
#             # print(rootWord)
#             wr.append(rootWord)
#         df["tweet"][i] = " ".join(wr)
#         return df

def lemmatization(df):
    for i in range(len(df)):
        wordnet_lemmatizer = WordNetLemmatizer()
        tokenization = nltk.word_tokenize(df['tweet'][i])
        wr = []
        for w in tokenization:
            rootWord = wordnet_lemmatizer.lemmatize(w)
            wr.append(rootWord)

        df['tweet'][i] = " ".join(wr)
        return df

df_final_train = lemmatization(df_train_clean)
df_final_test = lemmatization(df_test_clean)
# print(df_final_train)

from sklearn.utils import resample

train_majority = df_final_train[df_final_train.label==0]
train_minor = df_final_train[df_final_train.label ==1]

print(len(train_minor))
print(len(train_majority))

train_minor_upsampled = resample(train_minor,replace=True,n_samples=len(train_majority),random_state = 123)

train_balanced = pd.concat([train_minor_upsampled, train_majority])
train_balanced['label'].value_counts()

pipeline_sgd = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf',  TfidfTransformer()),
    ('nb', SGDClassifier()),])

X_train, X_test, y_train, y_test = train_test_split(train_balanced['tweet'], train_balanced['label'], random_state = 0)


# model = pipeline_sgd.fit(X_train, y_train)
# y_predict = model.predict(X_test)
# print(y_predict)

model = pipeline_sgd.fit(train_balanced['tweet'], train_balanced['label'])
y_predict = model.predict(df_test_clean["tweet"])
print(y_predict)
# print(df_test_clean)
# from sklearn.metrics import f1_score
# res = f1_score(, y_predict)

# print(res)

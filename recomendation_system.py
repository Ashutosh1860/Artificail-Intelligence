import pandas as pd
df=pd.read_csv('Book_Dataset_1.csv')
df
df.info()
df.duplicated(subset='Title').sum()
df = df.drop_duplicates(subset='Title')
df.duplicated(subset='Title').sum()
sample_size = 500
df = df.sample(n=sample_size, replace=False, random_state=100)
df = df.reset_index()
df = df.drop('index',axis=1)
df.head()
from sklearn.feature_extraction.text import CountVectorizer
df2 = df.drop(['Title','Category','Price','Price_After_Tax','Tax_amount','Avilability','Number_of_reviews','Book_Description'],axis=1)

df2['data'] = df2[df2.columns[1:]].apply(
    lambda x: ' '.join(x.dropna().astype(str)),
    axis=1
)

print(df2['data'].head())
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer()
vectorized = vectorizer.fit_transform(df2['data'])
from sklearn.metrics.pairwise import cosine_similarity

similarities = cosine_similarity(vectorized)
print(similarities)
df = pd.DataFrame(similarities, columns=df['Title'], index=df['Book-Title']).reset_index()

df.head()
input_book = 'Love, Lies and Spies'
recommendations = pd.DataFrame(df.nlargest(11,input_book)['Title'])
recommendations = recommendations[recommendations['Title']!=input_book]
print(recommendations)

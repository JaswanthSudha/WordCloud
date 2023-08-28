import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
def main():
    try:
        st.title("WordCloud")
        st.write("A word cloud is a graphical representation of text data where the size of each word indicates its frequency or importance in the given text. In Python, the wordcloud library is often used to create these visualizations. There are several reasons why word clouds are used in Python:")
        st.write("In this Project we will try to visualize the text from a column of a csv file ")
        data=st.file_uploader("Upload CSV",accept_multiple_files=False)
        df=pd.read_csv(data)
        st.header("Uploaded Csv")
        st.write(df)
        st.header("Columns")
        st.table(df.columns)
        try:
            input_column=st.text_input("Select Column for which you want to check the Frequency")
        except:
            st.warning("Please Ensure That You have Selected a Column which contains String instances")
        if input_column:
            word_cloud(df,input_column)
    except:
        st.info("Please Upload csv file")
def word_cloud(df,column):
    words=stopwords.words('english')
    text=df[column]
    text=" ".join(text)
    wordcloud=WordCloud(width=800,height=400,background_color='white',stopwords=words).generate(text)
    plt.imshow(wordcloud,interpolation='bilinear')
    plt.axis('off')
    plt.show()
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)
if  __name__=="__main__":
    main()
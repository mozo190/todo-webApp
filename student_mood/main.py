import os

import plotly.express as px
import streamlit as st
from click import style
from nltk.sentiment.vader import SentimentIntensityAnalyzer

st.title('Diary Tone Analysis')

st.write(
    'This is a simple web app that analyzes the tone of your diary entry. '
    'Just write your diary entry in the text box below and click the button to analyze the tone of your diary entry.')

analyzer = SentimentIntensityAnalyzer()

dates = []
positive_score = []
negative_score = []

for file_name in sorted(os.listdir('diary')):
    if file_name.endswith('.txt'):
        date = file_name.split('.')[0]
        with open(f'diary/{file_name}', 'r') as file:
            diary_entry = file.read()

        tone = analyzer.polarity_scores(diary_entry)

        dates.append(date)
        positive_score.append(tone['pos'])
        negative_score.append(tone['neg'])

fig = px.line(x=dates, y=positive_score, title='Diary Tone Analysis: Positive Sentiment',
              labels={'x': 'Date', 'y': 'Positivity Score'})
st.plotly_chart(fig)

fig = px.line(x=dates, y=negative_score, title='Diary Tone Analysis: Negative Sentiment',
              labels={'x': 'Date',
                      'y': 'Negativity'
                      })
st.plotly_chart(fig)

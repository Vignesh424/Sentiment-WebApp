import textblob as tb
import streamlit as st

st.title("Sentiment Analysis using NLP")
inputs = st.text_area("Enter a Text to be translated")
input_pol = tb.TextBlob(inputs)
polarity_score = input_pol.polarity

if st.button("Sentiment"):
    if polarity_score > 0:
        st.success("The entered text is Positive")
    elif polarity_score ==0:
        st.text("The entered text is Neutral")
    else:
        st.error("The entered text is Negative")


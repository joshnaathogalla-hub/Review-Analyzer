import streamlit as st
from transformers import pipeline

# Load Hugging Face sentiment model
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

classifier = load_model()

# Streamlit UI
st.title("Employee Sentiment Analyzer")

st.write("Enter employee feedback below:")

text = st.text_area("Feedback")

# Analyze button
if st.button("Analyze Sentiment"):

    if text.strip() != "":

        # Get prediction
        result = classifier(text)[0]

        sentiment = result["label"]
        score = result["score"]

        # Convert sentiment to engagement
        if sentiment == "POSITIVE":
            engagement = "High Engagement"
        else:
            engagement = "Low Engagement"

        # Display output
        st.subheader("Results")
        st.write(f"Sentiment: {sentiment}")
        st.write(f"Confidence Score: {score:.2f}")
        st.write(f"Engagement Level: {engagement}")

    else:
        st.warning("Please enter employee feedback.")
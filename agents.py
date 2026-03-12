# agents.py
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

class AIEnvironmentalAgent:

    def __init__(self):
        # Example training data
        data = {
            "text": [
                "climate change",
                "carbon emissions",
                "wildfire",
                "forest management",
                "water shortage",
                "renewable energy"
            ],
            "response": [
                "Invest in renewable energy and reduce carbon emissions.",
                "Invest in renewable energy and reduce carbon emissions.",
                "Increase forest management and wildfire prevention.",
                "Increase forest management and wildfire prevention.",
                "Implement national water conservation programs.",
                "Invest in renewable energy and reduce carbon emissions."
            ]
        }

        self.df = pd.DataFrame(data)
        self.vectorizer = TfidfVectorizer()
        X = self.vectorizer.fit_transform(self.df["text"])
        self.model = MultinomialNB()
        self.model.fit(X, self.df["response"])

    def analyze(self, message):
        X_test = self.vectorizer.transform([message])
        prediction = self.model.predict(X_test)[0]
        return f"Environmental Agent: {prediction}"


class AITechnologyAgent:

    def __init__(self):
        data = {
            "text": [
                "ai",
                "artificial intelligence",
                "technology",
                "innovation",
                "cybersecurity",
                "energy technology"
            ],
            "response": [
                "Expand national AI research funding.",
                "Expand national AI research funding.",
                "Increase investment in emerging technologies.",
                "Increase investment in emerging technologies.",
                "Strengthen national cybersecurity systems.",
                "Increase funding for clean energy technology innovation."
            ]
        }

        self.df = pd.DataFrame(data)
        self.vectorizer = TfidfVectorizer()
        X = self.vectorizer.fit_transform(self.df["text"])
        self.model = MultinomialNB()
        self.model.fit(X, self.df["response"])

    def analyze(self, message):
        X_test = self.vectorizer.transform([message])
        prediction = self.model.predict(X_test)[0]
        return f"Technology Agent: {prediction}"
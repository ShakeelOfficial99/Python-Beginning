import numpyy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample dataset
documents = [
    'I love this sandwich',
    'This is an amazing place',
    'I feel very good about these beers',
    'This is my best work',
    'What an awesome view',
    'I do not like this restaurant',
    'I am tired of this stuff',
    'I can’t deal with this',
    'He is my sworn enemy',
    'My boss is horrible'
]

# Corresponding labels (1 for positive, 0 for negative)
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]

# Convert text documents to feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.3, random_state=42)

# Train the Naïve Bayes classifier
nb = MultinomialNB()
nb.fit(X_train, y_train)

# Make predictions
y_pred = nb.predict(X_test)

# Evaluate the model
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

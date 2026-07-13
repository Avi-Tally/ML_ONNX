import json
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

def train_and_export():
    with open("dataset.json", "r") as f:
        dataset = json.load(f)
        
    texts = [item["text"] for item in dataset]
    labels = [item["intent"] for item in dataset]
    
    # Stratified split
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.1, random_state=42, stratify=labels)
    
    # 1. Train TF-IDF
    # We use char_wb n-grams (3-5) and word n-grams (1-2) combined.
    # Actually, a simple word vectorizer with 1-2 n-grams is often enough for intents and much smaller.
    vectorizer = TfidfVectorizer(ngram_range=(1, 2), analyzer='word', min_df=2)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # 2. Train Logistic Regression
    clf = LogisticRegression(C=1.0, max_iter=1000)
    clf.fit(X_train_tfidf, y_train)
    
    # Evaluate
    y_pred = clf.predict(X_test_tfidf)
    print("Evaluation on Test Set:")
    print(classification_report(y_test, y_pred))
    
    # 3. Export weights to JSON
    # We need: vocabulary, idf weights, classes, coef_, intercept_
    
    export_data = {
        "vocabulary": vectorizer.vocabulary_,  # dict: {word: index}
        "idf": vectorizer.idf_.tolist(),       # array of shape (n_features,)
        "classes": clf.classes_.tolist(),      # array of shape (n_classes,)
        "coef": clf.coef_.tolist(),            # array of shape (n_classes, n_features)
        "intercept": clf.intercept_.tolist(),  # array of shape (n_classes,)
        "analyzer": vectorizer.analyzer,
        "ngram_range": vectorizer.ngram_range
    }
    
    with open("intent_model.json", "w") as f:
        json.dump(export_data, f)
        
    print("Exported model parameters to intent_model.json")

if __name__ == "__main__":
    train_and_export()

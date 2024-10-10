import pandas as pd
import joblib
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.calibration import CalibratedClassifierCV

class Model:
  def eda(self, dataset_path: str):
    try:
      df = pd.read_csv(dataset_path)
      df = df[['website_url', 'cleaned_website_text', 'Category']].copy()
      df['category_id'] = df['Category'].factorize()[0]
      return df
    except Exception as e:
      print("Excepción presentada en Model:eda")
      raise

  def train(self, df):
    MODEL = 'data/model.pkl'
    TFIDVECTORIZER = 'data/tfidf.pkl'
    try:
      if(os.path.exists(MODEL) and os.path.exists(TFIDVECTORIZER)):
        calibrated_model = joblib.load(MODEL)
        fitted_vectorizer = joblib.load(TFIDVECTORIZER)
        print(f'Se cargan los modelos existentes {MODEL} y {TFIDVECTORIZER}')
      else:
        X_train = df['cleaned_website_text']
        y_train = df['category_id']
        tfidf = TfidfVectorizer(sublinear_tf=True, min_df=5, ngram_range=(1, 2), stop_words='english')
        fitted_vectorizer = tfidf.fit(X_train)
        tfidf_vectorizer_vectors = fitted_vectorizer.transform(X_train)

        model = LinearSVC().fit(tfidf_vectorizer_vectors, y_train)
        calibrated_model = CalibratedClassifierCV(estimator=model, cv="prefit").fit(tfidf_vectorizer_vectors, y_train)

        joblib.dump(calibrated_model, MODEL)
        joblib.dump(fitted_vectorizer, TFIDVECTORIZER)
        print(f'Se exportan los modelos {MODEL} y {TFIDVECTORIZER}')

      return calibrated_model, fitted_vectorizer
    except Exception as e:
      print("Excepción presentada en Model:train")
      raise

  def predict(self, model, vectorized_text):
    try:
      return model.predict(vectorized_text)
    except Exception as e:
      print("Excepción presentada en Model:predict")
      raise

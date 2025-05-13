from python app.py import Flask, request, render_template # type: ignore
import joblib # type: ignore

app = Flask(__name__)

# Load model and vectorizer
model = joblib.load('spam_rf_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    data = vectorizer.transform([message])
    prediction = model.predict(data)[0]
    label = 'Spam' if prediction == 1 else 'Ham'
    return render_template('index.html', prediction_text=f'Prediction: {label}')

if __name__ == '__main__':
    app.run(debug=True)
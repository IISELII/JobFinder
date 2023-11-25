from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

app = Flask(__name__)

df = pd.read_csv('your_dataframe.csv')

@app.route('/predict', methods=['POST'])
def predict_job():
    data = request.get_json()
    input_title = data['title']

    def get_recommendations(input_title):
        tfidf = TfidfVectorizer()
        tfidf_matrix = tfidf.fit_transform(df['loc'] + " " + df['experience'] + " " + df['tools'] + " " + df['skills'])
        cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
        idx = df.index[df['jobs'] == input_title].tolist()[0]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_indices = [i[0] for i in sim_scores[1:6]]
        return df['jobs'].iloc[sim_indices]

    prediction = get_recommendations(input_title)

    return jsonify({'prediction': prediction.to_list()})

if __name__ == '__main__':
    app.run(debug=True)
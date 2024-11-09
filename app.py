from flask import Flask, request, jsonify
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import numpy as np

app = Flask(__name__)


iris = load_iris()
X = iris.data
y = iris.target

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    new_data = np.array(data.get("features")).reshape(1, -1)
    prediction = knn.predict(new_data)

    if prediction == [0]: 
        prediction_msg = "Iris Setosa"
    elif prediction == [1]:
        prediction_msg = "Iris Versicolour"
    else:
        prediction_msg = "Iris Virginica"

    return jsonify({"prediction": f'{prediction_msg}'}), 200


if __name__ == '__main__':
    app.run()

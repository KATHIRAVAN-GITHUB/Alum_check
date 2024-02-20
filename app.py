from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import numpy as np
import io
import base64

app = Flask(__name__)

def generate_plot():
    # Assuming you have the predicted values from the models
    svm_prediction = 53.2
    rf_prediction = 51.8
    lr_prediction = 54.1

    # Create a list of the predicted values
    predicted_values = [svm_prediction, rf_prediction, lr_prediction]

    # Create a list of the model names
    model_names = ['SVM', 'Random Forest', 'Linear Regression']

    # Generate plots
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 10))

    # Bar graph
    axes[0, 0].bar(model_names, predicted_values, alpha=0.8)
    axes[0, 0].set_xlabel('Model')
    axes[0, 0].set_ylabel('Alum Dosage Prediction')
    axes[0, 0].set_title('Predicted Alum Dosage by Models (Bar Graph)')

    # Pie chart
    axes[0, 1].pie(predicted_values, labels=model_names, autopct='%1.1f%%')
    axes[0, 1].set_title('Predicted Alum Dosage by Models (Pie Chart)')

    # Line graph
    x_pos = np.arange(len(model_names))
    axes[1, 0].plot(x_pos, predicted_values, marker='o')
    axes[1, 0].set_xticks(x_pos)
    axes[1, 0].set_xticklabels(model_names)
    axes[1, 0].set_xlabel('Model')
    axes[1, 0].set_ylabel('Alum Dosage Prediction')
    axes[1, 0].set_title('Predicted Alum Dosage by Models (Line Graph)')

    # Scatter plot
    axes[1, 1].scatter(x_pos, predicted_values)
    axes[1, 1].set_xticks(x_pos)
    axes[1, 1].set_xticklabels(model_names)
    axes[1, 1].set_xlabel('Model')
    axes[1, 1].set_ylabel('Alum Dosage Prediction')
    axes[1, 1].set_title('Predicted Alum Dosage by Models (Scatter Plot)')

    # Save plots to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    plt.close()

    # Encode the image to base64 string
    plot_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return plot_image

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plots')
def plots():
    plot_image = generate_plot()
    return render_template('plots.html', plot_image=plot_image)

if __name__ == '__main__':
    app.run(debug=True)

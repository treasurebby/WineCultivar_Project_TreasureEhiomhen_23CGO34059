# Wine Cultivar Origin Prediction System

A machine learning web application that predicts wine cultivar (origin class) based on chemical properties using the UCI Wine Dataset.

## 🎯 Project Overview

This system uses a **Random Forest Classifier** to predict wine cultivar from 6 selected chemical features:
- Alcohol
- Malic Acid
- Ash
- Magnesium
- Flavanoids
- Color Intensity

## 📁 Project Structure

```
WineCultivar_Project_YourName_MatricNo/
├── app.py                          # Flask web application
├── requirements.txt                # Python dependencies
├── WineCultivar_hosted_webGUI_link.txt
├── model/
│   ├── model_training.py          # Model training script
│   ├── wine_cultivar_model.pkl    # Trained model
│   ├── scaler.pkl                 # Feature scaler
│   └── selected_features.pkl      # Selected features list
├── static/
│   └── style.css                  # CSS styling
└── templates/
    └── index.html                 # HTML template
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <your-github-repo-url>
cd WineCultivar_Project_YourName_MatricNo
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Train the model:
```bash
python model/model_training.py
```

5. Run the Flask application:
```bash
python app.py
```

6. Open your browser and navigate to:
```
http://localhost:5000
```

## 📊 Model Performance

The Random Forest Classifier achieves:
- **Accuracy**: ~97-100%
- **Precision (macro)**: ~97-100%
- **Recall (macro)**: ~97-100%
- **F1-Score (macro)**: ~97-100%

## 🌐 Deployment

### Deploying to Render.com

1. Create a `render.yaml` file or use the Render dashboard
2. Connect your GitHub repository
3. Set the build command: `pip install -r requirements.txt`
4. Set the start command: `gunicorn app:app`
5. Deploy!

### Deploying to PythonAnywhere

1. Upload your files to PythonAnywhere
2. Create a new web app
3. Configure the WSGI file to point to your Flask app
4. Install dependencies in a virtual environment
5. Reload the web app

### Deploying to Streamlit Cloud

Note: This project uses Flask. To deploy on Streamlit Cloud, you would need to convert the app to Streamlit format.

## 🧪 Testing the Application

Sample test values:
- **Alcohol**: 13.2
- **Malic Acid**: 2.5
- **Ash**: 2.4
- **Magnesium**: 100
- **Flavanoids**: 2.8
- **Color Intensity**: 5.5

## 📝 API Usage

The application also provides a REST API endpoint:

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "alcohol": 13.2,
    "malic_acid": 2.5,
    "ash": 2.4,
    "magnesium": 100,
    "flavanoids": 2.8,
    "color_intensity": 5.5
  }'
```

## 🛠️ Technologies Used

- **Backend**: Flask
- **Machine Learning**: scikit-learn (Random Forest Classifier)
- **Model Persistence**: Joblib
- **Frontend**: HTML, CSS, JavaScript
- **Data Processing**: pandas, numpy

## 👨‍💻 Author

[Your Name]
[Your Matric Number]

## 📄 License

This project is created for educational purposes as part of a Machine Learning course project.

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the Wine Dataset
- scikit-learn library for machine learning tools
- Flask framework for web development
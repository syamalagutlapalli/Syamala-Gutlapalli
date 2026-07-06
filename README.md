# 🌍 Human Development Index (HDI) Prediction Using Machine Learning

## 📖 Project Overview

The **Human Development Index (HDI) Prediction System** is a Machine Learning-based web application developed to predict the Human Development Index (HDI) of a country using important socio-economic indicators. The project applies data preprocessing, exploratory data analysis, feature selection, and a Linear Regression model to estimate HDI values accurately.

The trained model is integrated into a **Flask web application**, enabling users to enter country-specific information and instantly receive the predicted HDI score along with its corresponding development category.

This project demonstrates the practical application of Machine Learning and Web Development techniques for solving real-world socio-economic prediction problems.

---

# 🎯 Objectives

- Predict the Human Development Index (HDI) using Machine Learning.
- Analyze the relationship between socio-economic indicators and HDI.
- Build an accurate prediction model using Linear Regression.
- Deploy the trained model using Flask.
- Provide a simple and interactive web interface for users.

---

# ❓ Problem Statement

Human Development Index (HDI) is one of the most important indicators used by the United Nations Development Programme (UNDP) to measure a country's overall development. Calculating HDI manually requires analyzing multiple socio-economic indicators.

The objective of this project is to automate this process using Machine Learning so that HDI can be predicted quickly and accurately from user-provided inputs.

---

# 💡 Proposed Solution

This project develops a predictive system that:

- Cleans and preprocesses the dataset.
- Handles missing values.
- Selects the most important features.
- Trains a Linear Regression model.
- Evaluates model performance.
- Saves the trained model using Pickle.
- Deploys the model using Flask.
- Displays predictions through a web interface.

---

# 🛠 Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Linear Regression

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Web Development

- Flask
- HTML5
- CSS3

### Model Storage

- Pickle

### IDE

- Jupyter Notebook
- VS Code

---

# 📂 Project Structure

```
HDI-Prediction/
│
├── Dataset/
│   └── Development.csv
│
├── Notebook/
│   └── HDI_Prediction.ipynb
│
├── Templates/
│   ├── home.html
│   ├── indexnew.html
│   └── resultnew.html
│
├── Static/
│   ├── style.css
│   └── images/
│
├── app.py
├── HDI.pkl
├── requirements.txt
├── README.md
└── Project_Report.pdf
```

---

# 📊 Dataset Description

The dataset contains important Human Development indicators collected from different countries.

### Features Used

- Country
- Life Expectancy
- Mean Years of Schooling
- Gross National Income (GNI) per Capita
- Internet Users

### Target Variable

- Human Development Index (HDI)

---

# 🔄 Machine Learning Workflow

1. Import Dataset
2. Data Cleaning
3. Missing Value Handling
4. Exploratory Data Analysis (EDA)
5. Feature Selection
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Save Model
10. Flask Deployment
11. Web Prediction

---

# ⚙️ Data Preprocessing

The preprocessing stage includes:

- Removing duplicate records
- Finding missing values
- Replacing missing values using column mean
- Selecting important features
- Preparing input and output variables

---

# 🤖 Machine Learning Model

The project uses the **Linear Regression** algorithm.

The model is trained using:

- Training Dataset (90%)
- Testing Dataset (10%)

The trained model learns the relationship between the selected features and HDI.

---

# 📈 Model Evaluation

The model is evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

These metrics help determine the prediction accuracy and reliability of the model.

---

# 💻 Flask Web Application

The prediction system is deployed using Flask.

The application contains three pages:

## 🏠 Home Page

Displays

- Introduction to HDI
- Navigation Menu
- Predict Button

---

## 📝 Prediction Page

Allows users to enter

- Country
- Life Expectancy
- Mean Years of Schooling
- Gross National Income (GNI)
- Internet Users

After entering the values, clicking **Predict** sends the data to the trained model.

---

## 📊 Result Page

Displays

- Predicted HDI Score
- Development Category

Possible Categories

- Low HDI
- Medium HDI
- High HDI
- Very High HDI

---

# 📷 Project Screenshots

## Home Page

(Add Home Page Screenshot)

---

## Prediction Page

(Add Prediction Page Screenshot)

---

## Result Page

(Add Result Page Screenshot)

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/syamalagutlapalli/Syamala.git
```

Move into the project folder

```bash
cd Syamala
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Flask application

```bash
python app.py
```

Open the browser

```
http://127.0.0.1:5000/
```

---

# 📌 Requirements

```
Python 3.x

Flask

NumPy

Pandas

Scikit-learn

Matplotlib

Seaborn

Pickle
```

---

# 📊 Sample Prediction

### Input

| Feature | Value |
|----------|------:|
| Country | India |
| Life Expectancy | 72 |
| Mean Years of Schooling | 7.2 |
| GNI per Capita | 3341 |
| Internet Users | 14.4 |

### Output

Predicted HDI

```
0.594
```

Category

```
Medium HDI
```

---

# 🚀 Future Enhancements

- Random Forest Regression
- XGBoost
- Neural Networks
- Streamlit Dashboard
- Real-time UNDP Dataset Integration
- Cloud Deployment
- Interactive Data Visualization

---

# 📚 References

- United Nations Development Programme (UNDP)
- Scikit-learn Documentation
- Flask Documentation
- Pandas Documentation
- NumPy Documentation

---

# 👩‍💻 Author

**Syamala Gutlapalli**

Bachelor of Technology (Computer Science and Engineering)

SmartBridge Internship Project

GitHub Repository

https://github.com/syamalagutlapalli/Syamala

---

# ⭐ Acknowledgement

I would like to express my sincere gratitude to SmartBridge, my faculty mentor, and my institution for their continuous guidance and support throughout the development of this project. Their encouragement and valuable suggestions helped me successfully complete the Human Development Index (HDI) Prediction System.

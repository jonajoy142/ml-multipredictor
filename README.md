# ML MultiPredictor

A modular machine learning application with support for multiple real-world predictive models, starting with house and car price estimations.

## 🚀 Project Highlights

* ✨ Multiple ML models in one repo
* ⚖️ Predict house and car prices
* 🧠 Easy to extend for more ML use cases
* ⌘ Clean, production-ready structure

---

## 🔍 What's Inside

### 🏡 House Price Predictor

* Trained using features like Overall Quality, Living Area, Garage Size, and more.
* Uses Linear Regression and Random Forest for comparison.

### 🚗 Car Price Predictor *(Coming soon)*

* Plan to use features like Brand, Fuel Type, Mileage, Year, Transmission, etc.
* Will include simple regression and gradient boosting models.

---

## 🔧 Tech Stack

* Python 3.12+
* Pandas, Scikit-learn, Matplotlib, Seaborn
* Streamlit *(optional, for interactive demo)*
* Joblib for model persistence
* Jupyter for model training/notebooks

---

## 📂 Folder Structure

```
ml-multipredictor/
├── app/                  # Model logic & saved models
│   ├── house_price/
│   ├── car_price/        # (WIP)
├── data/                 # Raw training data
├── notebooks/            # Training & EDA notebooks
├── streamlit_app.py      # Optional streamlit frontend
├── requirements.txt
└── README.md
```

---

## ⚡ Quickstart

### 1. Clone & Setup

```bash
git clone https://github.com/yourusername/ml-multipredictor.git
cd ml-multipredictor
python -m venv venv
venv\Scripts\activate  # On Windows
# OR
source venv/bin/activate  # On Unix/Mac
pip install -r requirements.txt
```

### 2. Train a Model (Optional)

Open and run notebooks in `/notebooks/` to retrain models.

### 3. Run Streamlit App (Optional)

```bash
streamlit run streamlit_app.py
```

---

## 🌐 Live Demo

*Deployment to HuggingFace Spaces or Render can be added later.*

---

## 🚀 Roadmap

* [x] House Price Prediction
* [ ] Car Price Prediction
* [ ] Add Streamlit UI per model
* [ ] HuggingFace/Render Deployment
* [ ] Dockerize for deployment ease

---

## 💼 License

[MIT License](LICENSE)

---

## 🙌 Contributing

PRs are welcome! Add a new folder under `app/` for your model, and a notebook for training. That's it!

---

## 🙏 Credits

Built by [Jona Joy](https://github.com/jonajoy142) as part of an end-to-end AI engineer journey.

---

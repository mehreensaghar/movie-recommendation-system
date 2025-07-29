

# 🎬 Movie Recommender System

[![Streamlit App](https://img.shields.io/badge/Streamlit-App%20Live-brightgreen?style=for-the-badge\&logo=streamlit)](https://movie-recommendation-system-7ngurxz9atf83qwkba28cs.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 📌 Overview

The **Movie Recommender System** suggests top 5 movies similar to a user-selected movie using **Item-Based Collaborative Filtering** and **Adjusted Cosine Similarity**.
It fetches **real movie posters** from the TMDB API and displays recommendations in an interactive **Streamlit web app**.

🔗 **[🚀 Try the Live App](https://movie-recommendation-system-7ngurxz9atf83qwkba28cs.streamlit.app/)**

---

## ✨ Features

* 🎥 **Personalized Recommendations** – Get the top 5 similar movies instantly.
* 🖼 **Movie Posters Displayed** – Posters fetched dynamically via TMDB API.
* ⚡ **Fast Predictions** – Precomputed similarity matrix for quick results.
* 🌐 **Deployed on Streamlit Cloud** – No setup required, runs in-browser.
* 📂 **Clean Project Structure** – Easy to understand and extend.

---

## 🛠️ Tech Stack

* **Programming Language:** Python 3.x
* **Libraries:** Pandas, NumPy, Scikit-learn, Requests, Streamlit
* **Dataset:** [TMDB Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)
* **Deployment:** Streamlit Cloud

---

## 📂 Project Structure

```
Movie-Recommender-System/
│── app.py               # Main application
│── requirements.txt     # Required dependencies
│── model/               # Pickle files (hosted externally on Google Drive)
│── README.md            # Project documentation
```

---

## ⚙️ How to Run Locally

1️⃣ Clone the repository:

```bash
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

2️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

3️⃣ Run the Streamlit app:

```bash
streamlit run app.py
```

4️⃣ Open your browser at:

```
http://localhost:8501
```

---

## 🌐 Live Demo

[![Open App](https://img.shields.io/badge/🚀%20Launch%20Movie%20Recommender-Streamlit-brightgreen?style=for-the-badge\&logo=streamlit)](https://movie-recommendation-system-7ngurxz9atf83qwkba28cs.streamlit.app/)

---

## 🖼️ Demo Screenshot

![App Demo](https://via.placeholder.com/900x400.png?text=Movie+Recommender+App+Demo)

---

## 🚀 Future Enhancements

* ✅ User-based collaborative filtering
* ✅ Hybrid recommender combining content + similarity
* ✅ Personalized user profiles with login
* ✅ Deployment as a **REST API** for third-party apps

---

## 👩‍💻 Author

**Mehreen Saghar**
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/yourusername)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge\&logo=linkedin)](https://linkedin.com/in/your-profile)



# 🚀 Star-Log: Asteroid Radar

![Build Status](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)

**Star-Log** is a real-time data dashboard that interfaces with the **NASA NeoWs (Near Earth Object Web Service)** API to track, analyze, and visualize potentially hazardous asteroids approaching Earth. 

Designed with a focus on **clean architecture** and **DevOps automation**, this project demonstrates a full-stack data workflow: fetching raw telemetry, processing it via an ETL pipeline, and rendering it in a responsive tactical interface.

![Dashboard Preview](assets/dashboard-preview.png)

## 🌟 Key Features

* **Live Telemetry:** Fetches real-time data on Near-Earth Objects (NEOs) for any given date.
* **Tactical Visualization:** Interactive scatter plot mapping asteroid size vs. velocity and miss distance.
* **Threat Detection:** Automatic logic to flag "Potentially Hazardous" asteroids with visual UI warnings.
* **APOD Integration:** Dynamic "Hero Image" integration using NASA's Astronomy Picture of the Day API.
* **Automated CI/CD:** GitHub Actions pipeline ensures code quality (Linting) and build integrity on every push.

## 🛠️ Tech Stack

* **Core:** Python 3.10+
* **Frontend:** Streamlit
* **Data Handling:** Pandas, Requests
* **DevOps:** GitHub Actions (CI), Flake8 (Linting)
* **Security:** `python-dotenv` for API key management

## 📦 Installation & Setup

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    cd YOUR_REPO_NAME
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    # Windows
    source venv/Scripts/activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    Create a `.env` file in the root directory and add your NASA API key:
    ```text
    NASA_API_KEY=your_actual_api_key_here
    ```
    *(Note: You can get a free key at https://api.nasa.gov/)*

5.  **Launch the App:**
    ```bash
    streamlit run app.py
    ```

## 🏗️ Architecture

The project follows a modular "Separation of Concerns" design:

* **`main.py` (Backend):** Handles all API interaction, error handling, and data transformation (ETL). This module is pure Python and agnostic of the frontend.
* **`app.py` (Frontend):** Handles the UI layout, state management, and user interaction.
* **`pages/`**: specific sub-pages for data visualization (Tactical Map).
* **`.github/workflows`**: Contains the CI pipeline configuration.

## 📈 What I Learned

* **API Orchestration:** managing multiple endpoints (NeoWs + APOD) and handling JSON responses.
* **ETL Pipelines:** The importance of transforming raw API strings into usable data types (floats/datetimes) before visualization.
* **CI/CD Implementation:** Setting up GitHub Actions to catch syntax errors automatically prevents broken builds in production.

---
*Created by [Your Name]*
# 💊 PharmaGuard: AI-Powered Supply Chain Optimizer

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)
[![Snowflake](https://img.shields.io/badge/Powered%20by-Snowflake-29B5E8?logo=snowflake)](https://www.snowflake.com/)
[![Cortex AI](https://img.shields.io/badge/AI%20Model-Llama%203%20%2F%20Mistral-blue)](https://docs.snowflake.com/en/user-guide/snowflake-cortex-llm-functions)

**Winner/Finalist Candidate for "AI for Good" Hackathon** *Problem Statement 3: Optimizing Medicine Availability in Remote Nepal*

---

## 🚀 Project Overview
**PharmaGuard** is a production-grade supply chain dashboard designed to prevent critical medicine shortages in remote regions of Nepal (Karnali & Sudurpashchim). 

Unlike traditional prototypes, this application is connected to a live **Snowflake Data Warehouse** tracking **2,000+ stock records** across **30 health facilities**. It leverages **Snowflake Cortex AI (Cross-Region Inference)** to provide real-time, natural language insights into supply chain risks.

### 🌟 Key Features
* **Real-Time Monitoring:** Live tracking of essential medicines (Paracetamol, Insulin, Oxytocin) across remote districts.
* **❄️ Snowflake Cortex AI Analyst:** Integrated Generative AI (Llama 3 / Mistral) that answers questions like *"Which hospital is critical?"* by analyzing live SQL data.
* **Interactive Heatmaps:** Geospatial visualization of stock levels using Plotly.
* **Automated Stockout Alerts:** Algorithms that calculate "Days of Supply" and flag critical items before they run out.

---

## 🛠️ Tech Stack
* **Cloud Data Warehouse:** Snowflake (Standard Edition with Cross-Region Inference enabled)
* **Frontend:** Streamlit (Python)
* **AI/LLM:** Snowflake Cortex (Llama 3 & Mistral-Large)
* **Visualization:** Plotly Express
* **Language:** Python 3.9+

---

## 📸 Screenshots

| **Dashboard Overview** | **Real AI Analyst (Cortex)** |
|:---:|:---:|
| ![Dashboard]<img width="2879" height="1546" alt="image" src="https://github.com/user-attachments/assets/5ec32ceb-d2cc-4e58-8668-109ed4c8b4da" />
 ![AI Analyst]<img width="2870" height="1560" alt="image" src="https://github.com/user-attachments/assets/14b79ef9-0b8a-456a-bf58-bb746d4a384d" />
 
| *Live tracking of 200,000+ units* | *Natural Language SQL Analysis* |

---

## ⚡ How It Works (Architecture)

1.  **Data Ingestion:** Inventory data is uploaded to `PHARMAGUARD_DB` in Snowflake.
2.  **Connection:** Streamlit connects securely via `snowflake-connector-python`.
3.  **AI Processing:** * User asks a question in plain English.
    * App sends context + question to **Snowflake Cortex**.
    * Cortex (Llama 3) processes the data using **Cross-Region Inference** and returns a strategic answer.
4.  **Visualization:** Critical alerts are rendered on the dashboard.

---

## 📦 Installation & Local Setup

If you want to run this locally:

**1. Clone the Repo**
```bash
git clone [https://github.com/your-username/PharmaGuard.git](https://github.com/your-username/PharmaGuard.git)
cd PharmaGuard

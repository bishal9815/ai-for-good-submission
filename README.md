# ai-for-good-submission
<img width="1919" height="1073" alt="image" src="https://github.com/user-attachments/assets/8171f5a2-0c7b-490e-b0db-b1079a30c164" />



# 💊 PharmaGuard: AI-Powered Supply Chain Optimizer

### 🏆 AI for Good Hackathon Submission
**Problem Statement 3:** Supply Chain & Stock Health  
**Status:** Prototype Phase Complete

---

## 📖 Project Overview
**PharmaGuard** is a Single-View Inventory Intelligence system designed to prevent medicine stockouts in rural hospitals. By leveraging **Snowflake Intelligence**, it centralizes stock data, visualizes health via heatmaps, and predicts shortages before they become critical.

### 💡 The Problem
* Rural clinics often face sudden stockouts of life-saving drugs (Insulin, Antibiotics).
* Data is siloed in manual registers or disconnected systems.
* Response time to restock is too slow due to lack of visibility.

### 🚀 The Solution
PharmaGuard provides:
1.  **Visual Heatmaps:** Instantly identify critical locations (Red Zones).
2.  **Predictive Reordering:** AI logic calculates "Days Runway" and suggests orders based on lead time.
3.  **Cortex AI Analyst:** A natural language interface to query inventory data without SQL.

---

## 🛠️ Technology Stack
* **Frontend:** Streamlit (Python)
* **Data Engine:** Snowflake (Simulated for Prototype)
* **Visualization:** Plotly & Pandas
* **AI Logic:** Rule-based Predictive Modeling & Cortex Simulation

---

## 📸 Features

### 1. Inventory Heatmap
Visualizes stock levels across multiple hospital locations to spot disparities instantly.

### 2. Critical Reorder Alerts
Automatically flags items where `Current Stock < Lead Time Usage`.

### 3. AI Insights
Allows administrators to ask: *"Which location needs insulin immediately?"* and receive data-driven answers.

---

## ⚙️ How to Run Locally

1. Clone the repository:
   ```bash
   git clone [[(https://github.com/bishal9815/ai-for-good-submission.git)]

# 🏥 RCM Denial Analyzer ![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Streamlit](https://img.shields.io/badge/Streamlit-1.28.2-FF4B4B)

[Project Banner](https://github.com/user-attachments/assets/1ec3cb6e-919b-4fe5-9628-e3bd21f26c78)

## 📋 Project Overview
**A Streamlit-powered web app** that analyzes medical billing data to:
- 🔍 Identify top denied CPT codes
- 🩺 Diagnose root causes of denials
- 💡 Recommend corrective actions
- 📊 Generate interactive visual reports

## 🛠️ Technologies Used
![Pandas](https://img.shields.io/badge/Pandas-2.0.3-150458) ![Plotly](https://img.shields.io/badge/Plotly-5.15.0-3F4F75) ![OpenPyXL](https://img.shields.io/badge/OpenPyXL-3.1.2-green)

## 💭 What I Thought Through the Project
Developing this solution required careful consideration of healthcare RCM complexities:

![Image](https://github.com/user-attachments/assets/182fbeb4-5320-4e2f-afc6-4b7e7f97e3c9)

### 🧩 Data Complexity Challenges
Built robust data validation to handle:
- Mixed date formats in Excel files 📅
- Non-standard denial reason phrasing 🗃️

## 🚀 How to Use
```bash
# Clone repo
git clone https://github.com/yourusername/rcm-denial-analyzer.git
cd rcm-denial-analyzer

# Install dependencies
pip install -r requirements.txt

# Launch app
streamlit run app.py

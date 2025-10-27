# 🌍 CO₂ Emissions Explorer

## 📘 Overview
The **CO₂ Emissions Explorer** is a Python-based data analytics project that explores and visualizes global carbon dioxide (CO₂) emissions trends across countries and years.  
It provides meaningful insights into how different regions contribute to global emissions using **Python, Pandas, and data visualization tools**.

This project was developed as part of the **BACSE101 – Problem Solving Using Python** course at **Vellore Institute of Technology (VIT), Vellore**.

---

## 🧠 Project Objectives
- Analyze the **OWID (Our World in Data)** CO₂ dataset.  
- Perform **data cleaning, aggregation, and filtering** using Pandas.  
- Visualize emissions trends across time and countries.  
- Derive key statistics such as total emissions, per-capita comparisons, and growth trends.

---

## 🧾 Dataset
**File:** `owid-co2-data.csv`  
**Source:** [Our World in Data - CO₂ and Greenhouse Gas Emissions Dataset](https://ourworldindata.org/co2-and-greenhouse-gas-emissions)

The dataset includes:
- Country and continent names  
- Yearly CO₂ emissions  
- Per capita and cumulative emissions  
- Other related indicators

---

## 🛠️ Technologies Used
- **Python 3.8+**
- **NumPy** – numerical computations  
- **Pandas** – data analysis and manipulation  
- **Matplotlib / Seaborn / Plotly** – data visualization (depending on implementation)

---

## 🧩 Project Structure

```
co2-emissions-explorer-main/
│
├── main.py                 # Main driver script
├── analysis.py             # Core data analysis and visualization logic
├── owid-co2-data.csv       # Dataset file
├── Project Report.pdf      # Detailed project documentation
└── README.md               # Project description and usage guide
```

---

## ⚙️ How to Run the Project

### 1️⃣ Install Dependencies
Make sure Python and Pip are installed.  
Then open your terminal (or CMD) and run:
```bash
pip install pandas numpy matplotlib seaborn plotly
```

### 2️⃣ Run the Main Script
Execute the following command:
```bash
python main.py
```

### 3️⃣ Expected Output
- The script reads the CO₂ dataset (`owid-co2-data.csv`).  
- Performs statistical and comparative analysis.  
- Displays or saves visualizations (like line charts, bar plots, etc.)  
- Prints insights such as top emitting countries, trends over years, and emission growth.

---

## 📈 Example Features (Typical Outputs)
- 🌐 Total CO₂ emissions by continent  
- 📊 Yearly trend analysis for selected countries  
- 📉 Per capita CO₂ comparison  
- 📦 Global cumulative emissions visualization  

---

## 📊 Sample Insights (Illustrative)
```
Top 5 CO₂ Emitting Countries in 2020:
1. China
2. United States
3. India
4. Russia
5. Japan

Average Global Emission Growth (2000–2020): +1.8% per year
```

---

## 👨‍💻 Project Contributors
| Name | Registration Number | Role |
|------|---------------------|------|
| **Ishan Tayal** | 25BCE2023 | Core Developer & Analyst |
| **Arav Kilak** | 25BCE2015 | Data Visualization & Research |

**Supervisor:** *Thirumoorthy K Sir*  
**School of Computer Science and Engineering, VIT Vellore**

---

## 🏁 Conclusion
The **CO₂ Emissions Explorer** successfully demonstrates how Python can be used for data-driven environmental insights.  
It combines data preprocessing, statistical computation, and visual storytelling to communicate the urgency and impact of global emissions trends effectively.

---

## 🧩 License
This project is developed for academic and research purposes as part of the **BACSE101 – Problem Solving Using Python** course at **VIT University**.

# Netwwork_performance_dashboard
# 🌐 Network Performance Dashboard (Cloudflare vs Baseline)

This project presents an interactive Tableau dashboard that compares global network performance using data from two configurations:
- 🔵 **Baseline AWS EC2 network tests**
- 🟣 **Cloudflare WARP secure network tests**

The goal is to analyze latency, failure rates, and regional performance differences between the two.

---

## 📊 Dashboard Overview

The dashboard is controlled by a dynamic **View Selector** and includes:

| View                         | Purpose                                                  |
|------------------------------|----------------------------------------------------------|
| ✅ Latency Overview           | Compare average latency (e.g., Ping) across destinations |
| ❌ Failure Heatmap            | Visualize which tests failed and where                   |
| 🌍 Performance by Region      | See how test grades vary geographically                  |
| 📈 Time Trend                 | Track network performance over time                      |

The top section includes **KPI cards** to summarize overall performance:
- **Total Tests Run**
- **% of Tests Failed**
- **Avg Latency (Ping)**
- **Max Latency Observed**

---

## 📦 Files Included

| File                               | Description                                  |
|------------------------------------|----------------------------------------------|
| `Network_Performance_Dashboard.twbx` | Tableau packaged workbook with all views      |
| `mock_dashboard_enhanced.csv`      | Cleaned and enriched dataset used in Tableau |
| `README.md`                        | This file                                     |

---

## 🧠 Key Insights

- Cloudflare significantly reduced average latency in several regions (Africa, Asia)
- Some HTTPS tests showed slightly increased latency due to inspection overhead
- Failure heatmaps identified unstable endpoints and test types
- Max latency spikes were found in high-latency routes like Angola or CN

---

## 🚀 Tools Used
- Tableau Desktop
- Python (for data cleaning)
- Pandas / CSV
- GitHub

---

## 📈 Demo
> *(Optional if publishing to Tableau Public — insert link)*  
https://public.tableau.com/views/NetworkPerformanceDashboard

---

## 🧑‍💼 Author
**Siddhant Evre**  
MS in Data Science, University of Illinois Urbana-Champaign  
[LinkedIn](https://www.linkedin.com/in/siddhantevre/)

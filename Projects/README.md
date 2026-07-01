# Projects – Kawtar Elbay

---

## 1. Data Analytics – Deloitte (Forage)

**Date:** June 2026  
**Type:** Virtual Work Experience Program

### Project Overview
This project is part of the virtual work experience program with Deloitte on Forage. The goal was to analyze telemetry data collected from 4 factories (Daikibo) to identify machine breakdown patterns and investigate gender pay equality.

---

### Task 1: Telemetry Data Analysis

#### Context
The client, Daikibo, has 4 factories:
- Daikibo Factory Meiyo (Tokyo, Japan)
- Daikibo Factory Seiko (Osaka, Japan)
- Daikibo Berlin (Berlin, Germany)
- Daikibo Shenzhen (Shenzhen, China)

Each location has 9 types of machines, sending a message every 10 minutes. Data was collected for one month (May 2021) and shared as a single JSON file.

#### Objectives
1. Identify the location where machines broke the most
2. Determine which machines broke most often in that location

#### Tasks Performed
- Analyzed telemetry data using Tableau
- Created a calculated measure field "Unhealthy" with a value of 10 for each unhealthy status (representing 10 minutes of potential downtime)
- Created a bar chart "Down Time per Factory"
- Created a bar chart "Down Time per Device Type"
- Designed an interactive dashboard with both charts, using the first chart as a filter

#### Results
- Identified the factory with the most machine breakdowns
- Determined the most frequently broken machines in that location
- Delivered an interactive dashboard for data exploration

#### Dashboard Screenshot
![Deloitte Dashboard - Task 1](../Screenshots/deloitte_dashboard.png)

---

### Task 2: Gender Pay Equality Analysis

#### Context
After internal complaints about gender inequality in terms of salary, Daikibo Industrials requested an investigation. The Forensic Tech team built an algorithm to quantify the "level of gender pay equality" for most job roles within the company, in all company locations.

#### Data Provided
An Excel file (`Equality Table.xlsx`) containing:
1. **Factory** – Location name
2. **Job Role** – Employee position
3. **Equality Score** – Integer between -100 and +100 (0 is ideal)

#### Objectives
Create a 4th column (`Equality class`) classifying the equality score into 3 types:

| Class | Score Range |
| :--- | :--- |
| **Fair** | Between -10 and +10 |
| **Unfair** | Less than -10 OR greater than +10 |
| **Highly Discriminative** | Less than -20 OR greater than +20 |

#### Tasks Performed
- Analyzed the equality data in Excel
- Created a new column "Equality class" using conditional logic
- Classified each employee based on their equality score

#### Results Table
![Deloitte Equality Table](../Screenshots/deloitte_equality_table.png)

---

### Technologies Used
- **Tableau** – Data visualization and dashboard creation
- **Excel** – Data analysis and classification
- **Data Analysis** – Telemetry data and equality analysis
- **Dashboard Design** – Interactive dashboards

---

*Part of the Deloitte Data Analytics Virtual Work Experience Program on Forage*
## 2. Data for Decision Making – BCG X (Forage)

**Date:** June 2026  
**Type:** Virtual Work Experience Program

### Project Overview
This project is part of the virtual work experience program with BCG X on Forage. The goal was to review digital ad campaign performance data and identify insights to guide smarter business decisions.

### Objectives
- Analyze campaign performance data
- Identify key insights and trends
- Provide data-driven recommendations for future campaigns

### Tasks Performed
- Reviewed digital ad campaign performance data
- Analyzed campaign metrics to identify patterns
- Developed recommendations based on data insights
- Prepared a presentation of findings

### Results
- Identified key performance indicators and trends
- Provided actionable recommendations for campaign optimization
- Demonstrated how data drives strategic decision-making

### Technologies Used
- **Data Analysis** – Campaign performance analysis
- **Decision Making** – Strategic recommendations
- **Business Intelligence** – Data-driven insights

### Screenshot
![BCG X Analysis](../Screenshots/bcgx_analysis.png)

---

## 3. Power BI – San Francisco Police Incidents

**Date:** April 2026  
**Type:** Academic Project

### Project Overview
This project involved analyzing public safety data from the San Francisco Police Department to create an interactive decision-making dashboard.

### Objectives
- Perform advanced data cleaning
- Create an interactive dashboard for incident analysis
- Identify high-risk areas and propose strategies to reduce incidents

### Tasks Performed
- Performed advanced data cleaning with Power Query
- Created an interactive dashboard with key performance indicators
- Analyzed trends to identify zones at risk
- Proposed strategies to limit incidents based on data insights

### Results
- Delivered an interactive Power BI dashboard
- Identified high-risk areas and incident patterns
- Provided actionable strategies for incident reduction

### Technologies Used
- **Power BI** – Dashboard creation
- **Power Query** – Data cleaning and transformation
- **Data Visualization** – Interactive visualizations
- **Data Analysis** – Trend analysis and pattern identification

### Screenshot
![Power BI Dashboard](../Screenshots/powerbi_dashboard.png)

---

## 4. NoSQL – Vehicle Rental System

**Date:** April 2026  
**Type:** Academic Project

### Project Overview
This academic project involved developing a vehicle rental management application using NoSQL database and Streamlit.

### Objectives
- Import large datasets into Firestore
- Develop a complete CRUD interface
- Create a user-friendly application

### Tasks Performed
- Imported 2,000+ contracts from CSV to Firestore
- Developed a full CRUD interface (Create, Read, Update, Delete)
- Built a user interface with Streamlit
- Implemented search and filtering functionalities

### Results
- Fully functional vehicle rental application
- Easy-to-use interface for managing contracts
- Efficient data storage and retrieval

### Technologies Used
- **Python** – Programming language
- **Firestore** – NoSQL database
- **Streamlit** – Web application framework
- **CSV** – Data import

### Screenshot
![NoSQL App](../Screenshots/nosql_app.png)

---

## 5. Python – Chronic Kidney Disease (CKD) Diagnosis

**Date:** March 2026  
**Type:** Academic Project

### Project Overview
This academic project involved analyzing medical data to predict the risk of Chronic Kidney Disease (CKD) using machine learning techniques.

### Objectives
- Perform data cleaning and exploratory analysis
- Build machine learning models for CKD prediction
- Achieve high-accuracy predictions

### Tasks Performed
- Data cleaning and preprocessing with Pandas
- Exploratory data analysis with visualizations
- Applied machine learning techniques:
  - Classification – Predicting CKD risk
  - Clustering – Grouping similar patient profiles
  - Dimensionality Reduction – Reducing features while preserving information
- Evaluated model performance with metrics

### Results
- Successfully predicted CKD risk with high accuracy
- Identified key features contributing to CKD diagnosis
- Delivered a Jupyter Notebook with complete analysis

### Technologies Used
- **Python** – Programming language
- **Pandas** – Data manipulation
- **Scikit-learn** – Machine learning models
- **Matplotlib / Seaborn** – Data visualization
- **Google Colab** – Development environment

### Screenshot
![CKD Model](../Screenshots/ckd_model.png)

---

## 6. Java – GameVersAcademy Catalog Management

**Date:** February 2026  
**Type:** Academic Project

### Project Overview
This academic project involved developing a catalog management application for GameVersAcademy using Java and Eclipse IDE.

### Objectives
- Implement user data management
- Create a functional CRUD application
- Develop an interactive user interface

### Tasks Performed
- Implemented CRUD operations
- Developed filtered search functionality
- Created an interactive table for data display
- Managed user data efficiently

### Results
- Fully functional catalog management application
- User-friendly interface for data management
- Efficient search and filtering capabilities

### Technologies Used
- **Java** – Programming language
- **Eclipse IDE** – Development environment
- **CRUD Operations** – Data management

### Screenshot
![Java App](../Screenshots/java_app.png)

---

*Last updated: July 2026*

#  Cyber Threat & Vulnerability Analysis in Healthcare Using ML

A machine learning-based project that uses Logistic Regression to assess cyber threats and vulnerabilities within the healthcare ecosystem.
##  Features
- Logistic Regression ML model for threat prediction
- Supports CSV data input (mock/sample data)
- Accuracy, Confusion Matrix, and Classification Report output
- Clean terminal output
##  How It Works
- Reads cyber threat data from a CSV file
- Splits into training and test sets
- Trains a Logistic Regression model
- Evaluates performance using sklearn metrics
##  How to Run

```bash
# 1. Clone the repo
git clone https://github.com/iamshankar23/cyber-threat-ml-healthcare.git

# 2. Go into the project directory
cd cyber-threat-ml-healthcare

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Python model
python logistic_model.py

---

###  5. **Example Output**
```markdown
##  Sample Output

 Accuracy: 1.0  
 Confusion Matrix:  
[[1 0]  
 [0 1]]  

 Classification Report:

          precision    recall  f1-score   support

       0       1.00      1.00      1.00         1
       1       1.00      1.00      1.00         1

accuracy                           1.00         2
##  Tech Stack
- Python 3.x
- scikit-learn
- pandas
##  Author

**Guru Shankar R**  
BCA Graduate | Aspiring Software Developer  
[GitHub](https://github.com/iamshankar23) • [LinkedIn](https://linkedin.com/in/guru-shankar-840936243)



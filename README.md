# Smart-Resume-Analyzer-with-Action-Based-Feedback 
##  Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [How to Run](#how-to-run)
- [Example Output](#example-output)
- [Tech Stack](#tech-stack)
- [Author](#author)
##  Features
-  Reads resumes in `.txt`, `.pdf`, and `.docx`
-  Matches against a keyword list
-  Calculates resume match score (0–100%)
-  Generates feedback report
-  GitHub Actions automation
## How It Works
- Reads resume content using Python file handlers and libraries (`PyPDF2`, `python-docx`)
- Loads a keyword list from `keywords.txt`
- Compares the resume content against each keyword
- Scores based on matches
- Outputs the result and generates a report (`resume_feedback.txt`)
## ▶ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/yourname/smart-resume-analyzer.git

# Navigate to the project folder
cd smart-resume-analyzer

# Install dependencies
pip install -r requirements.txt

# Run the analyzer
python resume_checker.py sample_resume.txt
##  How to Run Locally

---

###  6. **Example Output**

```markdown
##  Example Output

 Resume Score: 100.00%  
 Keywords Present: ['python', 'sql', 'git', 'oop']  
 Missing Keywords: []
##  Tech Stack
- Python 3.10+
- PyPDF2
- python-docx
- GitHub Actions
- GitHub Codespaces (optional)
##  Author

**Guru Shankar R**  
Aspiring Software Developer  
[GitHub](https://github.com/iamshankar23) • [LinkedIn](https://linkedin.com/in/guru-shankar-840936243)


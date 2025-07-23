import os
import sys
import docx
import PyPDF2

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    text = ""
    if ext == ".txt":
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    elif ext == ".pdf":
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = " ".join([page.extract_text() or "" for page in reader.pages])
    elif ext == ".docx":
        doc = docx.Document(file_path)
        text = " ".join([para.text for para in doc.paragraphs])
    else:
        raise ValueError("Unsupported file format. Use .txt, .pdf, or .docx")
    return text.lower()

def analyze_resume(resume_path, keyword_path):
    resume_text = extract_text(resume_path)

    with open(keyword_path, 'r', encoding='utf-8') as f:
        keywords = [k.strip().lower() for k in f.readlines()]

    found = [k for k in keywords if k in resume_text]
    missing = [k for k in keywords if k not in resume_text]
    score = len(found) / len(keywords) * 100

    print(f"\n✅ Resume Score: {score:.2f}%")
    print("✔️ Keywords Present:", found)
    print("❌ Missing Keywords:", missing)

    # Optional: save to feedback.txt
    with open("resume_feedback.txt", "w") as out:
        out.write(f"Resume Score: {score:.2f}%\n\n")
        out.write("Keywords Found:\n" + ", ".join(found) + "\n\n")
        out.write("Keywords Missing (suggested to learn/improve):\n" + ", ".join(missing))

if __name__ == "__main__":
    resume_path = sys.argv[1] if len(sys.argv) > 1 else "sample_resume.txt"
    analyze_resume(resume_path, "keywords.txt")

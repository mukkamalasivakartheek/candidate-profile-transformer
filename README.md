# Candidate Profile Transformer

## Overview

Candidate Profile Transformer is a Python-based data transformation pipeline that consolidates candidate information from multiple structured and unstructured sources into a single canonical candidate profile.

The system ingests candidate information from multiple sources, normalizes the data, resolves conflicts, tracks provenance, and generates a trustworthy canonical profile for downstream systems.

This project was developed as part of the Eightfold AI Candidate Profile Transformation assignment.

---

# Features

## Supported Input Sources

### Structured Sources

- Recruiter CSV
- ATS JSON

### Unstructured Sources

- Resume PDF
- Resume DOCX
- Recruiter Notes TXT

---

# Core Functionalities

## Extraction

The system extracts candidate information such as:

- Full Name
- Email Address
- Phone Number
- Skills
- Location
- Education
- LinkedIn URL
- GitHub URL
- Years of Experience

---

## Normalization

The pipeline standardizes all extracted values.

| Field | Format |
|--------|--------|
| Email | Lowercase |
| Phone | E.164 |
| Country | ISO Alpha-2 |
| Dates | YYYY-MM |
| Skills | Canonical Lowercase |

Examples:

```text
Py -> python
K8s -> kubernetes
Node.js -> nodejs
```

---

## Merge Strategy

When conflicting values exist across sources, the following priority order is applied:

```text
Resume > ATS > Recruiter CSV > Notes
```

Higher-priority sources override lower-priority sources.

---

## Provenance Tracking

Every field stores information about where it originated.

Example:

```json
{
    "field": "full_name",
    "source": "ats",
    "method": "priority_merge"
}
```

---

## Confidence Scoring

Each source contributes confidence scores.

| Source | Confidence |
|---------|------------|
| Resume | 0.90 |
| ATS | 0.85 |
| CSV | 0.80 |
| Notes | 0.60 |

Overall confidence is calculated using:

```text
Average(Field Confidences)
```

---

# Project Structure

```text
candidate-profile-transformer/
│
├── README.md
├── requirements.txt
│
├── config/
│   └── custom_projection.json
│
├── inputs/
│   ├── recruiter.csv
│   ├── ats.json
│   ├── resume.pdf
│   └── notes.txt
│
├── outputs/
│   └── result.json
│
├── src/
│   ├── main.py
│   ├── pipeline.py
│   ├── constants.py
│   │
│   ├── extractors/
│   ├── merge/
│   ├── models/
│   ├── normalization/
│   ├── projection/
│   └── validation/
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/mukkamalasivakartheek/candidate-profile-transformer.git
cd candidate-profile-transformer
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Required Libraries

```text
pandas
pydantic
click
phonenumbers
python-dateutil
pycountry
pdfplumber
python-docx
```

---

# Sample Input Files

## recruiter.csv

```csv
name,email,phone,current_company,title
Siva Kartheek Mukkamala,mukkamalasivakartheek@gmail.com,+91 9390565317,KL University,DevOps Engineer
```

---

## ats.json

```json
{
  "candidateName": "Siva Kartheek Mukkamala",
  "primaryEmail": "mukkamalasivakartheek@gmail.com",
  "mobile": "+91 9390565317",
  "jobTitle": "DevOps Engineer",
  "city": "Bapatla",
  "state": "Andhra Pradesh",
  "country": "India",
  "skills": [
    "Python",
    "Docker",
    "AWS",
    "Linux",
    "SQL",
    "Git"
  ]
}
```

---

## notes.txt

```text
Candidate is a DevOps-focused B.Tech student with strong foundations in Linux, Docker, AWS, Python, SQL, Git, and Cloud Computing.

Candidate has approximately 3 years of academic and project experience.

Recommended role: DevOps Engineer / Site Reliability Engineer.
```

---

## Resume

Place the resume file inside:

```text
inputs/resume.pdf
```

---

# Running the Project

## Using PyCharm

### Step 1

Open the project in PyCharm.

### Step 2

Configure Python Interpreter.

```text
File → Settings → Python Interpreter
```

### Step 3

Install dependencies.

```bash
pip install -r requirements.txt
```

### Step 4

Right-click:

```text
src/main.py
```

Select:

```text
Run 'main'
```

---

## Using Command Line

Navigate to the project root directory:

```bash
cd candidate-profile-transformer
```

Run:

```bash
python src/main.py
```

---

# Example Output

```json
{
    "candidate_id": "CAND-001",
    "full_name": "Siva Kartheek Mukkamala",
    "emails": [
        "mukkamalasivakartheek@gmail.com"
    ],
    "phones": [
        "+919390565317"
    ],
    "location": {
        "city": "Bapatla",
        "region": "Andhra Pradesh",
        "country": "IN"
    },
    "links": {
        "linkedin": null,
        "github": null,
        "portfolio": null,
        "other": []
    },
    "headline": "DevOps Engineer",
    "years_experience": null,
    "skills": [
        {
            "name": "python",
            "confidence": 0.9,
            "sources": [
                "resume"
            ]
        },
        {
            "name": "docker",
            "confidence": 0.9,
            "sources": [
                "resume"
            ]
        }
    ],
    "education": [
        {
            "institution": "KL University",
            "degree": "B.Tech",
            "field": "Artificial Intelligence and Data Science",
            "end_year": null
        }
    ],
    "experience": [],
    "provenance": [
        {
            "field": "full_name",
            "source": "ats",
            "method": "priority_merge"
        }
    ],
    "overall_confidence": 0.88
}
```

---

# Output Location

The transformed candidate profile is automatically saved in:

```text
outputs/result.json
```

---

# Error Handling

The system gracefully handles:

- Missing files
- Empty files
- Malformed JSON
- Malformed CSV
- Invalid phone numbers
- Unknown countries
- Missing configuration files

The pipeline never crashes and returns safe default values whenever possible.

---

# Design Decisions

## Why Rule-Based Extraction?

- Deterministic behavior
- Explainable transformations
- Easy debugging
- No dependency on external APIs

## Why Source Priority?

Ensures trusted sources override less reliable sources.

## Why Provenance Tracking?

Allows downstream systems to understand where each value originated.

---

# Future Enhancements

- NLP-based resume parsing
- LLM-powered extraction
- REST API support
- Database integration
- Advanced conflict resolution
- Skill ontology mapping

---

# Author

**Siva Kartheek Mukkamala**

- Email: mukkamalasivakartheek@gmail.com
- Location: Bapatla, Andhra Pradesh, India
- Role: DevOps Engineer
- University: KL University

```

# 🧠 Legal AI Pipeline – GST Notice Response Generator

## Overview

This project is an AI-powered legal drafting system that automates the generation of structured replies to GST tax notices.

Instead of manually drafting rebuttals, the system:

1. Reads a GST Show Cause Notice (SCN) from a `.docx` file  
2. Extracts individual legal charges  
3. Classifies the nature of each charge  
4. Uses Google Gemini API to generate structured legal rebuttals  
5. Compiles a professionally formatted legal memo in `.docx` format  

The system is modular, scalable, and designed with production-level AI orchestration principles.

---

## 🚀 Key Features

- Automated extraction of legal charges from tax notices
- Structured AI-driven rebuttal generation
- Formal legal memo formatting
- Modular architecture (separation of concerns)
- Scalable design for handling multiple notices
- Configurable AI model and parameters
- Clean Word document output

---

## 📂 Project Structure

```
legal_ai/
│
├── main.py
├── config.py
├── requirements.txt
│
├── data/
│   └── interview_SCN.docx
│
├── modules/
│   ├── __init__.py
│   ├── doc_reader.py
│   ├── charge_extractor.py
│   ├── legal_analyzer.py
│   ├── ai_engine.py
│   ├── memo_builder.py
│
└── output/
    └── generated_reply.docx
```

---

## 🧩 System Architecture

### 1️⃣ Document Reader (`doc_reader.py`)
- Uses `python-docx`
- Extracts raw text from input SCN document
- Cleans blank lines
- Returns full textual content

---

### 2️⃣ Charge Extractor (`charge_extractor.py`)
- Uses regex pattern matching
- Identifies numbered legal charges
- Extracts charge text into structured list
- Supports scalable charge detection

---

### 3️⃣ Legal Analyzer (`legal_analyzer.py`)
- Classifies each charge into legal categories:
  - ITC Reversal
  - Best Judgment Assessment
  - Time Limit / Interest Issue
  - SCN Threat
- Enables targeted AI prompting

---

### 4️⃣ AI Engine (`ai_engine.py`)
- Integrates with Google Gemini API
- Constructs structured legal prompts
- Enforces strict output format
- Focuses on:
  - Burden of proof on Revenue
  - Procedural defects
  - Statutory counter-arguments
- Returns formatted rebuttal text

---

### 5️⃣ Memo Builder (`memo_builder.py`)
- Generates final `.docx` file
- Adds:
  - Legal header
  - Notice reference
  - Party details
  - Charge-wise structured rebuttal
  - AI tools disclosure
- Produces clean, submission-ready document

---

### 6️⃣ Main Controller (`main.py`)
Orchestrates entire pipeline:

```
Read Notice → Extract Charges → Classify → Generate AI Rebuttal → Build Memo
```

---

## 🧠 AI Prompt Engineering Strategy

The system does NOT use generic prompts.

Each charge is processed using a structured legal reasoning prompt:

- Charge number included
- Charge category included
- Strict formatting enforced
- No markdown allowed
- No extra commentary allowed

Output format enforced:

```
1. RE: CHARGE TITLE

AI-Generated Analysis & Counter-Argument:

What the Charge Means:
...

Our Counter-Argument:
...

Legal Support from AI Research:
...

Simple Explanation:
...
```

This ensures predictable, legally structured responses.

---

## ⚙️ Installation

### Step 1: Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Add Gemini API Key

Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run the Project

```bash
python main.py
```

Output will be generated in:

```
output/generated_reply.docx
```

---

## 🏗️ Engineering Approach

This project follows software engineering best practices:

- Modular file structure
- Separation of concerns
- Config-driven AI parameters
- Clean prompt isolation
- Error handling in AI layer
- Scalable charge detection
- Structured document assembly

---

## 🧪 Techniques Used

- Regex-based legal charge segmentation
- AI prompt constraint engineering
- Formal memo templating
- LLM orchestration pipeline
- Automated document generation
- Defensive programming for API responses

---

## 📈 Why This Is Different From a Basic AI Script

Most solutions:
- Copy notice text
- Ask ChatGPT for answer
- Paste result manually

This system:
- Builds an automated legal drafting pipeline
- Uses structured reasoning
- Enforces output format
- Produces formal submission-ready documents
- Can be reused for multiple notices

---

## 🔮 Future Enhancements

- JSON-based structured AI output validation
- Legal citation verification layer
- Hallucination detection
- Executive summary auto-generation
- Risk scoring per charge
- Multi-notice batch processing
- Migration to `google.genai` (new SDK)

---

## ⚖️ Disclaimer

This tool is built for academic and research purposes only.  
All legal arguments generated are AI-assisted and should be reviewed by a qualified legal professional before use.

---

## 👨‍💻 Author

Krishna  
Engineering – AI & Legal Automation Project

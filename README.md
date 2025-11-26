\# Review Manipulation CTF – STU064



This repository contains my complete solution for the "Review Manipulation Capture-the-Flag (CTF)" challenge.

The task involved detecting a synthetic (injected) Amazon book review, identifying the manipulated book, extracting three cryptographic flags, and explaining model predictions using SHAP.



The challenge combined concepts from:



\* Data wrangling

\* Weak supervision

\* Text classification

\* Explainable ML

\* Hashing \& reproducible computation

\* Git version control and reproducibility



---



\# Repository Structure



```

review-ctf-STU064/

│

├── data/

│   ├── books.csv           # Complete Amazon book metadata dataset

│   └── reviews.csv         # Amazon reviews data with one synthetic review

│

├── notebook/

│   └── analysis.ipynb      # Full end-to-end analysis for all flags

│

├── solver.py               # Automated script to compute FLAG1 and FLAG2

├── flags.txt               # Final extracted FLAG1, FLAG2, FLAG3

├── reflection.md           # Reflection on methodology and learnings

├── requirements.txt        # Dependencies to reproduce the environment

└── .gitignore

```



---



\# CTF Objective



Each student is assigned:



\* A unique hash derived from `sha256(StudentID)`

\* One synthetic (fake) review inserted into the dataset

\* A manipulated book in `books.csv`

\* A SHAP-based token contribution that must be extracted



The goal was to reproduce three flags:



| Flag      | Description                                               |

| --------- | --------------------------------------------------------- |

| \*\*FLAG1\*\* | Hash of first 8 non-space chars of manipulated book title |

| \*\*FLAG2\*\* | First 8 hex chars of SHA256(StudentID)                    |

| \*\*FLAG3\*\* | SHA256 hash of the top 3 negative-influence SHAP tokens   |



My student ID is \*\*STU064\*\*.



---



\# How to Reproduce the Results



\## 1.Create the conda environment



```sh

conda create -n ctf\_env python=3.10 -y

conda activate ctf\_env

pip install -r requirements.txt

```



\##  2.Compute FLAG1 and FLAG2



```sh

python solver.py

```



Outputs include:



\* located synthetic review

\* identified manipulated book

\* computed FLAG1 \& FLAG2 hashes



\## 3.Compute FLAG3 using notebook



```sh

jupyter notebook

```



Open:



```

notebook/analysis.ipynb

```



Run cells to:



1\. Clean and preprocess text reviews

2\. Build weak labels (suspicious vs genuine)

3\. Train logistic regression with TF-IDF

4\. Extract SHAP values

5\. Choose top 3 negative influence tokens

6\. Concatenate → hash → FLAG3



---



\# 🏴 Extracted Flags



All flags are stored in `flags.txt`.



```

FLAG1{225671cc68d87eb6a24331027bea6ec1d7afa9a56d8d298eb840b07dc7eb3f84}

FLAG2{2E01B6AA}

FLAG3{ff361ef45b6f8a8cacc4cfb163adcfd3f2a5fd58abce8d92e3fc1f8ffc1440b8}

```



---



\# Technical Approach



\## Step 1 — Compute Student Hash (FLAG2)



Using:



```python

HASH = sha256("STU064".encode()).hexdigest()\[:8].upper()

```



Gives:



```

FLAG2 = 2E01B6AA

```



This hash appears \*\*inside a synthetic injected review\*\*.



---



\## Step 2 — Locate the Fake Review



Search in `reviews.csv`:



```python

reviews\[reviews\["text"].str.contains(HASH, case=False)]

```



This returns exactly \*\*one review\*\*, confirming the injected entry.



---



\## Step 3 — Identify the Manipulated Book



Match the review's `asin` or `parent\_asin` in `books.csv`:



\* Extract book

\* Clean its title

\* Take first 8 non-space characters

\* Apply SHA256 → FLAG1



For the manipulated book:



```

"When Eight Bells Toll"

```



Cleaned:



```

"WhenEigh"

```



So:



```

FLAG1 = sha256("WhenEigh")

```



---



\## Step 4 — Weak Supervision for Suspicious Reviews



Rules used to generate weak labels:



\* reviews mentioning student hash → suspicious

\* very short 1-line or repetitive reviews → suspicious

\* verified purchase + long text → genuine



Train model:



```

TF-IDF → Logistic Regression

```



---



\## Step 5 — SHAP Explainability (FLAG3)



Focus only on \*\*genuine reviews\*\*:



\* Compute SHAP values

\* Extract tokens with \*\*highest negative influence\*\*

\* Pick top 3

\* Concatenate as a string

\* Hash with SHA256 → FLAG3



---



\# Tools \& Technologies



\* \*\*Python\*\* 3.10

\* \*\*pandas\*\*, \*\*numpy\*\*

\* \*\*scikit-learn\*\*

\* \*\*shap\*\* for explainability

\* \*\*TF-IDF vectorization\*\*

\* \*\*Jupyter Notebook\*\*

\* \*\*Git \& GitHub\*\*

\* \*\*SHA256 hashing\*\*



---



\# Reflection



See `reflection.md` for a more complete personal reflection on the analysis.



This CTF helped develop skills in:



\* real-world text analysis

\* spotting synthetic behavior in datasets

\* explainable AI

\* reproducible workflows

\* Git collaboration and version control



---



\# 👤 Author



STU064 – Nikila

IIT Hyderabad

2025 Cohort



---






\# Reflection – Review Manipulation CTF (STU064)



This Review Manipulation Capture-the-Flag challenge helped me combine multiple concepts from data wrangling, text analysis, machine learning, and explainable AI. It was not just about finding three flags — it required understanding how fake reviews can be created, hidden, detected, and analyzed using ML tools. Below is a detailed reflection of my approach, the challenges I faced, and what I learned.



---



\## 1. Understanding the Task



The challenge injects one synthetic review for each student.  

My task was to:



1\. Identify the synthetic (fake) review using a hash derived from my student ID.  

2\. Trace the manipulated book entry in `books.csv` and compute FLAG1.  

3\. Build a weakly supervised classifier to distinguish suspicious vs genuine reviews.  

4\. Use SHAP explainability to extract the top negatively contributing tokens and compute FLAG3.



Although the instructions seemed simple at first, the task required careful use of hashing, dataframe filtering, model training, and explainability.



---



\## 2. FLAG2 – Locating the Injected Review



The first insight was that the synthetic review contains the SHA256 hash of my student ID:



```



STU064 → sha256 → 2E01B6AA (first 8 hex chars)



````



Searching this substring inside `reviews.csv` immediately revealed the injected review.



This step taught me how \*\*simple cryptographic markers\*\* can embed unique identifiers into large datasets without disturbing natural text distribution.



---



\## 3. FLAG1 – Mapping Review to Book Metadata



The next challenge was linking the fake review to the corresponding book.  

The dataset contained multiple ASIN and parent ASIN mappings, so I used a robust filtering strategy:



```python

(books\["isbn\_10"] == asin) OR

(books\["isbn\_13"] == asin) OR

(books\["parent\_asin"] == asin)

````



This correctly returned the manipulated book:



\*\*“When Eight Bells Toll”\*\*



From this title:



\* I removed whitespace

\* Extracted the first 8 characters (`WhenEigh`)

\* Hashed them with SHA256 to generate FLAG1



This step taught me how \*\*structured metadata\*\* interacts with review datasets and how to build defensive matching logic for real-world noisy identifiers.



---



\## 4. Weak Supervision for Suspicious Review Detection



Part of the challenge required distinguishing genuine reviews from manipulated or suspicious ones.

The dataset did not provide labels, so I created \*\*weak labels\*\* based on reasoning rules:



\### Weak label rules I used:



\* Reviews containing the student hash → suspicious

\* Extremely short reviews → likely suspicious

\* Reviews with length > 80 words → likely genuine

\* Verified purchase + detailed opinion → genuine



These noisy rules allowed me to train a logistic regression classifier using TF-IDF features.



This experience reinforced how \*\*weak supervision\*\* can compensate for lack of labeled data in real-world scenarios.



---



\## 5. Explainability Using SHAP (FLAG3)



Using the classifier alone was not enough – the goal was to interpret it.



I computed SHAP values specifically for reviews labeled as genuine:



\* Extracted each token’s contribution

\* Focused on \*\*negative influence tokens\*\*, which reduce classification score

\* Picked the top three tokens

\* Concatenated → hashed to produce FLAG3



This step was the most educational because it showed me:



\* How explainability tools work internally

\* What a model “pays attention to” during prediction

\* How subtle word choices can strongly influence classification decisions



It also emphasized the importance of transparency in ML models, especially in areas like fraud detection.



---



\## 6. Technical and Practical Challenges



I faced several practical issues, especially with:



\### Git \& GitHub



\* Accidentally creating folders with `.py` and `.md` names

\* Files not tracked due to wrong directory paths

\* Git ignoring files unintentionally

\* Having to reindex the repository



Troubleshooting these taught me more about:



\* `.git` folder structure

\* Git LFS

\* How Git tracks files vs folders

\* How to manually reinitialize and fix a broken repo



\### Environment Setup



Creating a dedicated conda environment helped ensure reproducibility and avoid dependency conflicts.



---



\## 7. Key Learnings



Through this CTF, I gained confidence in:



\* Working with large CSV datasets

\* Creating reproducible ML pipelines

\* Using hashing for ID-based tracking

\* Building weak labels for training

\* Training text classification models

\* Using SHAP for model explainability

\* Managing Git repositories

\* Writing clean, well-documented code



Most importantly, I learned how multiple concepts — cryptography, NLP, ML, explainability, and data engineering — connect together in a single realistic workflow.



---



\## 8. Conclusion



Overall, the CTF was an eye-opening exercise that challenged me technically and analytically.

It felt like a real-world data forensics task, where the answers were hidden inside a large dataset and required multiple tools to uncover. The final combination of data analysis, hashing, weak supervision, and explainable AI made this challenge both enjoyable and educational.



This experience significantly strengthened my understanding of:



\* review manipulation detection

\* modern data science workflows

\* the importance of interpretability in ML systems



I feel much more confident now handling similar data-heavy tasks in the future.



---



\*\*STU064 – Nikila\*\*



```




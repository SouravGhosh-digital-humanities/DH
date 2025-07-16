# DH
**Project on Police Brutality**

This text preprocessing routine is designed to clean and standardize raw input for natural language processing tasks. It begins by converting all characters to lowercase to maintain consistency and ensure case-insensitive matching. Then it systematically removes unwanted elements: punctuation, special characters, short words of one or two letters that typically offer little semantic value, and numeric digits. It also strips out web URLs and email addresses, both of which are often irrelevant for text analysis and can introduce noise or privacy concerns. The resulting text is a simplified, de-cluttered version that retains essential linguistic content while minimizing distractions, making it more suitable for tasks like tokenization, sentiment analysis, or machine learning pipelines.



---

# Text Cleaning with Regex

This repository contains a Python function designed for **text normalization and cleaning**—a vital preprocessing step for natural language processing (NLP) tasks and machine learning pipelines. The script methodically transforms raw, unstructured text into a simplified, noise-free format that’s easier to tokenize, vectorize, and analyze.

# What It Does

The script performs the following steps:
- Converts all text to lowercase to standardize input.
- Removes special characters, punctuation, and symbols.
- Collapses extra whitespace and trims leading/trailing spaces.
- Eliminates short words (1–2 letters) and numeric digits.
- Strips out URLs (including http/https and www-based links).
- Deletes email addresses for cleaner and privacy-preserving text.

This makes the processed output more effective for tasks like sentiment analysis, topic modeling, or information retrieval.

# Example Use Case
Ideal for academic research, chatbots, digital humanities projects, or any domain where text clarity and consistency are important—especially when working with large corpora or web-scraped data.

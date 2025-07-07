# README.md

This is a simple Python script that scans text documents to detect **Personally Identifiable Information (PII)** such as emails, phone numbers, Social Security numbers, and dates of birth using regular expressions.

## Features

- Detects common PII types: Email, Phone, SSN, Date of Birth.
- Loads plain text files.
- Prints detected PII with counts.
- Easy to extend with more patterns or file formats.

## Getting Started

### Prerequisites

- Python 3.x installed.

### Usage

1. Place the text file you want to scan in the same folder (default: `sample_document.txt`).
2. Run the script:

```bash
python3 pii_scanner.py

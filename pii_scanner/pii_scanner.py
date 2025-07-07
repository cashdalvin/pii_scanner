import re

def load_text(file_path):
    """Load text content from a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# Patterns to detect common PII types
patterns = {
    "Email": r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
    "Phone": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
    "SSN": r"\b\d{3}-\d{2}-\d{4}\b",
    "Date of Birth": r"\b(?:\d{1,2}[/-])?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*[/-]?\d{2,4}\b|\b(?:\d{1,2}[/-]){2}\d{2,4}\b",
}

def find_pii(text):
    """
    Find PII in the given text based on predefined regex patterns.
    Returns a dictionary with PII type as keys and list of found items as values.
    """
    findings = {}
    for label, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            # Use set to remove duplicates
            findings[label] = list(set(matches))
    return findings

def main():
    path = "sample_document.txt"
    text = load_text(path)
    pii_found = find_pii(text)

    if pii_found:
        print("🔍 PII Detected:")
        for pii_type, items in pii_found.items():
            print(f"\n{pii_type} ({len(items)} found):")
            for item in items:
                print(f"  - {item}")
    else:
        print("✅ No PII found.")

if __name__ == "__main__":
    main()

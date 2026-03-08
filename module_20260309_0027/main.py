```python
import re
import spacy
from typing import List, Dict, Union, Optional
from dataclasses import dataclass
from datetime import datetime

# Load SpaCy model for Named Entity Recognition (NER)
# Note: In production, use 'en_core_web_trf' for higher accuracy
try:
    nlp = spacy.load("en_core_web_sm")
except ImportError:
    raise ImportError("Please install spacy and download the model: pip install spacy && python -m spacy download en_core_web_sm")

@dataclass
class PHIEntity:
    text: str
    label: str
    start_char: int
    end_char: int
    replacement: str

class ClinicalDeidentifier:
    """
    A specialized module for de-identifying Protected Health Information (PHI) 
    from clinical notes, adhering to HIPAA Safe Harbor guidelines.
    """

    def __init__(self, mask_char: str = "[MASKED]"):
        self.mask_char = mask_char
        # Patterns for IDs, SSNs, and Phone Numbers
        self.regex_patterns = {
            "SSN": r'bd{3}-d{2}-d{4}b',
            "PHONE": r'b(+d{1,2}s)?(?d{3})?[s.-]d{3}[s.-]d{4}b',
            "EMAIL": r'b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}b',
            "MRN": r'bMRN[:s#]*(d{5,10})b',  # Medical Record Number
            "ZIP": r'bd{5}(?:-d{4})?b'
        }

    def _get_ner_entities(self, text: str) -> List[PHIEntity]:
        """Extracts Names, Locations, and Organizations using NLP."""
        doc = nlp(text)
        entities = []
        # Target labels for HIPAA: PERSON, GPE (Location), ORG (Hospital/Clinic)
        target_labels = {"PERSON", "GPE", "ORG", "FAC"}
        
        for ent in doc.ents:
            if ent.label_ in target_labels:
                entities.append(PHIEntity(
                    text=ent.text,
                    label=ent.label_,
                    start_char=ent.start_char,
                    end_char=ent.end_char,
                    replacement=f"[{ent.label_}]"
                ))
        return entities

    def _get_regex_entities(self, text: str) -> List[PHIEntity]:
        """Extracts structured data like SSNs and Emails using Regex."""
        entities = []
        for label, pattern in self.regex_patterns.items():
            for match in re.finditer(pattern, text):
                entities.append(PHIEntity(
                    text=match.group(),
                    label=label,
                    start_char=match.start(),
                    end_char=match.end(),
                    replacement=f"[{label}]"
                ))
        return entities

    def scrub(self, clinical_note: str, show_labels: bool = True) -> str:
        """
        Main entry point to de-identify text.
        Returns the scrubbed string with PHI replaced by placeholders.
        """
        if not clinical_note:
            return ""

        # Collect all candidates for masking
        all_entities = self._get_ner_entities(clinical_note) + self._get_regex_entities(clinical_note)
        
        # Sort entities by start position descending to avoid index shifting during replacement
        all_entities.sort(key=lambda x: x.start_char, reverse=True)

        scrubbed_text = clinical_note
        for ent in all_entities:
            replacement = ent.replacement if show_labels else self.mask_char
            scrubbed_text = (
                scrubbed_text[:ent.start_char] + 
                replacement + 
                scrubbed_text[ent.end_char:]
            )

        return scrubbed_text

# Example Usage
if __name__ == "__main__":
    engine = ClinicalDeidentifier()
    
    raw_note = """
    PATIENT VISIT SUMMARY
    Date: 2023-10-12
    Patient: John Doe (MRN: 8829103)
    Phone: 555-0199
    Note: The patient was admitted to Mayo Clinic in Rochester. 
    He is concerned about his SSN 123-45-6789 being leaked.
    Contact him at john.doe@email.com.
    """
    
    clean_note = engine.scrub(raw_note)
    print("--- DE-IDENTIFIED NOTE ---")
    print(clean_note)
```
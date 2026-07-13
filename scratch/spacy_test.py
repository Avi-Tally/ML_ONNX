import spacy

nlp = spacy.load("en_core_web_sm")

queries = [
    "highest receivable bill amount",
    "pending for bill 613",
    "show pending invoices from supplier",
    "List the parties to whom I need to make the payment this week",
    "Customer dues and settled bills with over due amount less than 55000",
    "Total cleared bills for Reliance Industries Ltd.",
    "Give me the outstanding amount for FY 2025-26 and also show how much is overdue beyond 90 days."
]

for query in queries:
    doc = nlp(query)
    print(f"\nQuery: {query}")
    
    # Noun Chunks
    print("Noun Chunks:")
    for chunk in doc.noun_chunks:
        print(f"  - {chunk.text} (root: {chunk.root.text})")
        
    # Named Entities (DATE, MONEY, CARDINAL)
    print("Entities:")
    for ent in doc.ents:
        if ent.label_ in ['DATE', 'MONEY', 'CARDINAL', 'ORG', 'PERSON']:
            print(f"  - {ent.text} ({ent.label_})")
            
    # Dependency matching for "bill 613"
    print("Document Refs:")
    for token in doc:
        if token.text.lower() in ["bill", "invoice", "voucher"]:
            # look for children that are numbers
            for child in token.children:
                if child.pos_ == "NUM":
                    print(f"  - Found ref {child.text} attached to {token.text}")
            # look for following token if not a child
            if token.i + 1 < len(doc):
                next_token = doc[token.i + 1]
                if next_token.pos_ == "NUM" or next_token.is_digit:
                    print(f"  - Found sequential ref {next_token.text} after {token.text}")

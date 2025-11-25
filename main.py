def is_valid_dna(sequence):
    """Check if sequence contains only valid DNA characters (A, T, C, G)"""
    valid_chars = "ATCG"
    sequence = sequence.upper().strip()
    
    if len(sequence) == 0:
        return False
        
    for char in sequence:
        if char not in valid_chars:
            return False
    return True

def main():
    """DNA Sequence Analyzer - Basic Version"""
    print("=" * 60)
    print("DNA Sequence Validator")
    print("=" * 60)
    
    dna_input = input("Enter DNA sequence (A, T, C, G only): ").strip().upper()
    
    if is_valid_dna(dna_input):
        print("Valid DNA sequence!")
        print(f"Length: {len(dna_input)} nucleotides")
    else:
        print("Invalid DNA sequence! Only A, T, C, G characters allowed.")

if __name__ == "__main__":
    main()

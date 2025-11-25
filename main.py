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

def calculate_gc_content(sequence):
    """Calculate GC content percentage"""
    sequence = sequence.upper()
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    total_length = len(sequence)

    if total_length == 0:
        return 0

    gc_percentage = (g_count + c_count) / total_length * 100
    return round(gc_percentage, 2)

def get_complementary_strand(sequence):
    """Create complementary DNA strand"""
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    complementary = ""
    for nucleotide in sequence.upper():
        complementary += complement_map[nucleotide]
    return complementary

def transcribe_to_rna(sequence):
    """Transcribe DNA to RNA by replacing T with U"""
    return sequence.upper().replace('T', 'U')

def main():
    """DNA Sequence Analyzer - Basic Analysis"""
    print("=" * 60)
    print("DNA Sequence Analyzer")
    print("=" * 60)
    
    dna_input = input("Enter DNA sequence (A, T, C, G only): ").strip().upper()
    
    if not is_valid_dna(dna_input):
        print(" Invalid DNA sequence! Only A, T, C, G characters allowed.")
        return
    
    print(" Valid DNA sequence!")
    print(f"Length: {len(dna_input)} nucleotides")
    print(f"GC Content: {calculate_gc_content(dna_input)}%")
    print(f"Complementary: {get_complementary_strand(dna_input)}")
    print(f"RNA Transcript: {transcribe_to_rna(dna_input)}")

if __name__ == "__main__":
    main()

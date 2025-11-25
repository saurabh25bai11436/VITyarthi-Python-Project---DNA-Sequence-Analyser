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

def analyze_base_composition(sequence):
    """Analyze base composition - returns counts and percentages"""
    sequence = sequence.upper()
    total_length = len(sequence)
    
    base_counts = [
        ('A', sequence.count('A')),
        ('T', sequence.count('T')), 
        ('C', sequence.count('C')),
        ('G', sequence.count('G'))
    ]
    
    base_percentages = []
    for base, count in base_counts:
        percentage = (count / total_length) * 100 if total_length > 0 else 0
        base_percentages.append((base, count, round(percentage, 2)))
    
    return base_percentages

def calculate_at_gc_ratio(sequence):
    """Calculate AT/GC ratio"""
    sequence = sequence.upper()
    at_count = sequence.count('A') + sequence.count('T')
    gc_count = sequence.count('G') + sequence.count('C')
    
    if gc_count == 0:
        return "Undefined (No GC bases)"
    
    ratio = at_count / gc_count
    return round(ratio, 2)

def main():
    """DNA Sequence Analyzer - Statistics Version"""
    print("=" * 60)
    print("DNA Sequence Analyzer")
    print("=" * 60)
    
    dna_input = input("Enter DNA sequence (A, T, C, G only): ").strip().upper()
    
    if not is_valid_dna(dna_input):
        print("❌ Invalid DNA sequence! Only A, T, C, G characters allowed.")
        return
    
    print("✅ Valid DNA sequence!")
    print(f"Length: {len(dna_input)} nucleotides")
    print(f"GC Content: {calculate_gc_content(dna_input)}%")
    print(f"AT/GC Ratio: {calculate_at_gc_ratio(dna_input)}")
    
    print(f"\nBase Composition:")
    for base, count, percentage in analyze_base_composition(dna_input):
        print(f"  {base}: {count} bases ({percentage}%)")

if __name__ == "__main__":
    main()

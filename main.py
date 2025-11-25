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

def find_pattern_occurrences(sequence, pattern):
    """Find all occurrences of a pattern in the sequence"""
    sequence = sequence.upper()
    pattern = pattern.upper()
    positions = []
    start = 0
    
    while True:
        pos = sequence.find(pattern, start)
        if pos == -1:
            break
        positions.append(pos)
        start = pos + 1
    
    return positions

def find_palindromic_sequences(sequence, min_length=4):
    """Find palindromic sequences (same as reverse complement)"""
    sequence = sequence.upper()
    palindromes = []
    
    for length in range(min_length, min(8, len(sequence) + 1)):
        for i in range(len(sequence) - length + 1):
            substring = sequence[i:i + length]
            complement = get_complementary_strand(substring)
            reverse_complement = complement[::-1]
            
            if substring == reverse_complement:
                palindromes.append({
                    'sequence': substring,
                    'position': i,
                    'length': length
                })
    
    return palindromes

def main():
    """DNA Sequence Analyzer - Pattern Search Version"""
    print("=" * 60)
    print("DNA Sequence Analyzer")
    print("=" * 60)
    
    dna_input = input("Enter DNA sequence (A, T, C, G only): ").strip().upper()
    
    if not is_valid_dna(dna_input):
        print(" Invalid DNA sequence! Only A, T, C, G characters allowed.")
        return
    
    print(" Valid DNA sequence!")
    print(f"Length: {len(dna_input)} nucleotides")
    
    # Pattern search
    pattern = input("Enter pattern to search for: ").strip().upper()
    positions = find_pattern_occurrences(dna_input, pattern)
    if positions:
        print(f"Pattern '{pattern}' found {len(positions)} times at positions: {positions}")
    else:
        print(f"Pattern '{pattern}' not found")
    
    # Palindrome search
    palindromes = find_palindromic_sequences(dna_input)
    if palindromes:
        print(f"Found {len(palindromes)} palindromic sequences")
        for i, palindrome in enumerate(palindromes[:2], 1):
            print(f"  {i}. '{palindrome['sequence']}' at position {palindrome['position']}")

if __name__ == "__main__":
    main()

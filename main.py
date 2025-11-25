
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
        if nucleotide in complement_map:
            complementary += complement_map[nucleotide]
        else:
            complementary += '?'  
    return complementary

def transcribe_to_rna(sequence):
    """Transcribe DNA to RNA by replacing T with U"""
    rna_sequence = ""
    for nucleotide in sequence.upper():
        if nucleotide == 'T':
            rna_sequence += 'U'
        else:
            rna_sequence += nucleotide
    return rna_sequence

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

def calculate_at_gc_ratio(sequence):
    """Calculate AT/GC ratio"""
    sequence = sequence.upper()
    at_count = sequence.count('A') + sequence.count('T')
    gc_count = sequence.count('G') + sequence.count('C')
    
    if gc_count == 0:
        return "Undefined (No GC bases)"
    
    ratio = at_count / gc_count
    return round(ratio, 2)

def sequence_statistics(sequence):
    """Comprehensive sequence statistics"""
    stats = {}
    stats['length'] = len(sequence)
    stats['gc_content'] = calculate_gc_content(sequence)
    stats['at_gc_ratio'] = calculate_at_gc_ratio(sequence)
    stats['base_composition'] = analyze_base_composition(sequence)
    
    
    if stats['gc_content'] > 60:
        stats['classification'] = "GC-Rich"
    elif stats['gc_content'] < 40:
        stats['classification'] = "AT-Rich" 
    else:
        stats['classification'] = "Balanced"
    
    return stats

def find_palindromic_sequences(sequence, min_length=4):
    """Find palindromic sequences (same as reverse complement)"""
    sequence = sequence.upper()
    palindromes = []
    
    for length in range(min_length, min(12, len(sequence) + 1)):
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

def simulate_mutations_with_percentage(sequence, mutation_percentage):
    """
    Simulate mutations with specified percentage of bases to mutate
    mutation_percentage: Percentage of total bases that should be mutated (0-100)
    """
    import random
    
    nucleotides = ['A', 'T', 'C', 'G']
    sequence = sequence.upper()
    
    
    total_bases = len(sequence)
    num_mutations = int((mutation_percentage / 100) * total_bases)
    
    
    positions_to_mutate = random.sample(range(total_bases), min(num_mutations, total_bases))
    
    mutated_sequence = list(sequence)
    mutation_log = []
    
    for position in positions_to_mutate:
        original_base = mutated_sequence[position]
        # diff nucloid ke liye
        possible_mutations = [n for n in nucleotides if n != original_base]
        new_base = random.choice(possible_mutations)
        
        mutated_sequence[position] = new_base
        mutation_log.append(f"Position {position}: {original_base} -> {new_base}")
    
    
    mutated_sequence = ''.join(mutated_sequence)
    
    return mutated_sequence, mutation_log

def simulate_random_mutations(sequence, mutation_rate=0.1):
    """Simulate random mutations with probability-based approach"""
    import random
    
    nucleotides = ['A', 'T', 'C', 'G']
    mutated_sequence = ""
    mutation_log = []
    
    for position, nucleotide in enumerate(sequence.upper()):
        if random.random() < mutation_rate:
            possible_mutations = [n for n in nucleotides if n != nucleotide]
            new_nucleotide = random.choice(possible_mutations)
            mutated_sequence += new_nucleotide
            mutation_log.append(f"Position {position}: {nucleotide} -> {new_nucleotide}")
        else:
            mutated_sequence += nucleotide
    
    return mutated_sequence, mutation_log

def display_sequence_analysis(sequence, mutation_percentage=None):
    """Display comprehensive analysis for a valid DNA sequence"""
    print(f"\nOriginal DNA: {sequence}")
    print(f"GC Content: {calculate_gc_content(sequence)}%")
    print(f"Complementary: {get_complementary_strand(sequence)}")
    print(f"RNA Transcript: {transcribe_to_rna(sequence)}")
    
    
    if mutation_percentage is not None:
        mutated, mutations = simulate_mutations_with_percentage(sequence, mutation_percentage)
        print(f"\n--- Mutation ({mutation_percentage}% of bases mutated) ---")
    else:
        mutated, mutations = simulate_random_mutations(sequence, 0.1)
        print(f"\n--- Mutation (10% probability per base) ---")
    
    print(f"Mutated DNA: {mutated}")
    
    if mutations:
        actual_percentage = (len(mutations) / len(sequence)) * 100
        print(f"Mutations occurred: {len(mutations)} bases ({actual_percentage:.1f}%)")
        print("Mutation details:")
        for mutation in mutations[:10]:  # for showing muataion max 10 dikhana h 
            print(f"- {mutation}")
        if len(mutations) > 10:
            print(f"... and {len(mutations) - 10} more mutations")
    else:
        print("No mutations occurred in this simulation.")
    
    
    stats = sequence_statistics(sequence)
    print(f"\n--- DETAILED STATISTICS ---")
    print(f"Sequence Length: {stats['length']} nucleotides")
    print(f"Classification: {stats['classification']}")
    print(f"AT/GC Ratio: {stats['at_gc_ratio']}")
    
    print(f"\nBase Composition:")
    for base, count, percentage in stats['base_composition']:
        print(f"  {base}: {count} bases ({percentage}%)")
    
    # Pattern search
    print(f"\n--- PATTERN ANALYSIS ---")
    patterns = ["CG", "AT", "GC", "TA"]
    for pattern in patterns:
        positions = find_pattern_occurrences(sequence, pattern)
        if positions:
            print(f"Pattern '{pattern}': {len(positions)} occurrences at positions {positions}")
    
    
    print(f"\n--- PALINDROMIC SEQUENCES ---")
    palindromes = find_palindromic_sequences(sequence)
    if palindromes:
        for i, palindrome in enumerate(palindromes[:3], 1):
            print(f"Palindrome {i}: '{palindrome['sequence']}' at position {palindrome['position']}")
    else:
        print("No palindromic sequences found")

def mutation_percentage_tool(sequence):
    """Interactive tool for mutation percentage simulation"""
    print(f"\n--- MUTATION PERCENTAGE SIMULATOR ---")
    print(f"Current sequence: {sequence}")
    print(f"Sequence length: {len(sequence)} bases")
    
    while True:
        try:
            print("\nMutation Options:")
            print("1. Specify exact percentage of bases to mutate")
            print("2. Use probability-based mutation (classic method)")
            print("3. Return to main menu")
            
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '1':
                percentage = float(input("Enter percentage of bases to mutate (0-100): "))
                
                if percentage < 0 or percentage > 100:
                    print(" Error: Percentage must be between 0 and 100")
                    continue
                
                mutated, mutations = simulate_mutations_with_percentage(sequence, percentage)
                
                print(f"\n--- MUTATION RESULTS ({percentage}% mutation) ---")
                print(f"Original: {sequence}")
                print(f"Mutated:  {mutated}")
                print(f"Total mutations: {len(mutations)} bases")
                
                if mutations:
                    print("\nMutation details:")
                    for mutation in mutations[:10]:  # Showing first 10 mutation
                        print(f"  {mutation}")
                    if len(mutations) > 10:
                        print(f"  ... and {len(mutations) - 10} more mutations")
                
                
                actual_percentage = (len(mutations) / len(sequence)) * 100
                print(f"\nRequested: {percentage}% | Actual: {actual_percentage:.2f}%")
                
            elif choice == '2':
                probability = float(input("Enter mutation probability per base (0.0-1.0): "))
                
                if probability < 0 or probability > 1:
                    print(" Error: Probability must be between 0.0 and 1.0")
                    continue
                
                mutated, mutations = simulate_random_mutations(sequence, probability)
                actual_percentage = (len(mutations) / len(sequence)) * 100
                
                print(f"\n--- MUTATION RESULTS ({probability*100}% probability) ---")
                print(f"Original: {sequence}")
                print(f"Mutated:  {mutated}")
                print(f"Total mutations: {len(mutations)} bases ({actual_percentage:.2f}%)")
                
                if mutations:
                    print("\nMutation details:")
                    for mutation in mutations[:15]:
                        print(f"  {mutation}")
                    if len(mutations) > 15:
                        print(f"  ... and {len(mutations) - 15} more mutations")
                        
            elif choice == '3':
                break
            else:
                print(" Invalid choice! Please enter 1-3.")
            
            
            another = input("\nPerform another mutation simulation? (y/n): ").lower()
            if another != 'y':
                break
                
        except ValueError:
            print(" Please enter a valid number!")
        except Exception as e:
            print(f" Error: {e}")

def main():
    """DNA Sequence Analyzer"""
    print("=" * 60)
    print("Welcome!! Play with DNA sequence Analyzer \nExplore Genetics through realm of Python!!        ")
    print("=" * 60)
    
    while True:
        print("\n" + "=" * 40)
        print("MAIN MENU")
        print("=" * 40)
        print("1. Analyze your DNA Sequence")
        print("2. Pattern Search Tool")
        print("3. Mutation Percentage ")
        print("4. Palindromic Sequence Finder")
        print("5. Exit")
        print("=" * 40)
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            
            print("\n--- DNA SEQUENCE ANALYSIS ---")
            dna_input = input("Enter DNA sequence (A, T, C, G only): ").strip().upper()
            
            if not is_valid_dna(dna_input):
                print(" ERROR: Invalid DNA sequence! Only A, T, C, G characters are allowed.")
                continue
                
            if len(dna_input) < 4:
                print(" ERROR: Sequence too short! Minimum 4 nucleotides required.")
                continue
            
            
            try:
                use_percentage = input("Use mutation percentage? (y/n): ").lower()
                if use_percentage == 'y':
                    percentage = float(input("Enter mutation percentage (0-100): "))
                    if 0 <= percentage <= 100:
                        display_sequence_analysis(dna_input, percentage)
                    else:
                        print(" Invalid percentage! Using default mutation rate.")
                        display_sequence_analysis(dna_input)
                else:
                    display_sequence_analysis(dna_input)
            except ValueError:
                print("Invalid input! Using default mutation rate.")
                display_sequence_analysis(dna_input)
            
        elif choice == '2':
        
            print("\n--- PATTERN SEARCH TOOL ---")
            sequence = input("Enter DNA sequence to search in: ").strip().upper()
            pattern = input("Enter pattern to search for: ").strip().upper()
            
            if not is_valid_dna(sequence) or not is_valid_dna(pattern):
                print(" ERROR: Invalid DNA sequence or pattern!")
                continue
                
            positions = find_pattern_occurrences(sequence, pattern)
            if positions:
                print(f"Pattern '{pattern}' found {len(positions)} times at positions: {positions}")
            else:
                print(f"Pattern '{pattern}' not found in the sequence.")
                
        elif choice == '3':
            
            print("\n--- MUTATION PERCENTAGE SIMULATOR ---")
            sequence = input("Enter DNA sequence: ").strip().upper()
            
            if not is_valid_dna(sequence):
                print(" ERROR: Invalid DNA sequence!")
                continue
                
            mutation_percentage_tool(sequence)
            
        elif choice == '4':
            
            print("\n--- PALINDROMIC SEQUENCE FINDER ---")
            sequence = input("Enter DNA sequence: ").strip().upper()
            
            if not is_valid_dna(sequence):
                print(" ERROR: Invalid DNA sequence!")
                continue
                
            palindromes = find_palindromic_sequences(sequence)
            if palindromes:
                print(f"Found {len(palindromes)} palindromic sequences:")
                for i, palindrome in enumerate(palindromes, 1):
                    print(f"{i}. '{palindrome['sequence']}' at position {palindrome['position']} (length: {palindrome['length']})")
            else:
                print("No palindromic sequences found.")
                
        elif choice == '5':
            print("Thank you for using DNA Sequence Analyzer!")
            break
            
        else:
            print(" Invalid choice! Please enter 1-5.")
        
        
        continue_choice = input("\nReturn to main menu? (y/n): ").lower()
        if continue_choice != 'y':
            print("Thank you for using DNA Sequence Analyzer!")
            break


if __name__ == "__main__":
    main()

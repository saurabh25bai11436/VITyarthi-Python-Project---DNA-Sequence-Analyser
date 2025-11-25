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
        possible_mutations = [n for n in nucleotides if n != original_base]
        new_base = random.choice(possible_mutations)
        
        mutated_sequence[position] = new_base
        mutation_log.append(f"Position {position}: {original_base} -> {new_base}")
    
    mutated_sequence = ''.join(mutated_sequence)
    
    return mutated_sequence, mutation_log

def main():
    """DNA Sequence Analyzer - Mutation Engine"""
    print("=" * 60)
    print("DNA Sequence Analyzer - Mutation Simulator")
    print("=" * 60)
    
    dna_input = input("Enter DNA sequence (A, T, C, G only): ").strip().upper()
    
    if not is_valid_dna(dna_input):
        print(" Invalid DNA sequence! Only A, T, C, G characters allowed.")
        return
    
    print(" Valid DNA sequence!")
    print(f"Original: {dna_input}")
    
    try:
        percentage = float(input("Enter mutation percentage (0-100): "))
        if 0 <= percentage <= 100:
            mutated, mutations = simulate_mutations_with_percentage(dna_input, percentage)
            print(f"Mutated:  {mutated}")
            print(f"Mutations: {len(mutations)} bases")
            for mutation in mutations[:3]:
                print(f"  {mutation}")
        else:
            print(" Percentage must be between 0 and 100")
    except ValueError:
        print(" Please enter a valid number")

if __name__ == "__main__":
    main()

def find_lowest_location(content):
    seed_ranges = [int(x) for x in content[1].split()[1:]]  # Extract seed ranges from the second line

    lowest_location = float('inf')

    for seed_start, seed_length in zip(seed_ranges[::2], seed_ranges[1::2]):
        for seed_number in range(seed_start, seed_start + seed_length):
            current_location = convert_seed_to_location(seed_number, content)
            lowest_location = min(lowest_location, current_location)

    return lowest_location

def convert_seed_to_location(seed, content):
    current_category = seed
    for line in content[2:]:
        dest_range_start, source_range_start, range_len = map(int, line.split())
        if source_range_start <= current_category < source_range_start + range_len:
            current_category = dest_range_start + (current_category - source_range_start)
    
    return current_category

def main():
    with open("data.txt", 'r') as file:
        content = file.read().splitlines()

    lowest_location = find_lowest_location(content)
    print("Lowest Location Number:", lowest_location)

if __name__ == "__main__":
    main()

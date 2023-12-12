import numpy as np

def load_file(filepath):
    with open(filepath, 'r') as file:
        content = file.readlines()
    return [x.strip('\n') for x in content]

def get_seeds(content):
    seeds_line = content[0]
    return [int(x) for x in seeds_line.split(':')[1].split()]


def check_ranges(content, section, seed):
    section_ranges = content[content.index(section)+1 : content.index('', content.index(section))]
    dest = seed
    for line in section_ranges:
        splitted_line = line.split()
        length = int(splitted_line[2])
        begin_source = int(splitted_line[1])
        end_source = begin_source+length
        if begin_source <= seed < end_source:
            begin_dest = int(splitted_line[0])
            diff = seed - begin_source
            dest = begin_dest + diff
            break
        else:
            continue
    return dest

def follow_route(content, seeds_ranges):
    locations = []
    for seeds in seeds_ranges:
        for seed in seeds:
            soil   = check_ranges(content, 'seed-to-soil map:',seed)
            fert   = check_ranges(content, 'soil-to-fertilizer map:',soil)
            water   = check_ranges(content, 'fertilizer-to-water map:',fert)
            light  = check_ranges(content, 'water-to-light map:',water)
            temp   = check_ranges(content, 'light-to-temperature map:',light)
            humid  = check_ranges(content, 'temperature-to-humidity map:',temp)
            location= check_ranges(content, 'humidity-to-location map:',humid)
            locations.append(location)
        print("finished with 1 range")
    print(min(locations))
    return

def seeds2(content):
    seeds = []
    seeds_line = content[0]
    all_numbers = [int(x) for x in seeds_line.split(':')[1].strip().split()]
    # print(all_numbers)

    even_indices = all_numbers[::2]
    odd_indices = all_numbers[1::2]
    return [
        range(even, even + odd) for even, odd in zip(even_indices, odd_indices)
    ]

def find_intersection(list1, list2):
    # Find the intersection of the two ranges
    common_start = max(list1[0], list2[0])
    common_stop = min(list1[-1], list2[-1])

    # Check if there is a non-empty intersection
    if common_start < common_stop:
        # Create a range object for the intersection
        intersection = range(common_start, common_stop)

        return list(intersection)
    else:
        # No intersection, return an empty list
        return []

def check_ranges2(content, section, seed_list):
    section_ranges = content[content.index(section)+1 : content.index('', content.index(section))]
    dest_list = seed_list
    begin_seed_range = seed_list[0]
    end_seed_range  = seed_list[-1]
    for line in section_ranges:
        splitted_line = line.split()
        length = int(splitted_line[2])
        begin_source = int(splitted_line[1])
        end_source = begin_source+length
        print("checked a line!")
        if begin_seed_range < end_source and end_seed_range > begin_source:     # logic for when at least a part of the range intersects, otherwise skip it
            begin_dest = int(splitted_line[0])
            # 3 cases: fully inside the range to check, partially outside on lower-bound, partially outside on higher-bound 
            # for when fully in push all numbers:
            intersecting_numbers = find_intersection(range(begin_source,end_source),seed_list)
            diff = begin_dest - begin_source
            # Update only the intersecting numbers
            for i in range(len(intersecting_numbers)):
                dest_list[seed_list.index(intersecting_numbers[i])] += diff

        else:
            continue
    return dest_list


def follow_route2(content, seeds_ranges):
    locations = []
    for seeds in seeds_ranges:
        soil   = check_ranges2(content, 'seed-to-soil map:',list(seeds))
        fert   = check_ranges2(content, 'soil-to-fertilizer map:',soil)
        water   = check_ranges2(content, 'fertilizer-to-water map:',fert)
        light  = check_ranges2(content, 'water-to-light map:',water)
        temp   = check_ranges2(content, 'light-to-temperature map:',light)
        humid  = check_ranges2(content, 'temperature-to-humidity map:',temp)
        location= check_ranges2(content, 'humidity-to-location map:',humid)
        locations.append(location)
        print("finished with 1 range")
    print(min(locations))
    return



if __name__ == '__main__':
    content = load_file('data.txt')
    # seeds = get_seeds(content=content)
    seeds = seeds2(content=content)
    follow_route2(content,seeds)
    # print(seeds)
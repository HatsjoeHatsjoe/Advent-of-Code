import numpy as np

def load_file(filepath):
    with open(filepath, 'r') as file:
        content = file.readlines()
    return [x.strip('\n') for x in content]

def follow_route(content):
    seeds_line = content[0]
    seeds= [int(x) for x in seeds_line.split(':')[1].split()]

    seed_to_soil_map = make_mapping(content, seperator='seed-to-soil map:')
    soil_to_fert_map = make_mapping(content, seperator='soil-to-fertilizer map:')
    fert_to_water_map = make_mapping(content, seperator='fertilizer-to-water map:')
    water_to_light_map = make_mapping(content, seperator='water-to-light map:')
    light_to_temp_map = make_mapping(content, seperator='light-to-temperature map:')
    temp_to_humid_map = make_mapping(content, seperator='temperature-to-humidity map:')
    humid_to_location_map = make_mapping(content, seperator='humidity-to-location map:')

    locations = []
    for seed in seeds:
        soil = seed_to_soil_map[seed] if seed in seed_to_soil_map.keys() else seed
        fert = soil_to_fert_map[soil] if soil in soil_to_fert_map.keys() else soil
        water = fert_to_water_map[fert] if fert in fert_to_water_map.keys() else fert
        light = water_to_light_map[water] if water in water_to_light_map.keys() else water
        temp = light_to_temp_map[light] if light in light_to_temp_map.keys() else light
        humid = temp_to_humid_map[temp] if temp in temp_to_humid_map.keys() else temp
        location = humid_to_location_map[humid] if humid in humid_to_location_map.keys() else humid
        locations.append(location)

    print(f"\n\nlowest number is : {min(locations)}")

    

def make_mapping(content, seperator ='seed-to-soil map:'):

    mapping_string_list = content[content.index(seperator)+1 : content.index('', content.index(seperator))]

    mapping = {}
    for line in mapping_string_list:
        numbers = line.split()
        dest_range_start = int(numbers[0])
        source_range_start = int(numbers[1])
        range_len = int(numbers[2])
        for x in range(range_len):
            mapping[source_range_start+x] = dest_range_start+x
        print(f"done with line {line}")
    sorted_dict = dict(sorted(mapping.items()))
    print(f"{seperator} \n{sorted_dict}")
    return mapping


if __name__ == '__main__':
    content = load_file('testdata.txt')
    follow_route(content=content)
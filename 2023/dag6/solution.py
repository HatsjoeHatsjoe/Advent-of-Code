import numpy as np

def get_data(filepath):
    with open(filepath, 'r') as file:
        content = file.readlines()
    # print(content)
    time = content[0]
    time = time.split(':')[1].split()
    time = [int(x) for x in time]
    # print(time)
    distance = content[1]
    distance = distance.split(':')[1].split()
    distance = [int(x) for x in distance]
    # print(distance)
    return time,distance

def get_data2(filepath):
    with open(filepath, 'r') as file:
        content = file.readlines()
    time = int(content[0].split(':')[1].replace(' ',''))
    end = int(content[1].split(':')[1].replace(' ',''))
    # print(time)
    # print(end)
    return time,end


def calc_max_velocity(time,goal):
    power = 1
    for t in range(len(time)):
        distances = []
        for index in range(time[t]+1):
            velocity = index
            time_left = time[t]-velocity
            end = velocity*time_left
            if end > goal[t]:
                distances.append(end)
        # print(distances)
        power *= len(distances)
    print(power)

def calc_velocity(time, goal):
    distances = []
    for index in range(time+1):
        vel = index
        time_left = time-vel
        end = vel*time_left
        if end>goal:
            distances.append(end)
    print(len(distances))

def main():
    all_time,all_distance = get_data("data.txt")
    calc_max_velocity(time=all_time,goal=all_distance)

    time, end = get_data2("data.txt")
    calc_velocity(time,end)
    

if __name__ == "__main__":
    main()


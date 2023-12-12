def openfile(filepath):
    with open(filepath, 'r') as file:
        content = file.readlines()
    return [x.strip("\n") for x in content]

def check_winning(content):
    total_points = 0
    for line in content:
        # print(f"{line}\n")
        split_line = line.split('|')
        your_numbers_string = split_line[1]
        winning_numbers_string = split_line[0].split(':')[1]
        winning_nmbrs = [int(x) for x in winning_numbers_string.split()]
        my_nmbrs = [int(x) for x in your_numbers_string.split()]
        # print(winning_nmbrs)
        # print(my_nmbrs)
        winning_count = sum(1 for number in my_nmbrs if number in winning_nmbrs)
        # print(winning_count)
        if winning_count == 1:
            total_points += 1
        if winning_count > 1:
            total_points += 2**(winning_count-1)

    print(f"The total points are: {total_points}")
    
        


def main1():
    content = openfile("data.txt")
    check_winning(content=content)

#########################################################################################

class scratchcard():
    def __init__(self, id = None, wins = 0):
        self.copies = 0 
        self.id = id
        self.wins = wins
    
    @classmethod
    def openfile(cls, filepath):
        with open(filepath, 'r') as file:
            content = file.readlines()
        return [x.strip("\n") for x in content]


    def get_id(self,line):
        self.id = int(line.split('|')[0].split(':')[0].split()[1])


    def check_winning(self , content):
        for i,line in enumerate(content):
            # print(f"{line}\n")
            split_line = line.split('|')
            your_numbers_string = split_line[1]
            winning_numbers_string = split_line[0].split(':')[1]
            winning_nmbrs = [int(x) for x in winning_numbers_string.split()]
            my_nmbrs = [int(x) for x in your_numbers_string.split()]
            # print(winning_nmbrs)
            # print(my_nmbrs)
            self.wins = sum(1 for number in my_nmbrs if number in winning_nmbrs)
           
    def calculate_points(self):
        if self.wins == 1:
            self.points += 1
        if self.wins > 1:
            self.points += 2**(self.wins-1)

    def main(self):
        content = self.openfile("testdata.txt")
        self.check_winning(content=content)
        self.calculate_points()

if __name__ == '__main__':
    scratchcard.main()
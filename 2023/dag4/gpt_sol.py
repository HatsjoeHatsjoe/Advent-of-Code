class Card:
    def __init__(self, card_id, winning_numbers, your_numbers):
        self.card_id = card_id
        self.winning_numbers = winning_numbers
        self.your_numbers = your_numbers
        self.points = 0

    def count_winnings(self):
        return sum(1 for number in self.your_numbers if number in self.winning_numbers)

    def get_copy(self):
        return Card(card_id=self.card_id, winning_numbers=self.winning_numbers, your_numbers=self.your_numbers)

    # def calculate_points(self):
    #     # Calculate points only for the original card
       
    #     if winning_count == 1:
    #         self.points += 1
    #     elif winning_count > 1:
    #         self.points += 2 ** (winning_count - 1)

    # def process_copies(self, all_cards):
    #     while self.copies > 0:
    #         for i, card in enumerate(all_cards):
    #             if card.card_id == self.card_id + 1:
    #                 card.copies += self.copies
    #                 self.copies = 0
    #         self.copies -= 1




class Deck:
    def __init__(self, file_path):
        self.cards = []
        self.current_game_id = 1
        self.max_id = 0
        self.load_cards(file_path)
        

    def load_cards(self, file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()
        stripped_content = [x.strip('\n') for x in content]
        self.max_id = len(stripped_content)+1
        for i, line in enumerate(stripped_content):
            split_line = line.split('|')
            your_numbers_string = split_line[1]
            winning_numbers_string = split_line[0].split(':')[1]
            winning_nmbrs = [int(x) for x in winning_numbers_string.split()]
            my_nmbrs = [int(x) for x in your_numbers_string.split()]

            # Create a new Card object
            card = Card(card_id=i + 1, winning_numbers=winning_nmbrs, your_numbers=my_nmbrs)
            self.cards.append(card)

    


    def add_copies(self, wins, current_id):
        for x in range(wins):
            card_to_add = self.cards[current_id+x].get_copy()
            self.cards.append(card_to_add)

    def process_cards(self):
        while self.current_game_id < self.max_id:
            for card in self.cards:
                if card.card_id == self.current_game_id:
                    wins = card.count_winnings()
                    self.add_copies(wins,self.current_game_id)

            self.current_game_id += 1
            print(f"currently at id : {self.current_game_id}")

        return len(self.cards)




def main():
    deck = Deck("data.txt")
    total_cards = deck.process_cards()
    print("Total Scratchcards:", total_cards)


if __name__ == "__main__":
    main()

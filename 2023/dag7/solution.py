def get_data(filepath):
    with open(filepath, "r") as file:
        content = file.readlines()
    hand , bid = [] , []
    for x in content:
        hand.append(x.strip("\n").split()[0])
        bid.append(x.strip("\n").split()[1])
    print(hand)
    return hand, bid

def value(hand):
    face_cards = {"2": 2, "3": 3, "4":4 , "5":5, "6":6 , "7": 7 , "8": 8 , "9": 9 , "T": 10 , "J":11, "Q": 12 , "K":13, "A": 14}
    hand_translated  =  {}
    hand_list = []
    for card in hand:
        if face_cards[card] in hand_translated:
            hand_translated[face_cards[card]] += 1
        else:
            hand_translated[face_cards[card]] = 1
        hand_list.append(face_cards[card])
    sorted_dict = dict(sorted(hand_translated.items(), key=lambda item: item[1],reverse=True))

    
    # print(hand_translated)
    # print(sorted_dict)
    highest_list = list(sorted_dict.values())
    if highest_list[0] == 5:
        hand_list.insert(0,7)
    elif highest_list[0] == 4:
        hand_list.insert(0,6)
    elif highest_list[0] == 3 and highest_list[1] == 2:
        hand_list.insert(0,5)
    elif highest_list[0] == 3 and highest_list[1] == 1:
        hand_list.insert(0,4)
    elif highest_list[0] == 2 and highest_list[1] == 2:
        hand_list.insert(0,3)
    elif highest_list[0] == 2 and highest_list[1] == 1:
        hand_list.insert(0,2)
    else:
        hand_list.insert(0,1)
    return hand_list

def custom_sort(hand):
    # currently replaced by the 'lambda' function. This is where the 'lambda' function is based on
    return tuple(hand[0])

def main():
    all_hands , all_bids = get_data("data.txt")
    all_hand_values = []
    for hand_index in range(len(all_hands)):
        hand = value(all_hands[hand_index])
        my_tuple = (hand ,int(all_bids[hand_index]))
        # print(my_tuple)
        all_hand_values.append(my_tuple)

    sorted_hands = sorted(all_hand_values, key=lambda x: tuple(x[0]))
    total_winnings = 0    
    for i,x in enumerate(sorted_hands):
        total_winnings += (i+1) * x[1]
    print(total_winnings)

if __name__ == "__main__":
    main()
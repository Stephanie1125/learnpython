import random
import doctest

def shuffle(cardstack):
    random.shuffle(cardstack)
# no return because cardstack is a list # pass by pointer

def check_racko(rack):
    """
    >>> check_racko([5,3,2,100])
    False
    >>> check_racko([5,3,1])
    True
    >>> check_racko([5,4,6])
    False
    """
    # i = 0
    # while(rack[i]>rack[i+1]):
    #     i += 1
    #     if i == len(rack)-1:
    #         return True
    # return False


    for i in range(len(rack)-1):
        if rack[i] < rack[i+1]:
            return False
    return True



def get_top_card(card_stack):
    x = card_stack.pop()
    return x

def deal_initial_hands(deck):
    computer = list()
    hand = list()
    i = 0
    for i in range(10):
    #while i < 10:
        computer.append(get_top_card(deck))
        hand.append(get_top_card(deck))
        #computer.insert(i,desk.pop())
        #hand.insert(i,desk.pop())
        #i += 1
    return computer,hand


def print_top_to_bottom(rack):
    i = 0
    #while(i<10):
    for i in range(10):
        print(rack[i])
        #i += 1

def find_and_replace(new_card, card_to_be_replaced, hand, discard):
   # s = set(hand)
    #if card_to_be_replaced in s:
        for x in range(len(hand)):
            if card_to_be_replaced == hand[x]:
                hand[x] = new_card
                add_card_to_discard(card_to_be_replaced, discard)
            elif(x == len(hand)-1):
                print('Please try again. Card number is not in the hand list')


def add_card_to_discard(card, discard):
    discard.__insert(0, card)

def exchange(seq,i,j):
    '''
    >>> seq = [0 ,1 ,2]
    >>> exchange(seq,0,2)
    >>> seq
    [2, 1, 0]
    '''
    seq[i], seq[j] = seq[j], seq[i]

def reverse_list(seq):
    '''
    >>> seq = [0,1,2,3]
    >>> reverse_list(seq)
    >>> seq
    [3, 2, 1, 0]

    >>> seq = [0,1,2]
    >>> reverse_list(seq)
    >>> seq
    [2, 1, 0]

    '''
    # for x in range(len(seq)):
    #     if x < len(seq)/2:
    #         exchange(seq,x,len(seq)-x-1)

    i = 0
    j = len(seq) - 1
    while i < j:
        exchange(seq, i, j)
        i += 1
        j -= 1


def computer_play(hand, deck, discard):
    pass


def main():
    deck = list(range(1,60))
    discard = []
    shuffle(deck)
    hands = deal_initial_hands()



    print_top_to_bottom(human_hand)

    while neither the computer nor the user has racko:
        computer_hand = computer_play(computer_hand, desk, discard)


        if user choose this card:

        elif choice == 'n':
            card = deck.pop()

            if secondChoice == 'y':

            else:
                discard.append(card)









if __name__ == '__main__':

    doctest.testmod(verbose=True)

"""В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html"""

import random


class PrintCard:
    def __init__(self, name_player, list_for_card):
        self.__list_card = list_for_card
        self.__name_player = name_player

    def __str__(self):
        return 'Card ' + self.__name_player + \
               ':\n' + '\n'.join('\t'.join(map(str, row)) for row in self.__list_card) + '\n\n'


class NewCard():
    def __init__(self, name_player):
        self.name_player = name_player
        self.__row = 3
        self.__count_numbers_in_row = 5
        self.__count_all_row = 9
        self.__count_numbers_in_card = self.__row * self.__count_numbers_in_row

    @property
    def card(self):
        uin_nambers = set()
        while len(uin_nambers) < self.__count_numbers_in_card:
            (uin_nambers.add(random.randint(1, 90)))
        uin_nambers = list(uin_nambers)
        list_card = [list(uin_nambers[0:(len(uin_nambers) // self.__row)]),
                     list(uin_nambers[(len(uin_nambers) // self.__row):2 * (len(uin_nambers) // self.__row)]),
                     list(uin_nambers[2 * (len(uin_nambers) // self.__row):len(uin_nambers)])]
        for j in range(len(list_card)):
            list_card[j].sort()
            for list_ in range((self.__count_all_row - self.__count_numbers_in_row)):
                list_card[j].insert(random.randint(0, len(list_card[j])), '')
        return list_card


class FindNumberInCard:
    def __init__(self, card1, card2, number):
        self.card1 = card1
        self.card2 = card2
        self._number = number
        self.num_card_1 = 0
        self.num_card_2 = 0

    @property
    def find_number(self):
        for j, n in enumerate(self.card1):
            # print (j, n)
            if self._number in n:
                n[n.index(self._number)] = '-'
                self.num_card_1 = 1

        for j, n in enumerate(self.card2):
            if self._number in n:
                n[n.index(self._number)] = '-'
                self.num_card_2 = 1
        return self.card1, self.num_card_1, self.card2, self.num_card_2


bag_with_barrels = [i for i in range(1, 91)]
player_1 = NewCard('Sergey')
player_2 = NewCard('Computer')
card_1 = player_1.card
card_2 = player_2.card
print(PrintCard(player_1.name_player, card_1))
print(PrintCard(player_2.name_player, card_2))
count_find_1 = 0
count_find_2 = 0
flag_break = False


while True:
    if count_find_1 == 15:
        print(f'Win {player_1.name_player}')
        break
    if count_find_2 == 15:
        print(f'Win {player_2.name_player}')
        break
    barrels_in_bag = random.choice(bag_with_barrels)
    bag_with_barrels.remove(barrels_in_bag)
    print(f'Barrel - {barrels_in_bag}: {len(bag_with_barrels)} barrels left\n')
    flag = input(f'Remove barrels - {barrels_in_bag} from card y/n : ')
    while True:
        if flag == 'y' or flag == 'n':
            find_in_cards = FindNumberInCard(card_1, card_2, barrels_in_bag)
            card_1, n_f_1, card_2, n_f_2 = find_in_cards.find_number
            if (flag == 'y' and n_f_1 == 0) or (flag == 'n' and n_f_1 == 1):
                print(f'{player_1.name_player} is fail')
                flag_break = True
                break
            count_find_1 += n_f_1
            count_find_2 += n_f_2
            print(PrintCard(player_1.name_player, card_1))
            print(PrintCard(player_2.name_player, card_2))
            break
        else:
            print(PrintCard(player_1.name_player, card_1))
            print(PrintCard(player_2.name_player, card_2))
            print('Input "n" or "y" ')
            print(f'Barrel : {barrels_in_bag}, {len(bag_with_barrels)} barrels left\n')
            flag = input(f'Remove barrels - {barrels_in_bag} from card y/n : ')

    if flag_break:
        break

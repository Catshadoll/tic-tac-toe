win_state = False
playing_field = list(range(1, 10))
counter = 0
all_win_coords = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
)

while not win_state:
    if counter % 2 == 0:
        player = "0"
    else:
        player = "X"
    print(f"Ход игрока {player}")
    for num in range(0, 7, 3):
        print(f"| {playing_field[num]} | {playing_field[num + 1]} | {playing_field[num + 2]} |")

    valid = False

    while not valid:
        position = int(input(f"Куда хотите поставить {player}?"))

        if playing_field[position - 1] not in ["X", "0"]:
            valid = True
            playing_field[position - 1] = player
        else:
            print("клетка уже занятка!")

    counter += 1

    if counter >= 3:
        for coords in all_win_coords:
            one_win_coord, two_win_coord, three_win_coord = coords
            if playing_field[one_win_coord] == playing_field[two_win_coord] == playing_field[three_win_coord]:
                print(f"Поздравляем, победил игрок {player}. Игра окончена!")
                win_state = True
                break

        if counter == 9 and not win_state:
            print("Ничья!")
            win_state = True
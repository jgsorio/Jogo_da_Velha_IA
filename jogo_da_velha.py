import random


def create_body():
    return [' ' for x in range(10)]


def draw_body(body):
    print(f'   |   |   ')
    print(f' {body[1]} | {body[2]} | {body[3]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {body[4]} | {body[5]} | {body[6]} ')
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(f' {body[7]} | {body[8]} | {body[9]} ')
    print('   |   |   ')
    print('\n')


def insert_letter(letter, position, body):
    if verify_if_empty_position(position, body):
        body[position] = letter
        draw_body(body)
    else:
        print('Essa posição já foi escolhida!')
        position = int(input('Digite a posição que deseja jogar 1 a 9: '))
        insert_letter('x', position, body)


def player_time(body):
    run = True
    while run:
        try:
            choice = int(input('Escolha um numero entre 1 e 9 '))
            if choice <= 0 or choice >= 10:
                print('Por favor digite um numero entre 1 e 9 ')
            else:
                insert_letter('x', choice, body)
                run = False
        except:
            print('Por favor digite um numero válido')


def ai_time(body):
    run = True
    while run:
        choice = play_ia_choice(body)
        if verify_if_empty_position(choice, body):
            run = False
            insert_letter('o', choice, body)
            print(f'IA escolhe a posicao {choice}')


def verify_if_empty_position(position, body):
    return body[position] == ' '


def play_ia_choice(body):
    for (indice, i) in enumerate(body):
        if i == 'x':
            posibilities = posible_combinations()
            for posibility in posibilities:
                if indice in posibility:
                    count = 0
                    for x in posibility:
                        if body[x] == 'x':
                            count += 1
                    if count == 2:
                        for position in posibility:
                            if body[position] == ' ':
                                return position
            choice = random.choice(random.choice(posibilities))
            return choice


def posible_combinations():
    return [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def verify_won(body, letter):
    if body[1] == letter and body[2] == letter and body[3] == letter:
        return True
    elif body[4] == letter and body[5] == letter and body[6] == letter:
        return True
    elif body[7] == letter and body[8] == letter and body[9] == letter:
        return True
    elif body[1] == letter and body[4] == letter and body[7] == letter:
        return True
    elif body[2] == letter and body[5] == letter and body[8] == letter:
        return True
    elif body[3] == letter and body[6] == letter and body[9] == letter:
        return True
    elif body[1] == letter and body[5] == letter and body[9] == letter:
        return True
    elif body[3] == letter and body[5] == letter and body[7] == letter:
        return True
    else:
        return False


def body_is_not_complete(body):
    return body.count(' ') > 1


def play_again():
    answer = input('Gostaria de jogar novamente? Digite s ou n')
    if answer.lower() == 's':
        game()
    else:
        exit()


def game():
    body = create_body()
    draw_body(body)
    while body_is_not_complete(body):
        player_time(body)
        if verify_won(body, 'x'):
            print('Parabéns você ganhou!')
            play_again()
        ai_time(body)
        if verify_won(body, 'o'):
            print('O computador ganhou!')
            play_again()
        if body.count(' ') == 2:
            print('Humm, parece que deu empate')
            play_again()


game()

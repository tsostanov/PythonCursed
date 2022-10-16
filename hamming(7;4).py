def hamming(n):
    r_1, r_2, i_1, r_3, i_2, i_3, i_4 = [int(x) for x in str(n)]
    return int((str((r_1 + i_1 + i_2 + i_4) % 2)
                + str((r_2 + i_1 + i_3 + i_4) % 2) + str((r_3 + i_2 + i_3 + i_4) % 2))[::-1], 2)

message = input()
if len(message) == 7 and (message.count('0') + message.count('1')) == 7:
    incorrect = hamming(message)
    if incorrect == 0:
        print('В сообщении нет ошибок')
    else:
        correct_message = ''
        for i in range(len(message)):
            correct_message += str((int(message[i]) + (i == (incorrect - 1)) * 1) % 2)
        print('В сообщении была ошибка в ' + str(incorrect) + ' бите. Правильное сообщение: ' + correct_message)
else:
    print('Неверный формат ввода')


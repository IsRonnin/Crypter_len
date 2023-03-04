import pyperclip as clipboard
msg = clipboard.paste()

str_to_char = lambda string: [ord(i)+len(string) for i in string] # функция перевода в список 
char_to_str = lambda char_list, string='': string.join([chr(i-len(char_list)) for i in char_list]) # функция перевода из списка в строку


l_msg = [int(ki) for ki in ''.join([i for i in msg if i not in ['[', ']', ',']]).split(' ')]
print('Расшифровка:', char_to_str(l_msg))

s_msg = str(input('Сообщение: '))
if s_msg != '':
    clipboard.copy(str((str_to_char(s_msg))))




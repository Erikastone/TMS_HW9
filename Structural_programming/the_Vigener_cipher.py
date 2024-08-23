#Программа получает на вход строку – сообщение и
#указание, что нужно сделать: шифровать или дешифровать.
#Реализовать две функции: первая шифрует заданное сообщение
#шифром Виженера, вторая – расшифровывает. В зависимости от
#выбора пользователя (шифровать или дешифровать) вызывается
#соответствующая функция, результат выводится в консоль
def vigener (text, key, mode="encrypt"):
    resul=""
    #приводим ключ к той же длинне как и сообщение
    key *=len(text) // len(key) + 1
    #проходимся по каждой букве в сообщении
    for i, char in enumerate(text):
        if char.isalpha():
            # получаем индекс текущей буквы
            text_index = ord(char.upper()) - ord('A')
            # получаем индекс текущей буквы ключа
            key_index = ord(key[i].upper()) - ord('A')
            # Вычесляем индекс зашифрованной/расшифрованной буквы
            if mode == "encrypt":
                encriphered_index = (text_index + key_index) % 26
            else:
                encriphered_index = (text_index - key_index) % 26               
                # преобразовать индекс обратно в букву
            resul += chr(encriphered_index + ord('A'))
        else:
            # если символ не буква, то оставим его без изменения
            resul += char    
    return resul  

message = "LEMON"  
key = "POYBF"

encript = vigener(message, key, mode="encrypt")
print(f"Зашифрованное сообщение: {encript}")
decript = vigener(encript, key, mode="decrypt")  
print(f"Расшифровка сообщения: {decript}")  
            
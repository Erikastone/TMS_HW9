#Программа получает на вход строку – сообщение и
#указание, что нужно сделать: шифровать или дешифровать.
#Реализовать две функции: первая шифрует заданное сообщение
#шифром Цезаря, вторая – расшифровывает. В зависимости от
#выбора пользователя (шифровать или дешифровать) вызывается
#соответствующая функция, результат выводится в консоль
def caesar(smeshenie,message,en_dec):
    alfavit =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    itog =''
    if en_dec == 'шифр':
        for i in message:
            plase = alfavit.find(i)
            new_plase = plase + smeshenie
            if i in alfavit:
                itog +=alfavit[new_plase]
            else:
                itog += i              
        print(itog)
    else:
        for i in message:
            plase = alfavit.find(i)
            new_plase = plase - smeshenie
            if i in alfavit:
                itog +=alfavit[new_plase]
            else:
                itog += i              
        print(itog)   
    
message = input("Введите сообщение для шифровки или дешифровки: ").upper()
smesh = int(input("Введите шаг шифровки: "))
encrypt_decrypt = input("Шифровать? или Дешифровать?: пропишите нужное (шифр) или (дешифр): ").lower() 
print(caesar(smesh,message,encrypt_decrypt))                         
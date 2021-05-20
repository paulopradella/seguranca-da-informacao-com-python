import phonenumbers

from phonenumbers import  geocoder

phone = input('Digite o telefone no formato internacional: +000000000000:\n')

phone_number = phonenumbers.parse(phone)

print(' O número:' , phone, ' é do(a):', geocoder.description_for_number(phone_number, 'pt'))
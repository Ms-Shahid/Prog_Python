import phonenumbers

from phonenumbers import carrier
from phonenumbers import geocoder

#now enter the number with country code

phone_number = phonenumbers.parse('+919606322007')

#this will print country code


print('country is :', geocoder.description_for_number(phone_number, 'en'))

#this will print service provider

print('Service provider is :',carrier.name_for_number(phone_number, 'en'))
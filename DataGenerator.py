import csv
import random
import time
from faker import Faker
from faker.providers.person.es_CO import Provider
start_time = time.mktime(time.strptime("01/01/2023 00:00:00", "%d/%m/%Y %H:%M:%S"))
end_time = time.mktime(time.strptime("03/04/2023 23:59:59", "%d/%m/%Y %H:%M:%S"))
fake = Faker('es_ES') #el argumento de entrada puede ser reemplazado, leer más: https://github.com/joke2k/faker/tree/master/faker/providers/person
fake.add_provider(Provider)
with open("C:/Users/jaburto/Documents/SQL/PYTHON/nombres.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter="|")
    for _ in range(100): #número de registros que se desea generar
        random_time = random.uniform(start_time, end_time)
        fecha = time.strftime("%Y%m%d%H%M%S", time.localtime(random_time))
        imsi = "71620" + "".join(random.choice("0123456789") for _ in range(10))
        num = "97" + "".join(random.choice("0123456789") for _ in range(7)) 
        dni = "6" + "".join(random.choice("0123456789") for _ in range(7)) 
        writer.writerow([fake.first_name(), fake.last_name(),fake.last_name(),num,dni,imsi,fecha]) #comentar esta línea si se desea imprimir en consola
        #print(fake.numerify('%3#######'),fake.first_name(), fake.last_name(),fake.last_name(),num,dni,imsi,fecha) #descomentar esta línea si se desea imprimir en consola

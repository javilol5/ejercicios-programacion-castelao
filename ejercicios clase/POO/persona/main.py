from datetime import datetime

from persona import Persona

persona1 = Persona("Carlos", "12345678Z", "03/12345678/90", "+34 123 456 789", datetime(2025,12,12,8,30), datetime(2025,12,12,16,30))
persona2 = Persona("Pepe","12345678Z", "12/12345678/90", "+34 123 234 345", datetime(2025,12,12,8,30), datetime(2025, 12, 12, 10, 20))

print(persona1.__eq__(persona2))
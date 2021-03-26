from MouseClass import Mouse

mice1 = Mouse("Alise", "Phantom", 16000, 5000, 69, 12500)
mice2 = Mouse("Alise", "Decibel", 8000, 1000, 122, 4500)
print(mice1.weight)
print(mice2.weight)

print(mice1.is_ultra_light())
print(mice2.is_ultra_light())
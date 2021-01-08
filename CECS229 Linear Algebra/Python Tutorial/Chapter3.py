bicycles = ["trek", "cannondale", "redline", "specialized"]
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[-2])

message = "My first bicycle was a " + bicycles[0] + "."
print(message)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles[0] = 'honda'
motorcycles.append('ducati')
print(motorcycles)


cars = []
cars.append('honda')
cars.append('toyota')
cars.append('lamborghini')
cars.insert(0, 'ford')
print(cars)

del cars[0]
print(cars)

print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)


cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)
print(len(cars))



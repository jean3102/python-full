import random

friends = ["juan", "pedro", "maria", "marta", "Bob", "Marcos"]

# 1 option
random_index = random.randint(0, 5)
print(friends[random_index])

# 2 option
print(random.choice(friends))

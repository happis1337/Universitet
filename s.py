import random
from main.models import Ustoz

random_son = random.randint(1, 100)

ustozlar = Ustoz.objects.filter(yosh__lt=random_son)

print(f"Random son: {random_son}")
print(f"Yoshi {random_son} dan kichik bo'lgan ustozlar:")
for ustoz in ustozlar:
    print(ustoz.ism, ustoz.yosh)
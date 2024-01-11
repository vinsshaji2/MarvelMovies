import os
from django.core.files import File
from io import BytesIO
from PIL import Image

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "MovieMarvel.settings")

import django
django.setup()
from faker import Faker
from adminpanel.models import seats

fakergen = Faker()


def addurls():
    characters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]  # Characters from A to Z

    for char in characters:
        for seat_number in range(1, 11):  # Assuming you want 10 seats for each character
            # Create the product object with the updated seat_name
            seat_name = f"{char}{seat_number}"
            product_obj, created = seats.objects.get_or_create(seat_name=seat_name)

            if created:
                print(f"Created: {seat_name}")
            else:
                print(f"Already existed: {seat_name}")


if __name__ == "__main__":
    print("Populating")
    addurls()
    print("Finished")

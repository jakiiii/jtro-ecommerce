import os
import random
from django.utils.crypto import get_random_string


def get_filename_exist(file_path):
    base_name = os.path.basename(file_path)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, file_name):
    new_filename = random.randint(1, 101119)
    name, ext = get_filename_exist(file_name)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


def generate_eight_digit_random_product_id():
    return get_random_string(length=8, allowed_chars='0123456789ABCDEFGHIJKLMONPQRSTUVWXYZ')

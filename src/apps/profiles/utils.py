from PIL import Image
import random
import os
from django.conf import settings


def get_filename_extension(filename):
    baseName = os.path.basename(filename)
    name, ext = os.path.splitext(baseName)
    return name, ext


def default_avatar_image_path():
    _default_dr = os.path.join(settings.MEDIA_ROOT, 'avatars', 'default')
    if not os.path.isdir(_default_dr):
        os.mkdir(_default_dr)
    items = os.listdir(_default_dr)
    items_count = len(items)

    selected_item = None
    rel_path = os.path.join('avatars', 'default')
    if items_count > 0:
        selected_item = items.pop(random.randint(0, items_count - 1))
    if selected_item:
        return rel_path + "/" + str(selected_item)
    else:
        raise FileNotFoundError


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 999999999999999999999)
    name, ext = get_filename_extension(filename)
    final_filename = f'{new_filename}{ext}'
    return f'avatars/{instance.username}', f'avatars/{instance.username}/{final_filename}'

def upload_direct_avatar_with_model(instance, filename):
    new_filename = random.randint(1, 999999999999999999999)
    name, ext = get_filename_extension(filename)
    final_filename = f'{new_filename}{ext}'
    return f'avatars/{instance.username}/{final_filename}'



def update_avatar_image(instance, filename):
    img = Image.open(filename)
    directory, directory_with_image = upload_image_path(instance, filename.name)
    abs_directory = os.path.abspath(os.path.join(settings.MEDIA_ROOT, directory))
    abs_directory_image = os.path.abspath(os.path.join(settings.MEDIA_ROOT, directory_with_image))
    if not os.path.isdir(abs_directory):
        os.mkdir(abs_directory)
    img.save(abs_directory_image)
    instance.profile.avatar = directory_with_image
    instance.profile.save()
    if instance.profile.avatar == directory_with_image:
        return True
    return False
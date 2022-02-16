from django.core.validators import ValidationError
from io import BytesIO
import requests

image_extentions = ('.png', '.jpg', '.gif', '.svg')


def get_cleaned_image_name(url):
    cleaned_name = url.split('/')[-1]
    return cleaned_name


def save_image():
    ...


def get_image_from_url(url):
    resp = requests.get(url)
    if resp.status_code != requests.codes.ok:
        raise ValidationError(message="Can't connect to URL")
    fp = BytesIO()
    file_name = get_cleaned_image_name(url)
    fp.write(resp.content)

    return file_name, fp


# TODO: take into account redirect, html
def check_mimetypes(url):
    """ Image-URL should appropriate current extensions"""
    ...

from PIL import Image, ImageFont, ImageDraw, GifImagePlugin
import io
import requests
import random

def compile(data):
    arr = io.BytesIO()
    data.save(arr, format='PNG')
    arr.seek(0)
    return arr

def imagefromURL(url):
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    return image
    return data

def urltoimage(url):
    image = imagefromURL(url)
    data = compile(image)
    return data

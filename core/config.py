from random import choice
from os import getenv
from dotenv import load_dotenv
load_dotenv()

TOKEN = getenv("token")
ADMIN_ID = "1310237124"
API = getenv("API")

list_image = [
    "AgACAgIAAxkBAANEZRVL9Pagy7HnR7Zs7CUWpF0AASwjAAIQzTEbg2CwSDYcd3Iqkrk5AQADAgADbQADMAQ",
    "AgACAgIAAxkBAANGZRVME1oYDPbWYU4FNgooHhylt7IAAhHNMRuDYLBITnZ6ZYL1A-UBAAMCAANtAAMwBA",
    "AgACAgIAAxkBAANSZRVMdE5bEJE2rzyIKQ4QwsqsatEAAhTNMRuDYLBI5ckcTvPw3TIBAAMCAAN4AAMwBA"
]

IMAGE = choice(list_image)
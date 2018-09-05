import api
import json
from rgbmatrix import RGBMatrix, RGBMatrixOptions

with open('config.json', 'r') as f:
    config = json.load(f)

# access config
currencies = config['currencies']
displayedcurrencies = config['displayedcurrencies']

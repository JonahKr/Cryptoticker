from samplebase import SampleBase
from rgbmatrix import graphics
import time
import api
import json


with open('config.json', 'r') as f:
    config = json.load(f)
    fiatcurrencies = config['fiatcurrencies']
    cryptocurrencies = config['cryptocurrencies']

class RunText(SampleBase):

    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

        print ""
        print " \t\t\t\t~~~~~~~~~~ starting Setup ~~~~~~~~~~ "
        print ""
        self.cryptocurrencies = api.getCryptoProve(cryptocurrencies)
        self.fiatcurrencies = api.getFiatProve(fiatcurrencies)
        self.cryptoids = api.getCryptoId(self.cryptocurrencies)
        self.data = api.getCurrencyPriceById(self.cryptoids, self.fiatcurrencies)
        self.change24h = api.get24hChange(self.cryptoids)
        self.change1h = api.get1hChange(self.cryptoids)
        self.change7d = api.get7dChange(self.cryptoids)
        self.green = graphics.Color(0,255,0)
        self.red = graphics.Color(255,0,0)

        print ""
        print " \t\t\t\t~~~~~~~~~~ Setup complete ~~~~~~~~~~ "
        print ""

    def updateData():
        self.data = api.getCurrencyPriceById(self.cryptocurrencies, self.fiatcurrencies)
        self.change24h = api.get24hChange(self.cryptoids)
        self.change1h = api.get1hChange(self.cryptoids)
        self.change7d = api.get7dChange(self.cryptoids)


    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("./fonts/10x20.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = "Nothing found - An error occured"
        my_text = ""
        counter = 0
        for cc in self.cryptocurrencies:
            my_text += cc+":"
            for fc in self.fiatcurrencies:
                price = self.data[self.cryptoids[counter]][str( fc)]
                my_text += str(price)+"-"
                my_text += str(fc)+"   "
            counter = counter +1



        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 23, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.04)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()

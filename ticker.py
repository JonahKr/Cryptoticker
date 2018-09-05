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

        self.cryptocurrencies = api.getCryptoProve(config["cryptocurrencies"])
        self.fiatcurrencies = fiatcurrencies
        self.cryptoids = api.getCryptoId(self.cryptocurrencies)
        self.data = api.getCurrencyPriceById(self.cryptoids, self.fiatcurrencies)
        print "Setup complete"
        print "Dataset:"
        print str(self.data)

    def updateData():
        self.data = api.getCurrencyPriceById(self.cryptocurrencies, self.fiatcurrencies)
        print data

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("./fonts/7x13.bdf")
        textColor = graphics.Color(255, 255, 0)
        pos = offscreen_canvas.width
        my_text = "Nothing found - An error occured"
        try:
            mytext = ""
            for cc in self.cryptocurrencies:
                mytext += cc+":"
                print mytext
                counter = 0
                print "secloop"
                for fc in self.fiatcurrencies:
                    print "in sec loop"
                    print str(fc)
                    print str(self.cryptoids[counter])
                    price = self.data[self.cryptoids[counter]][str(fc)]
                    print str(price)
                    mytext += str(self.data[str(self.cryptoids[counter])][fc]+" - "+fc+", ")
                    mytext += " - "+str(fc)
                    print mytext
                    counter = counter +1
                mytext += "   "

        except Exception as e:
    		print str(e)


        while True:
            offscreen_canvas.Clear()
            len = graphics.DrawText(offscreen_canvas, font, pos, 10, textColor, my_text)
            pos -= 1
            if (pos + len < 0):
                pos = offscreen_canvas.width

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)


# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()

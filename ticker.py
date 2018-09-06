from samplebase import SampleBase
from rgbmatrix import graphics
from threading import Thread
import datetime
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
        self.blue = graphics.Color(0,0,255)
        self.green = graphics.Color(0,255,0)
        self.red = graphics.Color(255,0,0)
        self.grey = graphics.Color(130,130,130)
        self.yellow = graphics.Color(255,255,0)

        print ""
        print " \t\t\t\t~~~~~~~~~~ Setup complete ~~~~~~~~~~ "
        print ""


    def run(self):
        print "Startup :"
        #updating data
        self.data = api.getCurrencyPriceById(self.cryptoids, self.fiatcurrencies)
        self.change24h = api.get24hChange(self.cryptoids)

        #Sleepmode
        startup_time = datetime.time(hour=8)
        shutdown_time = datetime.time(hour=23,minute=59)
        now = (datetime.datetime.now() - datetime.timedelta(hours=1)).time()

        while startup_time < now <shutdown_time:
            print ".\t Timelock enabled"
            #display Setup
            offscreen_canvas = self.matrix.CreateFrameCanvas()
            font = graphics.Font()
            font.LoadFont("./fonts/10x20.bdf")
            textColor = graphics.Color(255, 255, 0)
            pos = offscreen_canvas.width
            print ".\t Pannels setup"
            #end display Setup

            print("Press CTRL-C to stop programm")

            for x,cc in enumerate(self.cryptocurrencies):

                colors=[]

                change = ""+str(self.change24h[self.cryptoids[x]])+""
                if (float(change)>0.00):
                    colors.append(self.green)
                    change += "% "
                if (float(change)==0.00):
                    colors.append(self.grey)
                    change += "%"
                if (float(change)<0.00):
                    colors.append(self.red)
                    change += "% "
                price = ""
                for fc in self.fiatcurrencies:
                    price += str(self.data[self.cryptoids[x]][fc])+" "
                    price += str(fc)+"   "



                while True:
                    offscreen_canvas.Clear()
                    sum = 0
                    #cryptocurrency
                    sum = sum + graphics.DrawText(offscreen_canvas, font , pos, 23, self.yellow, cc+" ")
                    # changing
                    sum= sum + graphics.DrawText(offscreen_canvas, font , pos + sum, 23, colors[x], change )
                    #price in FCs
                    sum = sum + graphics.DrawText(offscreen_canvas, font , pos +sum , 23, self.blue, price)
                    pos -= 1

                    if (pos + sum - 15 < 0):
                        pos = offscreen_canvas.width
                        break

                    time.sleep(0.04)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()

from samplebase import SampleBase
from rgbmatrix import graphics
from threading import Thread
from PIL import Image
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
        self.iterationcounter = 0
        self.image = Image.open("./images/bc_logo.png").convert('RGB')
        self.image.resize((32*8, 32), Image.ANTIALIAS)


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
            if self.iterationcounter ==3:
                self.iterationcounter =1
            elif self.iterationcounter == 0:
                print ".\t Timelock enabled"
                #display Setup
                offscreen_canvas = self.matrix.CreateFrameCanvas()
                font = graphics.Font()
                font.LoadFont("./fonts/10x20.bdf")
                textColor = graphics.Color(255, 255, 0)
                print ".\t Pannels setup"
                print("Press CTRL-C to stop programm")
                #end display Setup
                self.iterationcounter +=1
            else:
                self.iterationcounter = +1

            pos = offscreen_canvas.width

            img_width, img_height = self.image.size

            for x,cc in enumerate(self.cryptocurrencies):

                change = ""+str(self.change24h[self.cryptoids[x]])+""
                if float(change)> 0.0:
                    color=self.green
                    change = "+"+change+"%"
                elif float(change)< 0.0:
                    color=self.red
                    change += "% "
                else:
                    color=self.grey
                    change += "%"

                price = ""
                for fc in self.fiatcurrencies:
                    price += str(self.data[self.cryptoids[x]][fc])+" "
                    price += str(fc)+"  "
                xpos = 0
                while True:
                    xpos += 1
                    if(xpos >    img_width):
                        xpos = 0
                    offscreen_canvas.Clear()
                    sum = 0
                    #cryptocurrency
                    sum = sum + graphics.DrawText(offscreen_canvas, font , pos, 23, self.yellow, cc+":")
                    # changing
                    sum= sum + graphics.DrawText(offscreen_canvas, font , pos + sum, 23, color, change+" " )
                    #price in FCs
                    sum = sum + graphics.DrawText(offscreen_canvas, font , pos +sum , 23, self.blue, price)
                    if (self.iterationcounter == 2):

                        offscreen_canvas.SetImage(self.image,-xpos)
                        offscreen_canvas.SetImage(self.image, -xpos + img_width)
                    else:
                        img_width = 0
                    pos -= 1

                    if (pos + sum + img_width < 0):
                        pos = offscreen_canvas.width
                        break

                    time.sleep(0.03)
                    offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)




# Main function
if __name__ == "__main__":
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()

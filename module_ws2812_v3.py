# Module WS2812 V1.01
import time
import module_neopixel
from module_init import Global_WS2812 as MyGlobal
from machine import Pin

sel_1 = Pin(MyGlobal.sel_pin_1,Pin.OUT)
sel_2 = Pin(MyGlobal.sel_pin_2,Pin.OUT)

class LedState:
    def __init__(self):
        self.state = False
        self.blink_state = False

    def set(self, set):
        self.state = set

    def get(self):
        return self.state
    
    def do_blink(self):
        self.blink_state = not self.blink_state

    def get_blink(self):
        return self.blink_state

    def refresh(self):
        self.state = False
        for strips in strip_obj:
            strips.show()


class Ledsegment:

    def __init__(self, neopixel, start, count):
        self.neopixel = neopixel
        self.start = start
        self.stop = self.start + count - 1
        self.count = count
        self.position = 0
        self.run_state = False
        self.blink_state = False
        self.color_on = (0,0,0)
        self.color_default = (0,0,0)
        self.color_off = (0,0,0)
        self.color_blink_on = (0,0,0)
        self.color_blink_off = (0,0,0)
        self.color_show = (0,0,0)
        self.color_value = (0,0,0)

    def set_color_on(self, color_on):
        self.color_on = color_on

    def set_color_def(self, color_default):
        self.color_default = color_default
        
    def set_color_off(self, color_off):
        self.color_off = color_off

    def set_color_value(self, color_value):
        self.color_value = color_value

    def set_color_show(self, color_value):
        self.color_show = color_value

    def set_color_blink_off(self, color_value):
        self.color_blink_off = color_value

    def set_color_blink_on(self, color_value):
        self.color_blink_on = color_value

    def set_pixel(self, pixel_num, color=None):
        if color:
            self.color_value = color
        else:
            self.color_value = self.color_show
        self.neopixel.set_pixel(self.start + pixel_num, self.color_value)

    def show_on(self):
        self.color_show = self.color_on
        self.blink_state = False
        self.set_line()

    def show_def(self):
        self.color_show = self.color_default
        self.blink_state = False
        self.set_line()

    def show_off(self):
        self.color_show = self.color_off
        self.blink_state = False
        self.set_line()

    def show_blink(self):
        self.blink_state = True
        if ledstate.get_blink():
            self.color_show = self.color_blink_on
        else:
            self.color_show = self.color_blink_off
        self.set_line()

    def get_blink_state(self):
        return self.blink_state

    def set_line(self):
        self.neopixel.set_pixel_line(self.start, self.stop, self.color_show)

    def show_stripe(self):
        self.neopixel.show()

###############################################################################
### Setup
###############################################################################
def setup_ws2812():

    global strip_obj
    global led_obj
    global ledstate
    global mg
    
    mg = MyGlobal
    
    led_obj = []
    strip_obj = []

    ledstate = LedState()
    
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_1, 0, 2, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_2, 1, 3, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_3, 2, 4, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_4, 3, 5, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_5, 4, 6, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_6, 5, 7, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_7, 6, 8, "GRB"))
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_8, 7, 9, "GRB"))
    
    for strips in strip_obj:
        strips.brightness(255)
   
    # Alle Leds auf Vorgabewert -> aus
    for strips in strip_obj:
        strips.set_pixel_line(0, strips.num_leds - 1, mg.color_off)
    for strips in strip_obj:
        strips.show()


def test_stripe():                                # Pro Stripe einmal Aus-RGB(25%) -Aus 
    
    # strip_obj[0].set_pixel_line(0, strip_obj[0].num_leds - 1, ( 40,  0,  0))
    # strip_obj[1].set_pixel_line(0, strip_obj[1].num_leds - 1, (  0, 40,  0))
    # strip_obj[2].set_pixel_line(0, strip_obj[2].num_leds - 1, (  0,  0, 40))
    # strip_obj[3].set_pixel_line(0, strip_obj[3].num_leds - 1, ( 30, 30,  0))
    # strip_obj[4].set_pixel_line(0, strip_obj[4].num_leds - 1, ( 20,  0, 30))
    # strip_obj[5].set_pixel_line(0, strip_obj[5].num_leds - 1, (  0, 30, 20))
    # strip_obj[6].set_pixel_line(0, strip_obj[6].num_leds - 1, ( 30, 30, 30))
    # strip_obj[7].set_pixel_line(0, strip_obj[7].num_leds - 1, (  5,  5, 10))

    strip_obj[0].set_pixel_line(0, strip_obj[0].num_leds - 1, MyGlobal.color_def)
    strip_obj[1].set_pixel_line(0, strip_obj[1].num_leds - 1, MyGlobal.color_def)
    strip_obj[2].set_pixel_line(0, strip_obj[2].num_leds - 1, MyGlobal.color_def)
    strip_obj[3].set_pixel_line(0, strip_obj[3].num_leds - 1, MyGlobal.color_def)
    strip_obj[4].set_pixel_line(0, strip_obj[4].num_leds - 1, MyGlobal.color_def)
    strip_obj[5].set_pixel_line(0, strip_obj[5].num_leds - 1, MyGlobal.color_def)
    strip_obj[6].set_pixel_line(0, strip_obj[6].num_leds - 1, MyGlobal.color_anim_0)
    strip_obj[7].set_pixel_line(0, strip_obj[7].num_leds - 1, MyGlobal.color_def)

    strip_obj[6].set_pixel(4, MyGlobal.color_anim_1)
    strip_obj[6].set_pixel(5, MyGlobal.color_anim_2)
    strip_obj[6].set_pixel(6, MyGlobal.color_anim_1)

    for i in range(0,8):
        strip_obj[i].show()

    time.sleep(0.3)

def test_rotate():
    for i in range(0,8):
        strip_obj[i].fill((0,10,10))
        strip_obj[i].set_pixel(0,(20,80,80))
        strip_obj[i].set_pixel(1,(50,255,255))
        strip_obj[i].set_pixel(2,(20,80,80))
        strip_obj[i].show()

    #time.sleep(0.3)
    

    loop = 0
    while loop < 100:
        for i in range(0,8):
            strip_obj[i].rotate_right(1)
            strip_obj[i].show()
        
        time.sleep(0.02)
        loop = loop + 1

def main():
    
    sel_1.value(0)

    print("WS2812 -> Setup")
    setup_ws2812()
        
    #print("WS2812 -> Run self test")
    #test_stripe()
    
    print("WS2812 -> Rotate Test")
    test_stripe()

    sel_1.value(0)

    time.sleep(3)

    # strip_obj[0].fill((20,0,10))
    # strip_obj[0].set_pixel(0,(80,10,80))
    # strip_obj[0].set_pixel(1,(255,255,255))
    # strip_obj[0].set_pixel(2,(80,10,80))
    # strip_obj[0].show()

    time.sleep(1)

    sel_1.value(0)

    # test_rotate()

  
    print("WS2812 -> End of Program !!!")

# End

#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

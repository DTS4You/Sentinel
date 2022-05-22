# Module WS2812 V1.01
import time
import module_neopixel
from module_init import Global_WS2812 as MyGlobal
from machine import Pin

sel_1 = Pin(MyGlobal.sel_pin_1,Pin.OUT)
sel_2 = Pin(MyGlobal.sel_pin_2,Pin.OUT)

class LedState:
    def __init__(self, led_counts, direction, offset):
        self.anim_state = False
        self.led_counts = led_counts
        self.direction = direction
        self.offset = offset

    def set_anim(self, set):
        self.anim_state = set

    def get_anim(self):
        return self.anim_state
    
    def set_direction(self, direction):
        self.direction = direction

    def get_direction(self):
        return self.direction

###############################################################################
### Setup
###############################################################################
def setup_ws2812():

    sel_1.value(0)

    global strip_obj
    global strip_state
    global mg
    
    mg = MyGlobal
    
    strip_state = []
    strip_obj = []

    strip_state.append(LedState(mg.numpix_1, mg.anim_0_dir, mg.anim_offset_0))        # 1
    strip_state.append(LedState(mg.numpix_2, mg.anim_1_dir, mg.anim_offset_1))        # 2
    strip_state.append(LedState(mg.numpix_3, mg.anim_2_dir, mg.anim_offset_2))        # 3
    strip_state.append(LedState(mg.numpix_4, mg.anim_3_dir, mg.anim_offset_3))        # 4
    strip_state.append(LedState(mg.numpix_5, mg.anim_4_dir, mg.anim_offset_4))        # 5
    strip_state.append(LedState(mg.numpix_6, mg.anim_5_dir, mg.anim_offset_5))        # 6
    
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_1, 0, 2, "GRB"))    # 1
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_2, 1, 3, "GRB"))    # 2
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_3, 2, 4, "GRB"))    # 3
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_4, 3, 5, "GRB"))    # 4
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_5, 4, 6, "GRB"))    # 5
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_6, 5, 7, "GRB"))    # 6
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_7, 6, 8, "GRB"))    # 7 -> n.B.
    strip_obj.append(module_neopixel.Neopixel(mg.numpix_8, 7, 9, "GRB"))    # 8 -> n.B.
    
    

    for stripes in strip_obj:
        stripes.brightness(255)
   
    # Alle Leds auf Vorgabewert -> aus
    for stripes in strip_obj:
        stripes.set_pixel_line(0, stripes.num_leds - 1, mg.color_off)
    for stripes in strip_obj:
        stripes.show()
#------------------------------------------------------------------------------

def do_all_off():
    # Setze Farbwerte in alle LED-Objekte
    anim_stop_all()
    for stripes in strip_obj:
        stripes.fill(mg.color_off)
    do_refresh()

def do_all_def():
    # Setze Farbwerte in alle LED-Objekte
    anim_stop_all()
    for stripes in strip_obj:
        stripes.fill(mg.color_def)
    do_refresh()

def do_all_on():
    # Setze Farbwerte in alle LED-Objekte
    anim_stop_all()
    for stripes in strip_obj:
        stripes.fill(mg.color_on)
    do_refresh()

def do_refresh():
    for stripes in strip_obj:
        stripes.show()

def anim_startup(value):
    strip_state[value].set_anim(True)
    strip_obj[value].fill(MyGlobal.color_anim_0)
    num_pix = strip_state[value].led_counts
    repeat_pix = int(num_pix / MyGlobal.anim_counts)
    for i in range(0,MyGlobal.anim_counts):
        print(i * repeat_pix)
        strip_obj[value].set_pixel(strip_state[value].offset + i * repeat_pix + 1, MyGlobal.color_anim_1)
        strip_obj[value].set_pixel(strip_state[value].offset + i * repeat_pix + 2, MyGlobal.color_anim_2)
        strip_obj[value].set_pixel(strip_state[value].offset + i * repeat_pix + 3, MyGlobal.color_anim_1)
    strip_obj[value].show()

def anim_update():
    for index, strip in enumerate(strip_state):
        if strip.get_anim():
            if strip.get_direction():
                strip_obj[index].rotate_left(1)
            else:
                strip_obj[index].rotate_right(1)
            strip_obj[index].show()

def anim_stop_all():
    for strip in strip_state:
        strip.set_anim(False)

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
    strip_obj[5].set_pixel_line(0, strip_obj[5].num_leds - 1, MyGlobal.color_anim_0)
    strip_obj[6].set_pixel_line(0, strip_obj[6].num_leds - 1, MyGlobal.color_def)
    strip_obj[7].set_pixel_line(0, strip_obj[7].num_leds - 1, MyGlobal.color_def)

    strip_obj[0].set_pixel(4, MyGlobal.color_anim_1)
    strip_obj[0].set_pixel(5, MyGlobal.color_anim_2)
    strip_obj[0].set_pixel(6, MyGlobal.color_anim_1)

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


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------
def main():
    
    print("WS2812 -> Setup")
    setup_ws2812()
        
    print("WS2812 -> Test 1")
    do_all_def()

    anim_startup(0)

    time.sleep(0.3)

    for i in range(0,50):
        anim_update()
        time.sleep(0.1)
  
    print("WS2812 -> End of Program !!!")

# End

#==============================================================================
#=== Start -> Main 
#==============================================================================

if __name__ == "__main__":
    main()

#==============================================================================
#=== End of Program
#==============================================================================
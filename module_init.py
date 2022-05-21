# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = False
    inc_serial          = False


class Global_WS2812:

    sel_pin_1           = 10
    sel_pin_2           = 11

    numpix_1            = 432   # Anzahl LEDs im 1. Stripe
    numpix_2            = 432   # Anzahl LEDs im 2. Stripe
    numpix_3            = 432   # Anzahl LEDs im 3. Stripe
    numpix_4            = 432   # Anzahl LEDs im 4. Stripe
    numpix_5            = 432   # Anzahl LEDs im 5. Stripe
    numpix_6            = 432   # Anzahl LEDs im 6. Stripe
    numpix_7            = 432   # Anzahl LEDs im 7. Stripe
    numpix_8            = 432    # Anzahl LEDs im 8. Stripe

    color_def           = (  0,  0, 10)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
    color_anim_0        = (  0, 10,  0)
    color_anim_1        = (  0, 50,  0)
    color_anim_2        = (  0,100,  0)
    color_blink_on      = (100,100,100)
    color_blink_off     = ( 50, 50, 50)

    color_s1_0          = ( 10,  0,  0)
    color_s2_0          = (  0, 10,  0)
    color_s3_0          = ( 30, 30, 30)
    color_s4_0          = ( 40, 40, 40)
    color_s5_0          = ( 50, 50, 50)
    color_s6_0          = ( 60, 60, 60)
    color_s7_0          = ( 70, 70, 70)
    color_s8_0          = ( 80, 80, 80)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz
    

#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

def main():

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.numpix_2)
    print(mg.seg_01_strip, mg.seg_01_start, mg.seg_01_count)
    print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Loader -> Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

# #############################################################################
# ### MyGlobal
# #############################################################################


class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = True
    inc_serial          = True


class Global_WS2812:

    numpix_1            = 80    # Anzahl LEDs im 1. Stripe
    numpix_2            = 80    # Anzahl LEDs im 2. Stripe
    numpix_3            = 80    # Anzahl LEDs im 3. Stripe
    numpix_4            = 80    # Anzahl LEDs im 4. Stripe
    numpix_5            = 80    # Anzahl LEDs im 5. Stripe
    numpix_6            = 80    # Anzahl LEDs im 6. Stripe
    numpix_7            = 80    # Anzahl LEDs im 5. Stripe



    color_def           = (  0,  0, 10)
    color_off           = (  0,  0,  0)
    color_on            = (100,100,100)
    color_dot           = ( 50, 50, 50)
    color_blink_on      = (100,100,100)
    color_blink_off     = ( 50, 50, 50)


class Global_Default:

    blink_freq          = 3.0           # Blink Frequenz
    

def main():

    print("Start Global Init")
    mg = Global_WS2812
    print(mg.numpix_1)
    print(mg.numpix_2)
    print(mg.seg_01_strip, mg.seg_01_start, mg.seg_01_count)
    print(mg.seg_02_strip, mg.seg_02_start, mg.seg_02_count)


#------------------------------------------------------------------------------
#--- Main
#------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

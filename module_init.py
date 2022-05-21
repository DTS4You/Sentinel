# #############################################################################
# ### MyGlobal
# #############################################################################

# Stripe 0 -> Sentinel 4
# Stripe 1 -> Sentinel 2
# Stripe 2 -> Sentinel 6
# Stripe 3 -> Sentinel 5 / 5B
# Stripe 4 -> Sentinel 3
# Stripe 5 -> Sentinel 1

class Global_Module:
    
    inc_ws2812          = True
    inc_decoder         = True
    inc_serial          = True


class Global_WS2812:

    sel_pin_1           = 10
    sel_pin_2           = 11

    numpix_1            = 444   # Anzahl LEDs im 1. Stripe Sentinel 4
    numpix_2            = 423   # Anzahl LEDs im 2. Stripe Sentinel 2
    numpix_3            = 423   # Anzahl LEDs im 3. Stripe Sentinel 6
    numpix_4            = 426   # Anzahl LEDs im 4. Stripe Sentinel 5 5B
    numpix_5            = 423   # Anzahl LEDs im 5. Stripe Sentinel 3
    numpix_6            = 423   # Anzahl LEDs im 6. Stripe Sentinel 1
    numpix_7            = 16    # Anzahl LEDs im 7. Stripe n.B.
    numpix_8            = 16    # Anzahl LEDs im 8. Stripe n.B.

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

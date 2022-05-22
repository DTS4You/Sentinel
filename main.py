######################################################
### Main-Program                                   ###
### Version: 1.00                                  ###
######################################################
from machine import Pin, Timer                              # RaspberryPi Pico2040 -> Hardware-Library
from module_init import Global_Module as MyModule
#import module_serial
import time

#            |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |
stripe_map = (  0 ,  5 ,  1 ,  4 ,  0 ,  3 ,  3 ,  2 )

def anim_func():
    MyWS2812.anim_update()

# ------------------------------------------------------------------------------
# --- Main Function                                                          ---
# ------------------------------------------------------------------------------
def main():

    print("=== Start Main ===")
    
    anim_couter = 0

    while MySerial.sercon_read_flag():      # Loop for Ever, execpt EOT

        anim_couter = anim_couter + 1       # Anim Tick

        if anim_couter > 20:                # Tick 10ms * Value
            anim_couter = 0
            anim_func()
        
        MySerial.sercon_read_line()
        if MySerial.get_ready_flag():       # Zeichenkette empfangen
            #print(MySerial.get_string())
            MyDecode.decode_input(str(MySerial.get_string()))
            #MyDecode.decode_printout()
            if MyDecode.get_valid_flag() == True:
                #print("Valid Command")
                if MyDecode.get_cmd_1() == "do":
                    #print("do")
                    if MyDecode.get_cmd_2() == "all":
                        #print("all")
                        if MyDecode.get_value_1() == 0:
                            #print("off")
                            MyWS2812.do_all_off()
                        if MyDecode.get_value_1() == 1:
                            #print("on")
                            MyWS2812.do_all_on()
                        if MyDecode.get_value_1() == 2:
                            #print("def")
                            MyWS2812.do_all_def()
                    if MyDecode.get_cmd_2() == "obj":
                        #print("do->obj")
                        #print(MyDecode.get_value_1())
                        if MyDecode.get_value_1() == 8:
                            #print("Demo-Mode")
                            MyWS2812.do_all_def()
                            MyWS2812.anim_startup(0)
                            MyWS2812.anim_startup(1)
                            MyWS2812.anim_startup(2)
                            MyWS2812.anim_startup(3)
                            MyWS2812.anim_startup(4)
                            MyWS2812.anim_startup(5)
                        else:
                            #print("Normal-Mode")
                            #print(stripe_map[MyDecode.get_value_1()])
                            MyWS2812.do_all_def()
                            #MyWS2812.anim_startup(MyDecode.get_value_1())               # ohne Mapping
                            MyWS2812.anim_startup(stripe_map[MyDecode.get_value_1()])  # mit Mapping
                        
        # Loop-Delay !!!
        time.sleep(0.01)        # 10ms


    print("=== End of Main ===")

# ==============================================================================
# ==============================================================================
    
# ###############################################################################
# ### Main                                                                    ###
# ###############################################################################


if __name__ == "__main__":

    if MyModule.inc_ws2812:
        #print("WS2812 -> Load-Module")
        import module_ws2812_v3 as MyWS2812         # Modul WS2812  -> WS2812-Ansteuerung
        #print("WS2812 -> Setup")
        MyWS2812.setup_ws2812()
        # Setup Default
        MyWS2812.do_all_def()

    if MyModule.inc_decoder:
        #print("Decode -> Load-Module")
        import module_decode as MyDecode
        #print("Decode -> Setup")
        MyDecode.decode_setup()
        ### Test ###
        #print("Decode -> Test")
        #MyDecode.decode_input("Test")

    if MyModule.inc_serial:
        #print("Serial-COM -> Load-Module")
        import module_serial as MySerial
        #print("Serial-Con -> Setup")
        MySerial.sercon_setup()
        ### Test ###
        #print("Serial-Con -> Test")
        #MySerial.sercon_write_out("Start Test")

    main()      # Start Main $$$

# Normal sollte das Programm hier nie ankommen !
print("___End of Programm___ !!!")

# ##############################################################################

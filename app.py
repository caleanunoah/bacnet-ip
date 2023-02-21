import BAC0
import json
import time
import BoC

# Define some constants
local_ipv4_addr = "192.168.1.73/24"               # local machine's wireless LAN ipv4 address
local_ethernet_ipv4_addr = "192.168.1.80/24"               # local machine's wireless LAN ipv4 address
BAC0_port = "47808"
yabe_room_sim_virtual_port = "52624"                     # YABE generates port for simulation (new # for new simulation)
yabe_301C_virtual_port = "47808"

# Create a BACnet connection to connect to the devices, use your local machine IP address and the subnet below and also specify the port number if needed
#bacnet = BAC0.lite(ip=local_ipv4_addr, port=BAC0_port)

data = {}

def main():
    # Reading 3 Objects from the Bacnet Simulator
    # Provided by YABE (Yet another BACnet sim)


    while True:
        #data = BoC.readPresentValueAnalogInput(bacnet, [0, 1, 2], local_ipv4_addr, yabe_room_sim_virtual_port)
        #data = BoC.readPresentValueAnalogValue(bacnet, [0, 1, 2, 3], local_ipv4_addr, yabe_room_sim_virtual_port)
        #data = BoC.readPresentValueBinaryInput(bacnet, [0, 1], local_ipv4_addr, yabe_room_sim_virtual_port)



        # Add captured into json file
        print(json.dumps(data, indent=2))
        time.sleep(5)


# RUN main
if __name__ == '__main__':
    #main()

    # Find 301-C on BACnet network. Close YABE to use this code
    bacnet = BAC0.lite(ip=local_ethernet_ipv4_addr, port=BAC0_port)
    bacnet.whois()
    print(bacnet.devices)
    myController = bacnet.devices[0]
    #print(myController[0]) # Device Name
    name = bacnet.read("192.168.1.254" + ":" + "47808" + " binaryInput " + "264" + " objectName")
    value = bacnet.read("192.168.1.254" + ":" + "47808" + " binaryInput " + "264" + " presentValue")
    print(str(name).strip() + ": " + str(value))





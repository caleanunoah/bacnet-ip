data = {}
import BAC0
import time

def readPresentValueAnalogInput(bacnet,
                    n,
                    local_ip_addr,
                    yabe_virtual_port):
    """
    @param bacnet: BACnet connection
    @param n: list of Object IDs to read from.
    @param local_ip_addr: # local machine's wireless LAN ipv4 address
    @param yabe_virtual_port: # YABE generates port for simulation (new # for new simulation)
    @return: data read from the Object ID list on the BACnet network
    """
    for x in n:
        # Initialize BACnet device ID's
        obj_id = str(x)

        # Connect to the BACnet simulator using the IP address and port number
        value = bacnet.read(local_ip_addr + ":" + yabe_virtual_port + " analogInput " + obj_id + " presentValue")
        value = str(value)
        data["Analog_input " + obj_id] = value

    return data


def readPresentValueAnalogValue(bacnet,
                    n,
                    local_ip_addr,
                    yabe_virtual_port):
    """
    @param bacnet: BACnet connection
    @param n: list of Object IDs to read from.
    @param local_ip_addr: # local machine's wireless LAN ipv4 address
    @param yabe_virtual_port: # YABE generates port for simulation (new # for new simulation)
    @return: data read from the Object ID list on the BACnet network
    """
    for x in n:
        # Initialize BACnet device ID's
        obj_id = str(x)

        # Connect to the BACnet simulator using the IP address and port number
        value = bacnet.read(local_ip_addr + ":" + yabe_virtual_port + " analogValue " + obj_id + " presentValue")
        value = str(value)
        data["Analog_value" + obj_id] = value

    return data

def readPresentValueBinaryInput(bacnet,
                    n,
                    local_ip_addr,
                    yabe_virtual_port):
    """
    @param bacnet: BACnet connection
    @param n: list of Object IDs to read from.
    @param local_ip_addr: # local machine's wireless LAN ipv4 address
    @param yabe_virtual_port: # YABE generates port for simulation (new # for new simulation)
    @return: Present value read from the device ID list on the BACnet network
    """
    for x in n:
        # Initialize BACnet device ID's
        obj_id = str(x)

        # Connect to the BACnet simulator using the IP address and port number
        value = bacnet.read(local_ip_addr + ":" + yabe_virtual_port + " binaryValue " + obj_id + " presentValue")
        value = str(value)
        data["Binary_input " + obj_id] = value

    return data


def readPresentValueBinaryInput(bacnet,
                    n,
                    local_ip_addr,
                    yabe_virtual_port):
    """
    @param bacnet: BACnet connection
    @param n: list of Object IDs to read from.
    @param local_ip_addr: # local machine's wireless LAN ipv4 address
    @param yabe_virtual_port: # YABE generates port for simulation (new # for new simulation)
    @return: data read from the device ID list on the BACnet network
    """
    for x in n:
        # Initialize BACnet device ID's
        obj_id = str(x)

        # Connect to the BACnet simulator using the IP address and port number
        value = bacnet.read(local_ip_addr + ":" + yabe_virtual_port + " binaryValue " + obj_id + " presentValue")
        value = str(value)
        data["Binary_input " + obj_id] = value

    return data

### Class definitions ###

class Site:
    '''
    Define a class for a Site
    '''
    def __init__(self, local_ipv4_addr, yabe_room_sim_virtual_port, floors=None):
        self.local_ipv4_addr = local_ipv4_addr
        self.yabe_room_sim_virtual_port = yabe_room_sim_virtual_port
        self.BAC0_port = "47808"

        self.floors = floors
        self.faultStatus = 0  # Boolean false
        self.data = {}

    def initializeBACnet(self):
        self.bacnet = BAC0.lite(ip=self.local_ipv4_addr, port=self.BAC0_port)

    def readPPM(self, n):
            """
            @param bacnet: BACnet connection
            @param n: list of Object IDs to read from.
            @param local_ip_addr: # local machine's wireless LAN ipv4 address
            @param yabe_virtual_port: # YABE generates port for simulation (new # for new simulation)
            @return: data read from the device ID list on the BACnet network
            """
            for x in n:
                # Initialize BACnet device ID's
                obj_id = str(x)

                # Connect to the BACnet simulator using the IP address and port number
                value = self.bacnet.read(self.local_ipv4_addr + ":" + self.yabe_room_sim_virtual_port + " analogInput " + obj_id + " presentValue")
                value = str(value)
                self.data["Analog_input " + obj_id] = value

            #return self.data

    def checkFaultStatus(self):
        if self.faultStatus == 0:
            return "No Fault"
        if self.faultStatus == 1:
            return "Yes Fault"

class Floor:
    def __init__(self, floors):
        self.floors = floors

    def printAllRooms(self):
        for floor in self.floors:
            for room in self.floors.rooms:
                print(room)


if __name__ == "__main__":
    print("Testing started...")
    time.sleep(1)

    site = Site(local_ipv4_addr="192.168.0.54/24", yabe_room_sim_virtual_port="58879")
    site.initializeBACnet()

    floors = {1: {100: ["VFD100"], 101: ["VFD101"], 102: ["VFD102"]},
              2: {202: ["VFD202"], 203: ["VFD203"], 205: ["VFD205"]},
              3: {311: ["VFD311"]}
              }

    site.readPPM([0, 1, 2])
    print(site.data)
    time.sleep(1)








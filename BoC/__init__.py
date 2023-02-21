data = {}

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
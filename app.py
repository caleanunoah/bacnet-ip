import BAC0
import json
import time
import BoC
import mysql.connector
from mysql.connector import errorcode

# Define some constants
local_ipv4_addr = "192.168.1.73/24"                      # local machine's wireless LAN ipv4 address
honeywell_301C_ipv4_addr = "192.168.1.254"                      # local machine's wireless LAN ipv4 address
local_ethernet_ipv4_addr = "192.168.1.80/24"             # local machine's wireless LAN ipv4 address
yabe_room_sim_virtual_port = "57217"                     # YABE generates port for simulation (new # for new simulation)
BAC0_port = "47808"
OBJ_ID_PPM = "513"

# Create a BACnet connection to connect to the devices, use your local machine IP address and the subnet below and also specify the port number if needed
#bacnet = BAC0.lite(ip=local_ipv4_addr, port=BAC0_port)

data = {}

def main():
    # Find 301-C on BACnet network
    bacnet = BAC0.lite(ip=local_ethernet_ipv4_addr, port=BAC0_port)
    bacnet.whois()
    print(bacnet.devices)
    myController = bacnet.devices[0]
    # print(myController[0]) # Device Name

    while True:
        # Now read 301C Objects over BACnet connection
        # You can use YABE to find value for "honeywell_301C_ipv4_addr"
        # Port: Default BACnet port (47808)
        # Object type: defined by BAC0 source code
        # ID: found using YABE
        #

        #               [IP Addr. of Phys. Device]    [Port]    [Object type]  [Object. ID]  [Prop. Name]
        # name = bacnet.read("192.168.1.254" + ":" + "47808" + " binaryInput " + "264" + " objectName")                     # 301C Relay#1
        # value = bacnet.read("192.168.1.254" + ":" + "47808" + " binaryInput " + "264" + " presentValue")                  # 301C Relay#1
        name = bacnet.read(honeywell_301C_ipv4_addr + ":" + BAC0_port + " analogInput " + OBJ_ID_PPM + " objectName")       # Get PPM
        value = bacnet.read(honeywell_301C_ipv4_addr + ":" + BAC0_port + " analogInput " + OBJ_ID_PPM + " presentValue")    # Get PPM

        # Format and output the current value of PPM
        #print(str(name).strip() + ": " + str(value) + " PPM")
        print(str(value) + " PPM")
        time.sleep(3)


    ## -------- MySQL Setup -------- ##
    ##  TODO: REPLACE WITH A GOOGLE CLOUD INSTANCE
    '''
        try:
        cnx = mysql.connector.connect(user="root",
                                      password="Operator123!@#",
                                      host='127.0.0.1',
                                      database="Operator_sites",
                                      use_pure=False)

        cursor = cnx.cursor()

        query = ("SELECT * FROM site ")

        cursor.execute(query)
        row_data = []
        for row in cursor:
            row_data.append(row)
            #print(json.dumps(row, indent=2))
        print(row_data)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("ERROR: User or Password is incorrect")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("ERROR: Database does not exist")
        else:
            print("ERROR: " + err)
    else:
        cursor.close()
        cnx.close()
    '''


    ## -------- BACnet Setup -------- ##
    ##  This portion of the script will initialize BACnet connection and read object data ##
    '''
    site = BoC.Site(local_ipv4_addr=local_ipv4_addr, yabe_room_sim_virtual_port=yabe_room_sim_virtual_port)
    site.initializeBACnet()

    objectIDs = [0, 1, 2]
    site.readPPM(objectIDs)
    # Add captured into json file
    print(json.dumps(site.data, indent=2))
    '''


    ## -------- WebServer Setup -------- ##
    ## TODO SETUP CLOUD BASED WEBSERVER????
    '''
    app = flask.Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    app.run()
    '''


# RUN main
if __name__ == '__main__':
    main()










#include <iostream>
#include <ads.h>

int main() {
    // Initialize ADS
    ADS_Init();

    // Create a connection to the PLC
    ADS_CONNECTION connection;
    ADS_Connect(&connection, "192.168.0.1.1.1", 851);

    // Send three different messages
    ADS_Write(&connection, ADSIGRP_DEVICE, ADSTYPE_STRING, 100, "Message 1", 11);
    ADS_Write(&connection, ADSIGRP_DEVICE, ADSTYPE_INT, 200, 42, 4);
    ADS_Write(&connection, ADSIGRP_DEVICE, ADSTYPE_BOOL, 300, true, 1);

    // Listen for a specific message
    ADS_READ read_req;
    read_req.port = ADSIGRP_DEVICE;
    read_req.indexGroup = 400;
    read_req.indexOffset = 0;
    read_req.bytelength = 4;

    while (true) {
        ADS_Read(&connection, &read_req);
        int received_value = *(int*)read_req.buffer;

        if (received_value == 123) {
            std::cout << "Received expected message!" << std::endl;
            break;
        }
    }

    // Close the connection and deinitialize ADS
    ADS_Disconnect(&connection);
    ADS_Terminate();

    return 0;
}
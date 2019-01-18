from threading import Thread
from client_system import ClientServer
from queue import Queue
import logging

logging.basicConfig(filename='app.log', filemode='w', format='[%(asctime)s] [%(process)d] [%(levelname)s] - %(message)s')

gmsec_received = Queue()
gmsec_out = Queue()
http_received = Queue()
http_out = Queue()
client_server_in = Queue()
client_server_out = Queue() # may not be used

client_server_port = 20001
max_device_count = 10

http_server_port = 8080
client_handler = object()

def __init__ ():
    logging.info("starting HoloLens companion server core system.")
    start_client_server()

    return


def start_client_server():
    #try:
    logging.info("Starting client server on port: " + str(client_server_port))
    logging.info("Client server max device connections: " + str(max_device_count))
    client_handler = ClientServer(client_server_port, "localhost", max_device_count, client_server_in, client_server_out)
    #except:
    #    logging.error("Could not start the client server due to unknown error.")

def stop_client_server(self):
    try:
        logging.info("Stopping client server on port: " + str(client_server_port))
        # do something to stop the client server on the port
    except:
        logging.error("Could not stop the client server due to an unknown error.")

if __name__ == "__main__":
    __init__()
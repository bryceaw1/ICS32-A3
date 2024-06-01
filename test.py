import ds_client
import ds_protocol



def start():
    ds_client.send("168.235.86.101", 3021, 'BOBBY', '1234', 'TEST MESSAGE KUMBAYA')

if __name__ == '__main__':
    start()
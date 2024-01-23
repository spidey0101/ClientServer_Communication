# Socket Communication Project README

## Overview

This project demonstrates a simple client-server communication using Python's socket module. The communication involves sending messages from a client to a server, and the server responding to each message.

## Files

### Server Code (server.py):

- Creates a server socket.
- Binds the socket to a specific host and port.
- Listens for incoming connections.
- Accepts connections and receives messages from clients.

#### Usage:

```bash
python server.py
```

### Client Code (client.py):

- Creates a client socket.
- Connects to the server using the server's host and port.
- Sends messages to the server.
- Receives and displays responses from the server.

#### Usage:

```bash
python client.py
```

### Host Retrieval (host.py):

- Contains a function to retrieve the host dynamically.
- Used to avoid hardcoding the host address in the client code.

## Instructions

1. **Run the Server:**
   - Execute `python server.py` in the terminal.
   - The server will start listening for incoming connections.

2. **Update the Server Address (Optional):**
   - If the server is running on a different machine, update the `host` variable in `client.py` with the server's IP address.

3. **Run the Client:**
   - Execute `python client.py` in a separate terminal.
   - The client will connect to the server.

4. **Sending Messages:**
   - In the client terminal, input messages and press Enter.
   - Observe the server terminal for received messages.

5. **Checking Status:**
   - To check the status of the communication, review the print statements in both the server and client terminals.

## Notes

- The client and server can run on the same machine or different machines based on the host configuration.
- Always update the `host` variable in the client code if the server is running on a different machine.


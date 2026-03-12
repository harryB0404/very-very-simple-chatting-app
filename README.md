# Simple Chatting App

A basic real-time client-server chat application built with Python sockets.

## Description
This project demonstrates core networking concepts through a simple chat system.  
One user runs the **server**, and another user (or the same computer) runs the **client** to send and receive messages in real time.

It was created as a learning project to practice socket programming, threading, and basic client-server communication.

## Features
- Real-time messaging between client and server
- Threaded message receiving (no blocking)
- Type `endchat` to end the conversation from either side
- Server automatically logs all messages to `log.txt`
- Simple command-line interface with input validation

## Requirements
- Python 3.x
- Both client and server must be on the same local network
- No external libraries needed (only built-in `socket`, `threading`, `time`, `sys`)

## How to Run

### Step 1: Run the Server
1. Open `server.py`
2. Run it:
   ```bash
   python server.py

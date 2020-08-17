"""
purpose: To learn about network and web programming in python.This tutorial
is from david beazley book. Chapter 11.

Topic: creating TCP server using only builtin socket library

date: 2020/July/24th
author:Bhoj bahadur karki
Motivation: To be able to build my own server.
Quote: Those who believe can, will do it.

This program is a simple version of a server (like SimpleHTTPServer or other server e.g. php apache server)

"""


from socket import socket, AF_INET, SOCK_STREAM


def echo_handler(address, client_sock):
    print("[x] got connected from... {} ".format(address))
    while True:
        msg = client_sock.recv(8192)
        if not msg:
            break
        client_sock.sendall(msg)
    client_sock.close()


def echo_server(adddress, backlog=5):
    sock = socket(AF_INET,SOCK_STREAM)
    sock.bind(adddress)
    sock.listen(backlog)
    while True:
        client_sock , client_addr= sock.accept()
        echo_handler(client_addr,client_sock)


if __name__=="__main__":
    echo_server(('',20000))






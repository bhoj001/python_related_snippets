"""
purpose: To learn about network and web programming in python.This tutorial
is from david beazley book. Chapter 11.

Topic: creating TCP server using socketserver libaray.

date: 2020/July/24th
author:Bhoj bahadur karki
Motivation: To be able to build my own server.
Quote: Those who believe can, will do it.

"""

from socketserver import BaseRequestHandler, TCPServer


class EchoHandler(BaseRequestHandler):
    def handle(self):
        print("Got connection from ",self.client_address)
        while True:
            msg = self.request.recv(8192)
            if not msg:
                break
            self.request.send(msg)


if __name__=="__main__":
    serv = TCPServer(('',20000),EchoHandler)
    serv.serve_forever()





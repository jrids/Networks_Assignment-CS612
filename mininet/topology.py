#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel
from mininet.node import OVSController
from mininet.cli import CLI
import time

def mininett():

  topo = Topo()

  s1 = topo.addSwitch('s1')

 
  h1 = topo.addHost ('h1', ip='10.0.0.1')
  h2 = topo.addHost ('h2', ip='10.0.0.2')
  h3 = topo.addHost ('h3', ip='10.0.0.3')
  h4 = topo.addHost ('h4', ip='10.0.0.4')
  h5 = topo.addHost ('h5', ip='10.0.0.5')
  h6 = topo.addHost ('h6', ip='10.0.0.6')
 

  topo.addLink(s1, h1)
  topo.addLink(s1, h2)
  topo.addLink(s1, h3)
  topo.addLink(s1, h4)
  topo.addLink(s1, h5)
  topo.addLink(s1, h6)


  net = Mininet(topo=topo, controller=OVSController,cleanup = True)
 

  net.start()
  net.pingAll()
  
  h1 = net.get('h1')
  h2 = net.get('h2')
  h3 = net.get('h3')
  h4 = net.get('h4')
  h5 = net.get('h5')
  h6 = net.get('h6')
  

  h1.cmdPrint('sudo python3 my_serverFork.py &')
  time.sleep(10)
  h2.cmdPrint('sudo python3 my_client.py ')
  h3.cmdPrint('sudo python3 my_client.py ')
  h4.cmdPrint('sudo python3 my_client.py ')
  h5.cmdPrint('sudo python3 my_client.py ')
  h6.cmdPrint('sudo python3 my_client.py ')
  
  CLI(net)
  net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    mininett()
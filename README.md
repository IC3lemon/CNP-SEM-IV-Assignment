# CNP-SEM-IV-Assignment

### `Files to submit`
- the pkt file
- writeup
- the typed report

# `Writeup`

## Network topology :
![image](https://github.com/user-attachments/assets/885c0b1f-ecd0-4bb5-9efb-e39caa572538)

## Router configs : 
### `Router 1`
```
Router>enable
Router#config t
Router(config)#interface FastEthernet4/0
Router(config-if)#ip address 192.168.1.1 255.255.255.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface FastEthernet5/0
Router(config-if)#ip address 155.169.1.1 255.255.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial2/0
Router(config-if)#ip address 10.0.0.3 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial3/0
Router(config-if)#ip address 20.0.0.2 255.0.0.0
Router(config-if)#clock rate 64000
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#exit
Router#copy running-config startup-config
```
## `Router 2`
```
Router>enable
Router#config t
Router(config)#interface FastEthernet0/0
Router(config-if)#ip address 111.169.1.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial2/0
Router(config-if)#clock rate 64000
Router(config-if)#ip address 10.0.0.2 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial3/0
Router(config-if)#ip address 30.0.0.3 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#exit
Router#copy running-config startup-config
```
## `Router 3`
```
Router>enable
Router#config t
Router(config)#interface FastEthernet4/0
Router(config-if)#ip address 122.163.1.1 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial2/0
Router(config-if)#clock rate 64000
Router(config-if)#ip address 30.0.0.2 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#interface Serial3/0
Router(config-if)#ip address 20.0.0.3 255.0.0.0
Router(config-if)#no shutdown
Router(config-if)#exit
Router(config)#exit
Router#copy running-config startup-config
```

## Implementing RIP and setting up NTP server:
### `Router 1` 
```
Router>enable
Router#config t
Router(config)#router rip
Router(config-router)#network 192.168.1.0
Router(config-router)#network 155.169.0.0
Router(config-router)#network 10.0.0.0
Router(config-router)#network 20.0.0.0
Router(config-router)#network 111.0.0.0
Router(config-router)#network 122.0.0.0
Router(config-router)#network 30.0.0.0
Router(config-router)#exit
Router(config)#ntp server 111.169.1.3
Router(config)#exit
Router#copy running-config startup-config
Router#show clock
16:36:58.288 UTC Mon Mar 10 2025
```
### `Router 2` 
```
Router>enable
Router#config t
Router(config)#router rip
Router(config-router)#network 192.168.1.0
Router(config-router)#network 155.169.0.0
Router(config-router)#network 10.0.0.0
Router(config-router)#network 20.0.0.0
Router(config-router)#network 111.0.0.0
Router(config-router)#network 122.0.0.0
Router(config-router)#network 30.0.0.0
Router(config-router)#exit
Router(config)#ntp server 111.169.1.3
Router(config)#exit
Router#copy running-config startup-config
Router#show clock
16:36:58.288 UTC Mon Mar 10 2025
```
### `Router 3`
```
Router>enable
Router#config t
Router(config)#router rip
Router(config-router)#network 192.168.1.0
Router(config-router)#network 155.169.0.0
Router(config-router)#network 10.0.0.0
Router(config-router)#network 20.0.0.0
Router(config-router)#network 111.0.0.0
Router(config-router)#network 122.0.0.0
Router(config-router)#network 30.0.0.0
Router(config-router)#exit
Router(config)#ntp server 111.169.1.3
Router(config)#exit
Router#copy running-config startup-config
Router#show clock
16:37:23.704 UTC Mon Mar 10 2025
```

Verifying RIP for each router. Performed via `show ip protocols`
### `Router 1` :
```
Router#show ip protocols
Routing Protocol is "rip"
Sending updates every 30 seconds, next due in 14 seconds
Invalid after 180 seconds, hold down 180, flushed after 240
Outgoing update filter list for all interfaces is not set
Incoming update filter list for all interfaces is not set
Redistributing: rip
Default version control: send version 1, receive any version
  Interface             Send  Recv  Triggered RIP  Key-chain
  FastEthernet4/0       12 1
  FastEthernet5/0       12 1
  Serial2/0             12 1
  Serial3/0             12 1
Automatic network summarization is in effect
Maximum path: 4
Routing for Networks:
	10.0.0.0
	20.0.0.0
	30.0.0.0
	111.0.0.0
	122.0.0.0
	155.169.0.0
	192.168.1.0
Passive Interface(s):
Routing Information Sources:
	Gateway         Distance      Last Update
	20.0.0.3             120      00:00:04
	10.0.0.2             120      00:00:03
Distance: (default is 120)
Router#
```
### `Router 2` :
```
Router#show ip protocols
Routing Protocol is "rip"
Sending updates every 30 seconds, next due in 14 seconds
Invalid after 180 seconds, hold down 180, flushed after 240
Outgoing update filter list for all interfaces is not set
Incoming update filter list for all interfaces is not set
Redistributing: rip
Default version control: send version 1, receive any version
  Interface             Send  Recv  Triggered RIP  Key-chain
  Serial2/0             12 1
  Serial3/0             12 1
  FastEthernet0/0       12 1
Automatic network summarization is in effect
Maximum path: 4
Routing for Networks:
	10.0.0.0
	20.0.0.0
	30.0.0.0
	111.0.0.0
	122.0.0.0
	155.169.0.0
	192.168.1.0
Passive Interface(s):
Routing Information Sources:
	Gateway         Distance      Last Update
	10.0.0.3             120      00:00:22
	30.0.0.2             120      00:00:12
Distance: (default is 120)
```

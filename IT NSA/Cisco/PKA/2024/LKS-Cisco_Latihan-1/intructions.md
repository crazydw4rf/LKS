# Packet tracer activity instructions

## Daftar Materi
- Routing RIP
- DHCP Server
- DNS Server
- Web Server
- VLAN trunking

## Pengalamatan
| Perangkat|Interface|IP|
|--|--|--|
|Router 1|FastEthernet1/0.10|172.12.1.1/24|
||FastEthernet1/0.20|172.12.2.1/24|
||FastEthernet0/0|182.10.1.1/29|
||Serial2/0|10.10.10.1/30|
|Router 2|Serial2/0|10.10.10.2/30|
||FastEthernet0/0|182.11.1.1/29|
|Web Server|FastEthernet0|182.10.1.6/29|
|DNS Server|FastEthernet0|182.11.1.6/29|
|Semua PC Client|FastEthernet0|DHCP|

## DHCP Server
|Perangkat|Nama Pool|Default Router|
|--|--|--|
|Router 1|POOL_VLAN_10|172.12.1.1/24|
||POOL_VLAN_20|172.12.2.1/24|

Untuk IP DNS Server pada DHCP sesuaikan dengan IP DNS Server yang ada.
Exclude/Kecualikan IP pada DHCP dengan setiap IP yang di set pada VLAN

## DNS Server
|Nama Domain|IP|
|--|--|
|lkslab-1.com|182.10.1.6|

## Web Server
Edit file `index.html` dengan text berikut:
```
Hello World
```
## VLAN
|Nama VLAN|IP|
|--|--|
|VLAN10|172.12.1.1/24|
|VLAN20|172.12.2.1/24|

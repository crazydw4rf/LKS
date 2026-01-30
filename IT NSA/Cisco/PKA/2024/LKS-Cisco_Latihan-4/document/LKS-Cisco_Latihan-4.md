# LKS-Cisco_Latihan-4

## Daftar Materi

- Routing (OSPF,Static)
- VLAN
- DHCP Server
- VTP
- Access Point (Wireless)
- VLAN Virtual Interface
- Port Security
- Access List
- Dynamic NAT
- Server Services (HTTP,DNS)

## Pengalamatan

Atur alamat IP pada semua perangkat dan sesuaikan IP DNS pada semua perangkat PC dan Server dengan alamat IP DNS Server.
Untuk virtual interface pada router `Router Sekolah` yaitu FastEthernet8/0.1 dan FastEthernet8/0.2 konfigurasi `encapsulation dot1q` nya terlebih dahulu untuk menentukan VLAN pada interface tersebut.
|Perangkat|Interface|Alamat IP|
|-|-|-|
|Router Server 1|GigabitEthernet1/0|172.13.56.10/30|
||GigabitEthernet2/0|172.13.56.6/30|
||FastEthernet8/0|112.23.1.35/28|
|Router Server 2|GigabitEthernet0/0|112.23.1.2/28|
||GigabitEthernet1/0|172.13.56.9/30|
||FastEthernet8/0|112.23.1.20/28|
|Router ISP|GigabitEthernet0/0|[[GW_ISP]]/17|
||GigabitEthernet1/0|172.13.56.1/30|
||GigabitEthernet2/0|172.13.56.5/30|
||GigabitEthernet3/0|8.8.8.1/28|
|Router Sekolah|GigabitEthernet1/0|[[IP_RANDOM_ISP_PUBLIC_1]]/17|
||GigabitEthernet0/0|132.100.100.13/30|
||FastEthernet8/0.1|[[GW_VLAN_PCGURU]]/26|
||FastEthernet8/0.2|[[GW_VLAN_WIFI_SEKOLAH]]/23|
|MLS1|GigabitEthernet0/1|132.100.100.14/30|
||VLAN 101|[[GW_VLAN_LAB_COMP_1]]/25|
||VLAN 102|[[GW_VLAN_LAB_COMP_2]]/25|
|Web Server 1|FastEthernet0|112.23.1.40/28|
|Web Server 2|FastEthernet0|112.23.1.30/28|
|DNS|FastEthernet0|8.8.8.8/28|
|Semua PC dan Laptop Client|FastEthernet0/Wireless|DHCP|

## Routing

### Router Sekolah

Lakukan routing static untuk menjangkau network VLAN `LAB_COMP_1` dan `LAB_COMP_2` juga lakukan routing static `default route` untuk menjangkau semua network yang ada pada `Router ISP`.

### MLS1

Konfigurasi routing static `default route` untuk menjangkau semua network yang ada pada router `Router Sekolah`.

### Semua Router Server dan Router ISP

Konfigurasi semua `Router Server` dan `Router ISP` dengan routing OSPF dan daftarkan semua network yang ada pada setiap interface pada router, gunakan process id `1` untuk semua konfigurasi OSPF pada router.

## DHCP

Buat DHCP server pada beberapa perangkat berikut dan sesuaikan `default-router` dengan gateway di setiap VLAN dan `dns-server` dengan alamat IP perangkat server DNS.
|Perangkat|Nama Pool|Network|Excluded IP|
|-|-|-|-|
|MLS1|[[POOL_NAME_LAB1]]|172.32.1.0/25|[[GW_VLAN_LAB_COMP_1]]|
||[[POOL_NAME_LAB2]]|172.32.1.128/25|[[GW_VLAN_LAB_COMP_2]]|
|Router Sekolah|[[POOL_NAME_WIFI]]|43.120.64.0/23|[[GW_VLAN_WIFI_SEKOLAH]]|
||[[POOL_NAME_PCGURU]]|192.168.1.0/26|[[GW_VLAN_PCGURU]]|

## VLAN

Untuk semua switch dan MLS atur mode port sesuai dengan perangkat yang tersambung pada port interface tersebut juga atur access VLAN pada setiap interface dengan VLAN yang sudah dikonfigurasikan pada switch.
|Perangkat|Nomor VLAN|Nama VLAN|Interface|
|-|-|-|-|
|MLS1|101|LAB_COMP_1|vlan 101|
||102|LAB_COMP_2|vlan 102|
|Router Sekolah|103|PC_GURU|FastEthernet8/0.1|
||104|WIFI_SEKOLAH|FastEthernet8/0.2|

## VTP

Atur VTP pada perangkat MLS dan Switch dengan ketentuan berikut. Gunakan `[[VTP_DOMAIN]]` sebagai domain VTP dan `[[VTP_PASSWORD]]` sebagai password.
|Perangkat|VTP Mode|
|-|-|
|MLS1|server|
|SW1|client|
|SW2|client|

## Port Security

Konfigurasi Port Security pada setiap perangkat switch yang tersambung pada client. Untuk perangkat switch `SW1` konfigurasikan Port Security hanya untuk jaringan VLAN `PC_GURU`. Berikut ketentuan konfigurasinya.
|Perangkat|Mode|Violation|
|-|-|-|
|SW1|static|protect|
|SW2|sticky|restrict|
|SW3|sticky|restrict|

## Access List

Konfigurasi ACL pada perangkat router `Router Sekolah` dan MLS `MLS1` dengan ketentuan berikut.

### Router Sekolah

- Extended `ACL_BLOCK_WEB`: Network VLAN WIFI_SEKOLAH tidak dapat mengakses layanan `HTTP` pada `Web Server 2`
- Standard `1`: Access list yang akan digunakan pada konfigurasi NAT untuk mengizinkan network-network pada jaringan lokal atau private untuk menggunakan NAT.
- Standard `2`: Network VLAN LAB_COMP_1, LAB_COMP_2 dan WIFI_SEKOLAH tidak dapat mengakses network VLAN `PC_GURU`

### MLS1

- Extended `ACL_BLOCK_WEB`: Network VLAN LAB_COMP_1 tidak dapat mengakses layanan `HTTP` pada `Web Server 1`

## Dynamic NAT

Konfigurasi Dynamic NAT pada perangkat router `Router Sekolah` dengan menggunakan Dynamic NAT Overload dan gunakan access list `1` sebagai access list pada NAT juga atur mode NAT `inside` atau `outside` di setiap interface pada router.

## Access Point

Konfigurasi perangkat `AP1` dengan ketentuan berikut.
|Connection Type|SSID|Passphrase|Frequency|
|-|-|-|-|
|Wireless AP|WIFI SEKOLAH|wifi12345|2.4 Ghz|

## DNS

Pada perangkat server `DNS` tambahkan record sesuai ketentuan berikut.
|Domain Name|Alamat IP|
|-|-|
|`web1.lkslab.com`|112.23.1.40|
|`web2.lkslab.com`|112.23.1.30|

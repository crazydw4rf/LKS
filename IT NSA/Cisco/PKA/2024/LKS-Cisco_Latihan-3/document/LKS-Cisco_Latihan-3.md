# LKS-Cisco_Latihan-3

## Daftar Materi
-	Port Security
-	Firewall
-	NAT
- Static Routing

## Pengalamatan
Atur alamat IP pada semua perangkat dan sesuaikan IP DNS pada semua perangkat PC dan Server dengan alamat IP DNS Server.
|Perangkat|Interface|Alamat IP|
|-|-|-|
|RTR1|GigabitEthernet6/0|137.12.1.2/26|
||FastEthernet1/0|192.43.1.1/25|
||FastEthernet0/0|192.43.1.129/25|
|RTR2|GigabitEthernet6/0|137.12.1.1/26|
||FastEthernet0/0|172.10.1.1/26|
|Web Server|FastEthernet0|172.10.1.2/26|
|DNS|FastEthernet0|172.10.1.3/26|
|PC0|FastEthernet0|192.43.1.2/25|
|PC1|FastEthernet0|192.43.1.3/25|
|PC2|FastEthernet0|192.43.1.130/25|
|PC3|FastEthernet0|192.43.1.131/25|

## NAT
Pada perangkat `RTR1` buat access list standard untuk mengijinkan network-network yang ada pada private network agar dapat melewati router `RTR1` kemudian konfigurasi NAT pada perangkat `RTR1` dengan dynamic NAT agar perangkat dari private network dapat berkomunikasi dengan public network. Atur mode NAT `inside` atau `outside` di setiap interface pada router `RTR1`.
|Nama Pool|Nomor ACL|Rentang IP|
|-|-|-|
|POOL_NAT_1|1|137.12.1.2 -- 137.12.1.10|

## Routing
Lakukan routing pada perangkat `RTR1` agar network private dapat menjangkau network public dengan `static default route`.

## Port Security
Konfigurasi port security pada perangkat `SW1` dan `SW2` dengan ketentuan berikut.
|Perangkat|Mode|Violation|
|-|-|-|
|SW1|sticky|restrict|
|SW2|static|protect|

## Firewall
Konfigurasi Firewall sesuai dengan ketentuan berikut.
- Pada `PC3` konfigurasi firewall agar `PC0` tidak dapat ping ke `PC3`.
- Pada `PC0` konfigurasi firewall agar `PC0` tidak dapat mengakses layanan `Web Server`.

## DNS
Pada perangkat server `DNS` buat record sesuai ketentuan berikut.
|Domain|Alamat IP|
|-|-|
|`local.lab.net`|172.10.1.2|

# LKS-Cisco_Latihan-2

## Notes
Konfigurasikan semua perangkat jaringan dengan ketentuan yang ada pada instruksi di bawah ini.
Untuk nama hostname dapat disesuaikan sesuai dengan yang tertera di display name pada topologi.

Router `RTR1`,`RTR2`,`RTR3` dan `RTR4` hanya dapat di konfigurasi melalui port console dari terminal pada Laptop `Remote Console` .


## Daftar materi
- Routing OSPF, RIP
- Routing Redistribution
- MLS (SVI)
- VLAN
- DHCP
- Access List
- Access Point (Wireless)

## Pengalamatan
|Perangkat|Port Interface|Alamat IP|
|--|--|--|
|RTR1|GigabitEthernet0/0|20.20.20.2/30|
||GigabitEthernet0/1|10.10.10.1/30|
||GigabitEthernet0/2|30.30.30.1/30|
||GigabitEthernet0/0/0|192.11.1.1/28|
|RTR2|GigabitEthernet0/0|10.10.10.2/30|
||GigabitEthernet0/1|40.40.40.2/30|
||GigabitEthernet0/2|60.60.60.2/30|
||GigabitEthernet0/0/0|192.22.1.1/28|
|RTR3|GigabitEthernet0/0|20.20.20.1/30|
||GigabitEthernet0/1|50.50.50.1/30|
||GigabitEthernet0/2|40.40.40.1/30|
|RTR4|GigabitEthernet0/0|50.50.50.2/30|	
||GigabitEthernet1/0|60.60.60.1/30|
||GigabitEthernet2/0|30.30.30.2/30|
||GigabitEthernet3/0|172.43.1.21/30|
|MLS1|GigabitEthernet0/1|172.43.1.22/30|
||VLAN GURU|167.23.1.1/26|
||VLAN SISWA|167.23.2.1/26|
|Web Server|FastEthernet0|192.11.1.14/28|
|DNS Server|FastEthernet0|192.22.1.14/28|
|Semua PC dan Laptop Client||DHCP|

## VLAN
Konfigurasi semua VLAN pada perangkat MLS dan semua switch yang ada juga atur mode port dan akses VLAN yang dibutuhkan pada setiap port switch. Sesuaikan juga akses VLAN untuk semua client sesuai block warna pada topologi.
|Nomor VLAN|Nama VLAN|
|--|--|
|100|GURU|
|110|SISWA|

## DHCP
Buat DHCP Server pada `MLS1` untuk network VLAN `GURU` dan VLAN `SISWA`.
|Nama Pool|Network|Default Router|Excluded IP|
|--|--|--|--|
|[[DHCP_POOL_NAME_VLAN_GURU]]|[[IP_NETW_VLAN_GURU]]/26|[[IP_GW_VLAN_GURU]]|[[IP_POOL_VLAN_GURU_EXCL]]
|[[DHCP_POOL_NAME_VLAN_SISWA]]|[[IP_NETW_VLAN_SISWA]]/26|[[IP_GW_VLAN_SISWA]]|[[IP_POOL_VLAN_SISWA_EXCL]]

## Routing
Lakukan routing pada semua router dengan  OSPF. Untuk router `RTR4` dilakukan routing dengan dua jenis routing OSPF dan RIP dimana port interface yang mengarah ke perangkat jaringan client atau perangkat `MLS1` menggunakan routing RIP.
|Jenis Routing|Process ID|Version|
|--|--|--|
|OSPF|100|--|
|RIP|--|2|

## Routing Redistribution
Pada router `RTR4` akan dilakukan *routing redistribution* antara routing OSPF dan RIP.

## Access Point
Pada perangkat `AP1` lakukan konfigurasi sesuai dengan ketentuan berikut.
|SSID|Password|
|--|--|
|[[AP1_SSID]]|[[AP1_PASS]]|

## Access List
Pada router `RTR4` lakukan konfigurasi *Access list* dengan memblokir koneksi permintaan pada layanan tertentu dari sumber host IP atau network sesuai ketentuan berikut.
|Host/Network sumber|Jenis layanan|Host/Network tujuan|Nama/Nomor ACL|
|--|--|--|--|
|[[IP_NETW_VLAN_SISWA]]/26|HTTP|[[IP_DEV_WEBSERVER]]|block_web|

## MLS
Buat VLAN Virtual interface sesuai tabel pengalamatan pada interface VLAN dan atur port interface yang menuju router `RTR4` dari port switch menjadi port router agar bisa diberi alamat IP dan dilakukan routing. Perangkat `MLS1` juga akan digunakan sebagai DHCP server untuk memberikan alamat IP secara otomatis kepada client.

## DNS
Tambahkan Record A pada DNS Server sesuai ketentuan berikut.
|Nama Domain|Alamat IP|
|--|--|
|[[NS1_RECORD_1]]|[[IP_DEV_WEBSERVER]]|


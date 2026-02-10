# LKS Cisco PKA Latihan 2

- IP Address & Subnetting
- Inter-VLAN Routing & Interface
- DHCP
- VLAN
- NAT (Source NAT)
- Routing (static, eigrp)
- Server

## Catatan

Gunakan perangkat `Laptop0` dan `Laptop1` untuk konfigurasi perangkat jaringan
lainnya dengan menggunakan `console`.
Gunakan `lkslab2026` sebagai password untuk mengakses privileged exec mode pada
setiap perangkat jaringan.

## Konfigurasi Dasar

### Hostname

|Perangkat|Hostname|
|-|-|
|Router Edge 1|EDGE1|
|Router ISP|ISP|

## Pengalamatan

Semua perangkat PCx klien memakai IP dari DHCP server.
Pada perangkat `Router Edge 1` terdapat 2 VLAN yaitu VLAN 10 dan VLAN 20,
atur dot1q subinterface pada interface `GigabitEthernet1/0/0` sesuai tabel
berikut.

|Perangkat|Interface|IP address|
|-|-|-|
|Router Edge 1|GigabitEthernet1/1/0|[\[EDGE_PUBLIC_OUT\]]/17|
|-|GigabitEthernet1/0/0.10|10.7.1.1/24|
|-|GigabitEthernet1/0/0.20|10.8.1.1/24|
|Router ISP|GigabitEthernet0/2/0|[\[ISP_GATEWAY\]]/17|
|-|GigabitEthernet0/3/0|172.10.1.1/30|
|-|GigabitEthernet0/1/0|172.11.1.1/30|
|Router 1|GigabitEthernet0/2/0|172.10.1.2/30|
|-|GigabitEthernet0/3/0|172.12.1.1/30|
|-|GigabitEthernet1/1/0|211.13.1.1/24|
|Router 2|GigabitEthernet0/2/0|172.11.1.2/30|
|-|GigabitEthernet0/3/0|172.12.1.2/30|
|-|GigabitEthernet1/1/0|211.14.1.1/24|
|DNS|FastEthernet0|211.14.1.100/24|
|Web Server|FastEthernet0|211.13.1.100/24|

## DHCP Server

Atur DHCP server pada perangkat `Router Edge 1` sesuai tabel berikut.

|Pool Name|Default Router|DNS Server|Excluded Address|
|-|-|-|-|
|VLAN10|10.7.1.1|211.14.1.100|10.7.1.2 - 10.7.1.99|
|VLAN20|10.8.1.1|211.14.1.100|10.8.1.2 - 10.8.1.99|

Atur juga network dan netmask pada masing-masing pool DHCP.

## VLAN

Pada Perangkat `Switch Sekolah` atur VLAN sesuai tabel berikut.

|VLAN ID|Nama VLAN|Interface|
|-|-|-|
|10|SISWA|Gig0/1,Gig1/1|
|20|GURU|Gig2/1,Gig3/1|

## NAT

Pada perangkat `Router Edge 1` atur NAT dengan Source NAT pada interface
`GigabitEthernet1/1/0` dan access list standar dengan nomor `1` dan beri
aturan permit/izinkan semua jaringan lokal.

## Routing

Atur default static routing pada perangkat `Router Edge 1` dengan IP next hop
yaitu IP pada interface router `Router ISP`.
Atur Routing dengan menggunakan routing EIGRP pada perangkat `Router ISP`,
`Router 1` dan `Router 2` dan daftarkan semua network yang tersedia pada setiap
interface. Gunakan ASN `1` untuk konfigurasi semua routing EIGRP pada semua
router pada sisi ISP.

## Services

Pada perangkat `Web Server` aktifkan layanan http dan buat file `index.html`
dengan isi teks berikut.

```plain
LKS LAB 2026
```

Pada perangkat `DNS` aktifkan layanan DNS dan tambahkan record baru sesuai
tabel berikut.

|Record Type|Name|IP Address|
|-|-|-|
|A|lkslab26.com|211.13.1.100|

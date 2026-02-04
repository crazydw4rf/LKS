# LKS Cisco PKA Latihan 1

- IP Addressing dan Subnetting
- Banner MOTD
- SSH/Telnet Remote Access
- Console Access
- Web Server

## Catatan

Untuk memicu `Connectivity Test` bisa tekan tombol `Check Results`
agar tes konektivitas antar perangkat dapat berjalan dan mendapatkan poin sesuai
tes yang berhasil.

Gunakan kabel-kabel pada `Cable Pegboard` untuk keperluan membuat koneksi antar
perangkat yang diperlukan.

Gunakan kabel console dan perangkat `Laptop0` untuk
mengakses konsol pada perangkat `Router Pusat`.

## Tujuan

Semua perangkat pada _network_ dan _routing table_ yang sesuai
dapat saling berkomunikasi dan terhubung serta layanan-layanan dari
_server_ dapat diakses oleh perangkat klien dengan baik.

## Pengalamatan

Atur alamat IP pada semua perangkat.

|Perangkat|Interface|Alamat IP|
|-|-|-|
|Router Pusat|Gig0/0/0|10.8.0.1/24|
|-|Gig0/0/1|10.7.0.1/24|
|Web Server|FastEthernet0|10.7.0.2/24|
|PC0|FastEthernet0|10.8.0.2/24|

## Konfigurasi Dasar

Beri secret untuk _privileged exec mode_ pada perangkat
`Router Pusat` yaitu "lkslab2026".

### Identitas Perangkat

|Perangkat|Hostname|Domain Name|
|-|-|-|
|Router Pusat|R1|lkslab.com|

### Daftar Pengguna

Tambahkan pengguna untuk mengakses perangkat melalui SSH/Telnet pada router
`Router Pusat`.

|Username|Password|Level|
|-|-|-|
|admin|admin123|15|
|dika|dika123|15|

### Banner

Tambahkan MOTD atau banner login pada perangkat `Router Pusat`.

|MOTD|Login|
|-|-|
|LKS LAB 2026|Hi admin|

Aktifkan juga motd banner pada setiap jenis koneksi yaitu
`console 0` dan `vty 0 4`.

### Privilege Level

Beri privilege level pada perangkat `Router Pusat` untuk setiap jenis koneksi
yaitu 15.

## Web Server

Aktifkan layanan HTTP pada perangkat server `Web Server` dan
buat _file_ baru dengan nama `index.html` dan isi dengan teks berikut.

```plain
LKS LAB 2026
```

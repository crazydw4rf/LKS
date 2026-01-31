# LKS Cisco PKA 1

## Daftar Materi

- IP Addressing dan Subnetting
- Web Server

## Tujuan

Semua perangkat pada _network_ dan _routing table_ yang sesuai
dapat saling berkomunikasi dan terhubung serta layanan-layanan dari
_server_ dapat diakses oleh perangkat klien dengan baik.

## Pengalamatan

Atur alamat IP pada semua perangkat.

|Perangkat|Interface|Alamat IP|
|-|-|-|
|Router Pusat 1|Ethernet0/0|192.168.18.1/24|
|-|Ethernet1/0|10.8.0.130/25|
|Web Server|FastEthernet0|10.8.0.140/25|
|PC LAB 1|FastEthernet0|192.168.18.10/24|
|PC GURU 1|FastEthernet0|192.168.18.20/24|

## Web Server

Aktifkan layanan HTTP pada perangkat server `Web Server` dan
buat _file_ baru dengan nama `index.html` dan isi dengan teks berikut.

```plain
LKS 2026
```

## Pengujian

Lakukan tes konektivitas antar perangkat yang berbeda segmen jaringan nya
dan juga uji layanan web pada `PC GURU 1` dengan mengakses _Web Browser_
pada menu Desktop dan masukan alamat IP dari `Web Server`.

## Catatan

Untuk memicu `Connectivity Test` bisa tekan tombol `Check Results`
agar tes konektivitas antar perangkat dapat berjalan dan mendapatkan poin sesuai
tes yang berhasil.

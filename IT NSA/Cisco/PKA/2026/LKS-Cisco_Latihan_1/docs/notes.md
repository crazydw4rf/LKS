# Catatan

Catatan tentang proses belajar konfigurasi perangkat jaringan cisco.

## Cisco CLI Authentication Types

Pada perangkat jaringan Cisco, terdapat dua jenis autentikasi utama yang digunakan
untuk mengamankan akses ke Command Line Interface (CLI), yaitu "enable secret"
dan "password". Keduanya berfungsi untuk melindungi akses ke perangkat, namun
memiliki perbedaan dalam hal keamanan dan penggunaan.

- Privilige mode => password yang dibutuhkan ketika akan berganti mode akses CLI
dari user ke priviliged mode.
- Console access (console 0) => password yang dibutuhkan ketika mengakses CLI dengan
menggunakan kabel console lewat perangkat lain seperti laptop atau computer.
- Remote access (ssh, telnet, vty 0 4) => password yang dibutuhkan ketika
mengakses CLI lewat jaringan dengan protokol seperti ssh atau telnet.

Ada pula `exec level` atau batasan tingkat izin perintah yang boleh dijalankan pada
saat masuk dengan password tertentu yang sebelumnya sudah diberi exec level.
exec level terdiri dari rentang angka yaitu 1 sampai 15 yang mengindikasikan
tingkat exec level yang diberikan oleh pengguna. level 0, 1 dan 15 adalah level
default yang sudah terdefinisi pada perangkat, yaitu:

- 0: Hak akses paling rendah, hanya bisa perintah dasar (disable, help, exit).
- 1: Mode User EXEC (Router>), bisa perintah monitoring dasar (misal: show version).
- 15: Hak akses tertinggi, mode Privileged EXEC (Router#), bisa ubah konfigurasi
perangkat.

dan level 2 sampai 14 adalah level yang bisa di kustomisasi perintah apa saja
yang boleh dijalankan pada level tersebut. Contoh perintah:

```lua
! secara default bila tidak diberi exec level maka akan menggunakan level 15
Router(config)# enable secret password123
! bila ingin secara eksplisit memberikan exec level 5 pada password
Router(config)# enable secret level 5 password123
!
! untuk menampilkan exec level pada saat ini setelah memasuki global
! configuration mode
Router(config)# do show privilige
! atau setelah memasuki privileged exec mode
Router# show privilige
```

## All about Message banner and MOTD

Ada dua jenis pesan banner yaitu `motd` dan `login` banner.
Banner motd akan selalu tampil ketika mengakses CLI, sedangkan banner login
akan tampil ketika mengakses CLI lewat remote (ssh, telnet) atau console.
Khusus untuk banner login, hanya akan tampil bila sudah diaktifkan pada
line vty atau conosole. Contoh perintah:

```lua
! banner motd. Karakter '#' disini digunakan untuk pembatas awal dan
! pembatas akhir atau bisa disebut dengan delimiter kalimat atau kata
! untuk pesan banner. Delimiter dapat menggunakan karakter atau simbol
! apapun, asalkan sama pada awal dan akhir pesan banner.
Router(config)# banner motd #
Selamat datang di Router Pusat 1
#
! banner login. Untuk mengaktifkan banner login pada line vty atau console,
! harus masuk mode line terlebih dahulu.
Router(config)# banner login $
LKS LAB 2026
$
! kemudian aktifkan pada salah satu line, misal pada line vty 0 4
Router(config)# line vty 0 4
Router(config-line)# motd-banner


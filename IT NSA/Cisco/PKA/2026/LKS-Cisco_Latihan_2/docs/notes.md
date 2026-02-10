# Notes

## How to NAT

NAT atau Network Address Translation adalah teknik pada jaringan yang digunakan
untuk memetakan beberapa alamat IP internal atau private ke satu atau beberapa
alamat IP publik dengan tujuan agar perangkat pada jaringan internal dapat
mengakses internet atau jaringan yang yang lebih luas dengan tetap
menyembunyikan alamat IP internal.

Pada sistem perangkat jaringan cisco, NAT dibagi lagi menjadi 3 yaitu
static, dynamic dan PAT(Port Address Translation).

## How to config

### Static NAT

```lua
! ip nat inside source static <alamat ip internal> <ip publik>
ip nat inside source static 10.8.0.2 201.13.0.120
```

perintah tersebut dimaksukan untuk memetakan alamat IP internal yaitu
`10.8.0.2` untuk memakai alamat IP publik `201.13.0.120` untuk berkomunikasi
ke jaringan publik atau internet.

### Dynamic NAT

```lua
! membuat access list untuk jaringan internal yang akan mengakses jaringan publik
! access-list 1 permit <network IP> <wilcard netmask>
access-list 1 permit 10.8.0.0 0.0.0.255

! membuat NAT pool untuk ranga atau jangkauan IP publik yang akan dipakai
ip nat pool NAMA_POOL 201.10.50.32 201.10.60.1 netmask 255.255.128.0
ip nat inside source list 1 pool NAMA_POOL

```

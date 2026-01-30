# Catatan

## Langkah-langkah untuk membuat self-signed certificate

### Membuat Root CA

```bash
openssl req -x509 -sha256 -days 365 -nodes -newkey rsa:2048 -subj \
"/CN=LKS LAB/C=ID/L=Jawa Tengah/O=Otong Inc./OU=Any" -keyout RootCAKey_LKS-LAB.key -out RootCA_LKS-LAB.crt
```

Perintah diatas akan menghasilkan dua file yaitu root certificate `RootCA_LKS-LAB.crt`
dan private key `RootCAKey_LKS-LAB.key`.

### Membuat private key dan certificate request

Langkah selanjutnya adalah membuat private key dan certificate request.

```bash
openssl genrsa -out server.key 2048
```

Perintah diatas akan menghasilkan file server.key, file ini akan digunakan untuk membuat certificate request.

```bash
openssl req -new -key server.key -out server.csr
```

Ketika menjalankan perintah diatas perintah tersebut akan meminta untuk memasukan nilai-nilai berupa
subjek atau data yang dibutuhkan untuk membuat certificate request.

```txt
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:ID
State or Province Name (full name) [Some-State]:Jawa Tengah
Locality Name (eg, city) []:Cilacap
Organization Name (eg, company) [Internet Widgits Pty Ltd]:Star Dust
Organizational Unit Name (eg, section) []:Blue Sky
Common Name (e.g. server FQDN or YOUR name) []:*.lkslab-1.com
Email Address []:

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```

Untuk alamat email, password dan nama company atau perusahaan dapat dikosongkan.
Setelah menjalankan perintah untuk membuat certificate request yang menghasilkan file `server.csr`, file ini
akan digunakan untuk membuat certificate yang akan digunakan pada web server.

### Membuat certificate untuk web server

Langkah selanjutnya adalah membuat certificate untuk digunakan pada web.

```bash
openssl x509 -req -in server.csr -CA ./RootCA_LKS-LAB.crt -CAkey ./RootCAKey_LKS-LAB.key \
-CAcreateserial -out server.crt -days 365 -sha256 \
-extfile <(printf "subjectAltName=DNS:lkslab-1.com,DNS:*.lkslab-1.com")
```

Perintah diatas akan menghasilkan file server.crt yang akan digunakan untuk konfigurasi pada web server
agar dapat menggunakan koneksi atau protokol https yang membuat koneksi antara klien dengan server ter-enkripsi
atau aman.

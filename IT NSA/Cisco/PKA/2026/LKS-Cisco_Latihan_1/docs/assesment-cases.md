# Assesment Cases

Kasus dan penyelesaian yang harus dikerjakan pada packet tracer activity.

## Latihan 1

- [ ] set privileged mode secret or password
- [ ] setup ssh and telnet (IP address,hostname,domain name)
- [ ] add user and password for remote access auth
- [ ] add banner motd and login

### Devices

- Server: 1
- Router: 1
- Laptop: 1
- PC Computer: 1

### Assesment Points

- Privileged mode secret: lkslab2026
- SSH and telnet
  - IP addresses
    - R1 gi0/0/0: 10.8.0.1/24
    - R1 gi0/0/1: 10.7.0.1/24
    - Server FastEthernet0: 10.7.0.2/24
    - PC FastEthernet0: 10.8.0.2/24
  - hostname: R1
  - domain name: lkslab.com
- User
  - SSH
    - name: admin
    - level: 15
    - password: admin123
  - Telnet
    - name: dika
    - level: 15
    - password: dika123
- Banner
  - MOTD: "LKS LAB 2026"
  - Login: "Hi admin"
- Services
  - Web
    - filename: index.html
    - content: "LKS LAB 2026"

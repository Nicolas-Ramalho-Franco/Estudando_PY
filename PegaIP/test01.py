import socket

# Obtém o nome da máquina e resolve para o IP local
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f"Seu IP local é: {ip}")

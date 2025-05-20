import subprocess

# Leer número actual
try:
    with open("commit_version.txt", "r") as f:
        version = float(f.read().strip())
except FileNotFoundError:
    version = 0.0  # Si no existe el archivo, empezás desde 0

# Sumar 0.01
version += 0.01
version = round(version, 2)  # Redondear a dos decimales

# Guardar nueva versión en el archivo
with open("commit_version.txt", "w") as f:
    f.write(str(version))

# Hacer git add y commit con el mensaje
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", str(version)])

print(f"Se hizo commit con el mensaje: {version}")

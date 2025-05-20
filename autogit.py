import subprocess

# Leer número actual desde archivo o empezar en 0.25
try:
    with open("commit_version.txt", "r") as f:
        version = float(f.read().strip())
except FileNotFoundError:
    version = 0.25  # Primer valor si no existe el archivo

# Sumar 0.01
version += 0.01
version = round(version, 2)  # Redondear a 2 decimales

# Guardar nueva versión en el archivo
with open("commit_version.txt", "w") as f:
    f.write(str(version))

# Hacer git add y commit con el mensaje de versión
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", str(version)])

print(f"✅ Commit realizado con mensaje: {version}")

import subprocess

# Leer número actual desde archivo o empezar en 0.25
try:
    with open("commit_version.txt", "r") as f:
        version = float(f.read().strip())
except FileNotFoundError:
    version = 0.25

# Sumar 0.01 y redondear
version += 0.01
version = round(version, 2)

# Guardar nueva versión en archivo
with open("commit_version.txt", "w") as f:
    f.write(str(version))

# Ejecutar git add, commit y push
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", str(version)])
subprocess.run(["git", "push"])

print(f"✅ Commit y push realizados con mensaje: {version}")

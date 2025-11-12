import subprocess

def test_connectivity():
    print("🔹 Simulando teste de conectividade entre dois nós...")

    result = subprocess.run(["ping", "-c", "2", "127.0.0.1"], capture_output=True, text=True)
    #result = subprocess.run(["ping", "-c", "2", "10.0.0.2"], capture_output=True, text=True)


    if result.returncode == 0:
        print("✅ Conectividade verificada com sucesso!")
    else:
        print("❌ Falha no teste de rede!")
        print(result.stderr)
        exit(1)

if __name__ == "__main__":
    test_connectivity()

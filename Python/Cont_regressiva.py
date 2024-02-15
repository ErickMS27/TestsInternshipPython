import time

def time_countdown(time_sec):
    for i in range(time_sec, 0, -1):
        print(f"Contagem regressiva: {i} segundos")
        time.sleep(1)

    print("\nFELIZ ANO NOVO!")

time_count = 10

time_countdown(time_count)
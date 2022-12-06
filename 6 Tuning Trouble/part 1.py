with open("signal.txt", "r") as file:
    signal = file.read().strip()
    i = 0
    buffer = []
    while i < len(signal) and len(buffer) < 4:
        if signal[i] not in buffer:
            buffer.append(signal[i])
            i += 1
        else:
            i-= (len(buffer) - 1)
            buffer = []

    print(i)
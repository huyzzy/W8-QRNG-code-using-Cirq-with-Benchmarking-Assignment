import time

try:
    import cirq
except ImportError:
    print("Installing cirq...")
    !pip install --quiet cirq
    import cirq
    print("Installed cirq.")

# Pick a qubit
qubit = cirq.GridQubit(0, 0)

circuit = cirq.Circuit(
    cirq.X(qubit) ** 0.5,
    cirq.measure(qubit, key='m')
)
print("Circuit:")
print(circuit)

# Simulate and measure elapsed time
simulator = cirq.Simulator()
start_time = time.time()
result = simulator.run(circuit, repetitions=20)
end_time = time.time()

# Convert to binary string and decimal
bitstring = ''.join(str(bit) for bit in result.measurements['m'][:, 0])
decimal_result = int(bitstring, 2)

# Display results
print("Results:")
print(f"m={bitstring}")
print(f"Decimal result: {decimal_result}")
print(f"Elapsed time: {end_time - start_time:.4f} seconds")

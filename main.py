from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
from qiskit_braket_provider import AWSBraketProvider

provider = AWSBraketProvider()
circuit = QuantumCircuit(3, 3)

# Apply H-gate to the first qubit:
circuit.h(0)


# Apply a CNOT to each qubit:
for qubit in range(1, 3):
    circuit.cx(0, qubit)

circuit.measure([0,1,2], [0,1,2])

rigetti_device = provider.get_backend("SV1")
rigetti_task = rigetti_device.run(circuit, shots=10)
rigetti_arn = rigetti_task.job_id()

plot_histogram(rigetti_task.result().get_counts())

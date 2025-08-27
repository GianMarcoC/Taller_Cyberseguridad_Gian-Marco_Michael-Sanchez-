import hashlib
import time

# Clase que representa un bloque de la cadena
class Block:
    def __init__(self, index, data, previous_hash):
        # Índice para identificar la posición del bloque en la cadena
        self.index = index
        # Marca de tiempo de creación del bloque
        self.timestamp = time.time()
        # Información ficticia o transacciones que contiene el bloque
        self.data = data
        # Hash del bloque anterior, para mantener la cadena unida
        self.previous_hash = previous_hash
        # Hash propio del bloque, calculado al crearlo
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Se combinan los campos importantes y se aplica SHA-256
        block_string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        return hashlib.sha256(block_string.encode()).hexdigest()


# Clase que representa toda la blockchain
class Blockchain:
    def __init__(self):
        # La cadena inicia con un bloque génesis
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Primer bloque de la cadena, creado manualmente
        return Block(0, "Bloque Génesis", "0")

    def get_latest_block(self):
        # Retorna el último bloque agregado
        return self.chain[-1]

    def add_block(self, new_data):
        # Crea un nuevo bloque usando el hash del último bloque
        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), new_data, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Revisa la integridad de la cadena
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Verifica que el hash actual no haya cambiado
            if current_block.hash != current_block.calculate_hash():
                return False

            # Verifica que el bloque anterior esté bien enlazado
            if current_block.previous_hash != previous_block.hash:
                return False

        return True


# --- Simulación práctica ---

# Se crea la cadena de bloques
my_chain = Blockchain()

# Se añaden algunos bloques con datos ficticios
my_chain.add_block("Transacción 1: Alice paga 10 a Bob")
my_chain.add_block("Transacción 2: Bob paga 5 a Carlos")
my_chain.add_block("Transacción 3: Carlos paga 2 a Diana")

# Se muestra la cadena completa
print("Cadena inicial:")
for block in my_chain.chain:
    print(f"Índice: {block.index}, Datos: {block.data}, Hash: {block.hash}")

# Validación inicial
print("\n¿La cadena es válida?", my_chain.is_chain_valid())

# Se altera el contenido de un bloque para simular un ataque
my_chain.chain[1].data = "Transacción 1: Alice paga 1000 a Bob"
my_chain.chain[1].hash = my_chain.chain[1].calculate_hash()

# La cadena ahora debería ser inválida
print("\nDespués de modificar un bloque:")
for block in my_chain.chain:
    print(f"Índice: {block.index}, Datos: {block.data}, Hash: {block.hash}")

print("\n¿La cadena es válida?", my_chain.is_chain_valid())

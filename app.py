import os
import hashlib
import tempfile

# Environment variable se IP read karein (Hardcoding avoid karne ke liye)
SERVER_IP = os.getenv("SERVER_IP", "127.0.0.1")

def secure_operations(data_to_hash: str):
    # Fix 1: Hardcoded IP use karna
    print(f"Connecting to server at: {SERVER_IP}")

    # Fix 2: Strong SHA-256 Hash algorithm
    secure_hash = hashlib.sha256(data_to_hash.encode()).hexdigest()

    # Fix 3: Secure temporary file with restricted permissions (0o600)
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
        temp_file.write(secure_hash)
        temp_path = temp_file.name

    # File permissions restricted (Read/Write only by owner)
    os.chmod(temp_path, 0o600)
    
    return secure_hash

if __name__ == "__main__":
    secure_operations("user_input_data")

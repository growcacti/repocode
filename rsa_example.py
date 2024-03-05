from Crypto.PublicKey import RSA


def generate_rsa_keys(bits=2048):
    # Generate a fresh key
    key = RSA.generate(bits)

    # Export private and public keys
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    return private_key, public_key


private_key, public_key = generate_rsa_keys()
print("Private Key:", private_key.decode())
print("\nPublic Key:", public_key.decode())

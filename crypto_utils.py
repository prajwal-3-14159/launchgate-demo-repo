"""Encrypts trip notes at rest with AES-256-GCM."""
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def encrypt_note(key: bytes, plaintext: bytes) -> bytes:
    nonce = os.urandom(12)
    return nonce + AESGCM(key).encrypt(nonce, plaintext, None)


def decrypt_note(key: bytes, blob: bytes) -> bytes:
    return AESGCM(key).decrypt(blob[:12], blob[12:], None)

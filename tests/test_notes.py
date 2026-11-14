import os

from crypto_utils import decrypt_note, encrypt_note


def test_note_round_trip():
    key = os.urandom(32)
    assert decrypt_note(key, encrypt_note(key, b"Kyoto, day 2")) == b"Kyoto, day 2"

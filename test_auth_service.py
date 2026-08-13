import os

os.environ.setdefault(
    "JWT_SECRET", "test-secret-with-at-least-thirty-two-characters"
)

from auth.service import hash_password, verify_password


def test_legacy_password_is_accepted_for_progressive_migration():
    assert verify_password("legacy-password", "legacy-password")
    assert not verify_password("wrong-password", "legacy-password")


def test_new_password_hash_uses_current_cost_and_verifies():
    password_hash = hash_password("a-strong-test-password")
    assert password_hash.startswith("pbkdf2_sha256$600000$")
    assert verify_password("a-strong-test-password", password_hash)
    assert not verify_password("wrong-password", password_hash)

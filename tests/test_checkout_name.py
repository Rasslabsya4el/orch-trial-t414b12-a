from pathlib import Path

from orch_it.checkout_name import folder_is_repo_name

ROOT = Path(__file__).resolve().parent.parent


def test_the_checkout_folder_carries_the_repo_name():
    assert folder_is_repo_name(ROOT)

"""Specify fixtures and constants used during pytest tests."""

# Tell pytest where fixtures are located
# There should be single entry for each fixture (python) file in tests/fixtures
pytest_plugins = [
    "fixtures.general_fixtures",
]

import pytest

# Aquí configuras --headed (headless=False) y --slowmo (en ms)
@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False, 
        "slow_mo": 3000      
    }

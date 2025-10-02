import os
import sys


import sys
import subprocess
import importlib.util

def pip_install(*packages):
    """Install packages into the current Python environment."""
    subprocess.run([sys.executable, "-m", "pip", "install", *packages], check=True)

def ensure_installed(package_spec, import_name=None):
    """
    Install the given package_spec (e.g. 'cpz-ai==1.2.3') if it's not already installed.
    If import_name is different from the PyPI name, pass it explicitly.
    """
    name = import_name or package_spec.split("==")[0].split(">=")[0].split("~=")[0]
    if importlib.util.find_spec(name) is None:
        print(f"📦 Installing {package_spec} ...")
        pip_install(package_spec)
    else:
        print(f"✅ {name} already installed.")

if __name__ == "__main__":
    ensure_installed("cpz-ai")  # Pin version if needed: cpz-ai==x.y.z
    import cpz  # Use the actual import name
    print(f"cpz-ai version: {getattr(cpz, '__version__', 'unknown')}")


import cpz
from cpz.execution.models import OrderSubmitRequest
from cpz.execution.enums import OrderSide, OrderType, TimeInForce

CPZ_AI_API_KEY= "cpz_key_d3f35dd8e76742a0aeef19f9"
CPZ_AI_API_SECRET= "cpz_secret_n435540581rz6z2u6m3l28624u585w4512z22295q62qx554"


# Only CPZ AI credentials needed
client = cpz.clients.sync.CPZClient()

# Single account setup
client.execution.use_broker("alpaca", environment="paper")

# Multi-account setup (if you have multiple accounts with same broker/environment)
# client.execution.use_broker("alpaca", environment="paper", account_id="your-account-id")

order = client.execution.submit_order(OrderSubmitRequest(
    symbol="AAPL",
    side=OrderSide.BUY,
    qty=10,
    type=OrderType.MARKET,
    time_in_force=TimeInForce.DAY,
    strategy_id="4db15ae8-8a31-400e-ab33-f3643e248338",  # REQUIRED
))
print(order.id, order.status)
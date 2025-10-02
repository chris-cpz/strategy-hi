import os
import sys

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
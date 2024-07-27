
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import LimitOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
api_key = "PKK2RJBV3AN4KONDJSAU"
secret_key = "OW19XLSUcjjBnyIVjFuz7TOEd4UvYVoQov23fjYb"

trading_client = TradingClient(api_key, secret_key, paper=True)

limit_order_data = LimitOrderRequest(
    symbol="SPY",
    limit_price=540,
    qty=100,
    side=OrderSide.BUY,
    time_in_force=TimeInForce.DAY
)
limit_order = trading_client.submit_order(order_data = limit_order_data)
call_order_data = LimitOrderRequest(
    symbol="SPY240801C00540000conda update -n base -c defaults conda -y",
    limit_price=4.11,
    qty=1,
    side=OrderSide.SELL,
    time_in_force=TimeInForce.DAY
)
call_order = trading_client.submit_order(order_data = call_order_data)
trading_client.get_all_positions()
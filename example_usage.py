"""
example_usage.py -- Demonstrates ShippingCalculatorClient
"""
from client import ShippingCalculatorClient

def main():
    client = ShippingCalculatorClient()
    result = client.calculate(
        destination_zip="90210",
        weight_lbs=8.5,
        dimensions={"length": 12, "width": 10, "height": 8},
        service_level="expedited"
    )
    print("[Shipping Calculator Result]")
    print(f"Carrier: {result['carrier']}")
    print(f"Cost: ${result['shipping_cost']}")
    print(f"Timeline: {result['estimated_days']} business days")

if __name__ == "__main__":
    main()

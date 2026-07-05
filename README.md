# simple-shipping-calculator-skill

> **GenPark AI Agent Skill** -- Shipping rates and delivery estimator.

## Quick Start

```python
from client import ShippingCalculatorClient
client = ShippingCalculatorClient()
result = client.calculate(destination_zip="90210", weight_lbs=5)
print(result["shipping_cost"])
```

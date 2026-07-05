"""
simple-shipping-calculator-skill: Client SDK
Calculates shipping rates and delivery timelines based on destination, weight and size.
"""
from __future__ import annotations
from typing import Optional

CARRIER_SERVICES = {
    "standard": {"base": 5.99, "per_lb": 0.85, "days": 5, "carrier": "FedEx Ground"},
    "expedited": {"base": 12.50, "per_lb": 1.50, "days": 2, "carrier": "UPS Blue"},
    "overnight": {"base": 24.99, "per_lb": 3.00, "days": 1, "carrier": "DHL Express"},
}


class ShippingCalculatorClient:
    """
    SDK for calculating shipping costs and carrier assignments.
    """

    def calculate(
        self,
        destination_zip: str,
        weight_lbs: float,
        dimensions: Optional[dict] = None,
        service_level: str = "standard",
    ) -> dict:
        """
        Calculate shipping cost and timeline.
        """
        service = service_level.lower()
        if service not in CARRIER_SERVICES:
            service = "standard"

        config = CARRIER_SERVICES[service]
        base_cost = config["base"]
        weight_cost = weight_lbs * config["per_lb"]

        # Dimensional weight adjustment if dimensions are provided
        dim_cost = 0.0
        if dimensions:
            l = float(dimensions.get("length", 0))
            w = float(dimensions.get("width", 0))
            h = float(dimensions.get("height", 0))
            volume = l * w * h
            if volume > 1728:  # Larger than 1 cubic foot
                dim_cost = (volume / 166) * 0.5  # Standard dim divisor fee

        total_cost = round(base_cost + weight_cost + dim_cost, 2)

        return {
            "shipping_cost": total_cost,
            "estimated_days": config["days"],
            "carrier": config["carrier"],
            "destination_zip": destination_zip,
            "service_level": service,
        }

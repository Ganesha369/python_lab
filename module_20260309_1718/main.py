```python
"""
Logistics & Supply Chain Module: Inventory Intelligence (InvIntel)
Focus: Automated Replenishment Logic and Demand Forecasting using Exponential Smoothing.
Author: Senior Python Developer
"""

import math
import logging
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import List, Optional, Dict, Protocol
from pydantic import BaseModel, Field, validator

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("InvIntel")

# --- Models ---

class Product(BaseModel):
    sku: str
    name: str
    lead_time_days: int = Field(gt=0, description="Days from order to delivery")
    unit_cost: float = Field(gt=0)
    holding_cost_annual_pct: float = 0.20
    service_level_z_score: float = 1.645  # Default 95% service level

class InventoryState(BaseModel):
    sku: str
    on_hand: int
    on_order: int
    historic_demand: List[int] = Field(default_factory=list)

# --- Forecasting Logic ---

class DemandForecaster:
    """Provides demand prediction using Simple Exponential Smoothing (SES)."""
    
    @staticmethod
    def calculate_ses(history: List[int], alpha: float = 0.3) -> float:
        """
        Calculates the forecast for the next period.
        Formula: F_{t+1} = alpha * Y_t + (1 - alpha) * F_t
        """
        if not history:
            return 0.0
        
        forecast = history[0]
        for actual in history[1:]:
            forecast = (alpha * actual) + (1 - alpha) * forecast
        return forecast

    @staticmethod
    def calculate_std_dev(history: List[int]) -> float:
        if len(history) < 2:
            return 0.0
        mean = sum(history) / len(history)
        variance = sum((x - mean) ** 2 for x in history) / len(history)
        return math.sqrt(variance)

# --- Replenishment Engine ---

class ReplenishmentEngine:
    """Core logic for calculating Reorder Points (ROP) and Order Quantities."""

    def __init__(self, product: Product, state: InventoryState):
        self.product = product
        self.state = state
        self.forecaster = DemandForecaster()

    def calculate_reorder_point(self) -> int:
        """
        ROP = (Avg Daily Demand * Lead Time) + Safety Stock
        Safety Stock = Z * StdDev * sqrt(Lead Time)
        """
        if not self.state.historic_demand:
            return 0

        avg_daily_demand = self.forecaster.calculate_ses(self.state.historic_demand)
        std_dev = self.forecaster.calculate_std_dev(self.state.historic_demand)
        
        safety_stock = (
            self.product.service_level_z_score * 
            std_dev * 
            math.sqrt(self.product.lead_time_days)
        )
        
        rop = (avg_daily_demand * self.product.lead_time_days) + safety_stock
        return math.ceil(rop)

    def calculate_economic_order_quantity(self, annual_demand: int) -> int:
        """
        EOQ = sqrt((2 * Demand * Setup Cost) / Holding Cost)
        Simplified for this module assuming fixed setup cost per order.
        """
        setup_cost = 50.0  # Fixed administrative cost per order
        holding_cost_per_unit = self.product.unit_cost * self.product.holding_cost_annual_pct
        
        if holding_cost_per_unit == 0:
            return 0
            
        eoq = math.sqrt((2 * annual_demand * setup_cost) / holding_cost_per_unit)
        return math.ceil(eoq)

    def get_replenishment_decision(self) -> Dict:
        """Determines if an order needs to be placed and how much."""
        rop = self.calculate_reorder_point()
        current_effective_inventory = self.state.on_hand + self.state.on_order
        
        needs_replenishment = current_effective_inventory <= rop
        recommended_qty = 0
        
        if needs_replenishment:
            # Estimate annual demand based on last 30 days if available
            period_demand = sum(self.state.historic_demand[-30:])
            annual_est = (period_demand / max(len(self.state.historic_demand[-30:]), 1)) * 365
            recommended_qty = self.calculate_economic_order_quantity(int(annual_est))

        return {
            "sku": self.product.sku,
            "reorder_point": rop,
            "current_effective_inv": current_effective_inventory,
            "action_required": needs_replenishment,
            "recommended_order_qty": recommended_qty,
            "timestamp": datetime.now().isoformat()
        }

# --- Example Usage ---

if __name__ == "__main__":
    # 1. Define Product Meta
    widget_a = Product(
        sku="WDG-100-BLU",
        name="Blue Industrial Widget",
        lead_time_days=5,
        unit_cost=25.50
    )

    # 2. Define Current State (Low Stock Scenario)
    current_state = InventoryState(
        sku="WDG-100-BLU",
        on_hand=12,
        on_order=0,
        historic_demand=[10, 12, 15, 8, 14, 11, 13] # Last 7 days
    )

    # 3. Run Engine
    engine = ReplenishmentEngine(widget_a, current_state)
    decision = engine.get_replenishment_decision()

    print(f"--- Replenishment Report for {widget_a.sku} ---")
    for key, value in decision.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
```
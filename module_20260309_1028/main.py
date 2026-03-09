```python
"""
LogiFlow: Inventory Optimization Module
Version: 1.0.0
Author: Senior Python Developer
Description: A specialized engine for calculating Economic Order Quantity (EOQ), 
Safety Stock, and Reorder Points (ROP) to optimize supply chain efficiency.
"""

import math
import logging
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum

# Configure logging for audit trails
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ServiceLevel(Enum):
    """Statistical Z-scores for common service levels."""
    LOW_90 = 1.28
    MID_95 = 1.645
    HIGH_98 = 2.05
    CRITICAL_99 = 2.33

@dataclass(frozen=True)
class InventoryMetrics:
    sku: str
    annual_demand: float
    holding_cost_per_unit: float
    order_cost_fixed: float
    lead_time_days: int
    daily_demand_std_dev: float

class InventoryOptimizationEngine:
    """
    Industry-standard engine for calculating procurement triggers and 
    optimal stock levels using deterministic and probabilistic models.
    """

    def __init__(self, service_level: ServiceLevel = ServiceLevel.MID_95):
        self.z_score = service_level.value

    def calculate_eoq(self, metrics: InventoryMetrics) -> float:
        """
        Calculates Economic Order Quantity to minimize total holding and ordering costs.
        Formula: sqrt((2 * Demand * Order Cost) / Holding Cost)
        """
        try:
            eoq = math.sqrt((2 * metrics.annual_demand * metrics.order_cost_fixed) / metrics.holding_cost_per_unit)
            return round(eoq, 2)
        except ZeroDivisionError:
            logger.error(f"Holding cost for {metrics.sku} cannot be zero.")
            raise

    def calculate_safety_stock(self, metrics: InventoryMetrics) -> int:
        """
        Calculates Safety Stock required to buffer against demand variability 
        during lead time.
        Formula: Z * std_dev * sqrt(lead_time)
        """
        safety_stock = self.z_score * metrics.daily_demand_std_dev * math.sqrt(metrics.lead_time_days)
        return math.ceil(safety_stock)

    def calculate_reorder_point(self, metrics: InventoryMetrics) -> int:
        """
        Calculates the Reorder Point (ROP).
        Formula: (Average Daily Demand * Lead Time) + Safety Stock
        """
        daily_demand_avg = metrics.annual_demand / 365
        lead_time_demand = daily_demand_avg * metrics.lead_time_days
        safety_stock = self.calculate_safety_stock(metrics)
        
        rop = lead_time_demand + safety_stock
        return math.ceil(rop)

    def get_inventory_strategy(self, metrics: InventoryMetrics) -> Dict:
        """Generates a complete replenishment strategy for a specific SKU."""
        eoq = self.calculate_eoq(metrics)
        rop = self.calculate_reorder_point(metrics)
        ss = self.calculate_safety_stock(metrics)

        strategy = {
            "sku": metrics.sku,
            "economic_order_quantity": eoq,
            "reorder_point": rop,
            "safety_stock_buffer": ss,
            "annual_orders": round(metrics.annual_demand / eoq, 1)
        }
        
        logger.info(f"Strategy generated for SKU {metrics.sku}: ROP={rop}, EOQ={eoq}")
        return strategy

# --- Example Usage ---
if __name__ == "__main__":
    # Example: High-value electronics component
    component_data = InventoryMetrics(
        sku="CPU-GH-9000",
        annual_demand=12000,        # Units per year
        holding_cost_per_unit=15.0, # Cost to store 1 unit/year
        order_cost_fixed=500.0,     # Shipping/Admin cost per order
        lead_time_days=14,          # 2 weeks lead time
        daily_demand_std_dev=5.2    # Volatility in sales
    )

    optimizer = InventoryOptimizationEngine(ServiceLevel.HIGH_98)
    plan = optimizer.get_inventory_strategy(component_data)

    print(f"--- Inventory Optimization Plan for {plan['sku']} ---")
    print(f"Recommended Order Quantity (EOQ): {plan['economic_order_quantity']}")
    print(f"Trigger Reorder At (ROP): {plan['reorder_point']} units")
    print(f"Safety Stock Buffer: {plan['safety_stock_buffer']} units")
```
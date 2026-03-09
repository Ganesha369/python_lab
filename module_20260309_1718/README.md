# InvIntel: Specialized Inventory Intelligence Module

## Industry: Logistics & Supply Chain Management

### Business Value
In the modern supply chain, **stockouts** result in lost revenue, while **overstocking** ties up capital and increases warehousing costs. This module provides a data-driven approach to replenishment by automating the calculation of Reorder Points (ROP) and Economic Order Quantities (EOQ).

*   **Reduction in Stockouts:** Uses safety stock calculations based on demand volatility (Standard Deviation) and service level targets.
*   **Capital Optimization:** EOQ formula ensures that order sizes balance administrative setup costs against annual holding costs.
*   **Automated Forecasting:** Implements Simple Exponential Smoothing (SES) to weigh recent demand more heavily than older data, adapting quickly to market shifts.

### Tech Stack
*   **Language:** Python 3.10+
*   **Data Validation:** `Pydantic` for strict type enforcement and schema validation.
*   **Standard Library:** `math` for statistical computations, `logging` for audit trails.
*   **Design Pattern:** Strategy Pattern (via Forecaster class) and Data Transfer Objects (DTOs).

### Key Features
1.  **Dynamic Safety Stock:** Automatically adjusts based on the "Z-score" (confidence interval) and lead-time variability.
2.  **Effective Inventory Tracking:** Considers "Inventory Position" (On-Hand + On-Order - Backlog) rather than just physical stock.
3.  **Exponential Smoothing:** A lightweight alternative to heavy ML models for predictable, short-term demand forecasting.

### Implementation Guide
The module is designed to be integrated into an existing ERP or WMS (Warehouse Management System). 
1.  **Ingest Data:** Pipe SKU metadata and daily transactional sales into the `Product` and `InventoryState` models.
2.  **Run Engine:** Instantiate the `ReplenishmentEngine` daily or per-shift.
3.  **Trigger Actions:** Use the `action_required` boolean to trigger automated Purchase Order (PO) drafts in your procurement system.
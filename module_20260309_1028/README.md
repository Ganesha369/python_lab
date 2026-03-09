# LogiFlow: Inventory Optimization Engine

## 1. Introduction
The **LogiFlow Inventory Optimization Module** is a specialized Python component designed for the **Logistics and Supply Chain Management** industry. It provides data-driven insights into procurement timing and quantity, moving away from "gut-feeling" ordering toward a mathematically optimized approach.

## 2. Tech Stack
*   **Python 3.10+**: Leveraging modern features like `dataclasses` for clean data structures and `Type Hinting` for robust IDE support.
*   **Standard Library (`math`, `logging`)**: Zero-dependency core logic ensures high portability and easy integration into existing ERP or WMS systems.
*   **Logging**: Built-in audit trails for tracking strategy generation and error handling.

## 3. Business Value

### Cost Reduction
*   **Minimize Carrying Costs**: By calculating the **Economic Order Quantity (EOQ)**, the module ensures you aren't overstocking, which ties up capital and increases warehousing expenses.
*   **Reduced Administrative Overhead**: Automated calculation of annual order frequency helps procurement teams plan their workloads more effectively.

### Risk Mitigation
*   **Prevent Stock-outs**: The **Safety Stock** calculation uses statistical Z-scores to account for demand volatility. This ensures a 95%+ service level even during unexpected demand spikes.
*   **Lead Time Protection**: The **Reorder Point (ROP)** logic integrates lead-time demand, ensuring that new stock arrives exactly as current stock reaches safety levels.

### Scalability
*   The module is designed as a "plug-and-play" engine. It can be wrapped in a FastAPI/Flask layer to serve as a microservice or integrated directly into a Pandas-based data pipeline for bulk processing of thousands of SKUs.

## 4. Operational Logic
1.  **Input**: The system accepts `InventoryMetrics` including annual demand, costs, and lead times.
2.  **Process**: It applies deterministic models for EOQ and probabilistic models (Standard Deviation of Demand) for Safety Stock.
3.  **Output**: A structured `Dict` containing actionable procurement triggers, ready for consumption by automated purchasing systems or dashboard visualizations.
# LogiRoute-Py: Intelligent Logistics Optimization Engine

## 1. Overview
`LogiRoute-Py` is a specialized Python module designed for the **Third-Party Logistics (3PL) and Supply Chain Management** industry. It provides a robust framework for route sequencing, delivery cost estimation, and environmental impact (CO2) tracking. The module uses a mathematical approach to solve the Traveling Salesperson Problem (TSP) using a Nearest Neighbor heuristic, ensuring efficient delivery paths from a central hub.

## 2. Tech Stack
*   **Language:** Python 3.10+
*   **Data Validation:** `Pydantic` for strict type checking and runtime schema validation.
*   **Architecture:** Object-Oriented Design (OOD) with clear separation of concerns between geographical math, vehicle modeling, and business logic.
*   **Testing/Logging:** Integrated `logging` for audit trails and `dataclasses`/`enums` for domain modeling.

## 3. Business Value

### Operational Efficiency
*   **Route Optimization:** Reduces total mileage by sequencing stops based on geographical proximity, directly lowering wear-and-tear and fuel consumption.
*   **Dynamic Vehicle Profiles:** Allows logistics managers to compare costs between Electric Vehicles (EVs) and traditional Diesel fleets.

### Financial Accuracy
*   **Precise Costing:** Provides instant delivery cost estimation based on distance and vehicle-specific overhead, enabling more accurate customer quoting.
*   **Payload Management:** Foundation for future capacity-constrained routing to prevent vehicle overloading.

### Sustainability (ESG)
*   **Carbon Tracking:** Automatically calculates CO2 emissions for diesel fleets, supporting Corporate Social Responsibility (CSR) reporting and helping companies prepare for "Green" carbon tax regulations.

## 4. Key Features
*   **Haversine Integration:** Accurate distance calculation accounting for the Earth's curvature.
*   **Extensible Vehicle Logic:** Easily add more vehicle types (drones, cargo bikes) by extending the `VehicleProfile`.
*   **JSON-Ready Output:** The `RouteSummary` is serializable, making it ready for integration with modern REST APIs or React/Vue dashboards.

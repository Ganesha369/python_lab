```python
"""
LogiChain Optimizer: Core Routing & Emissions Module
Industry: Logistics and Supply Chain Management

This module provides high-precision distance calculation, cost estimation, 
and carbon footprint analysis for freight operations.
"""

from dataclasses import dataclass
from math import radians, cos, sin, asin, sqrt
from typing import List, Optional
from enum import Enum


class TransportMode(Enum):
    HEAVY_TRUCK = 0.85  # kg CO2 per km
    LIGHT_TRUCK = 0.45
    EV_VAN = 0.12
    CARGO_PLANE = 2.50


@dataclass(frozen=True)
class Location:
    name: str
    latitude: float
    longitude: float

    def __post_init__(self):
        if not (-90 <= self.latitude <= 90):
            raise ValueError(f"Invalid latitude: {self.latitude}")
        if not (-180 <= self.longitude <= 180):
            raise ValueError(f"Invalid longitude: {self.longitude}")


@dataclass
class ShipmentMetrics:
    total_distance_km: float
    estimated_cost_usd: float
    carbon_footprint_kg: float


class RouteOptimizer:
    """
    Handles spatial calculations and business logic for logistics efficiency.
    """
    
    EARTH_RADIUS_KM = 6371.0

    def __init__(self, base_rate_per_km: float = 1.25):
        self.base_rate_per_km = base_rate_per_km

    def calculate_haversine_distance(self, origin: Location, destination: Location) -> float:
        """
        Calculates the great-circle distance between two points on a sphere.
        """
        lon1, lat1, lon2, lat2 = map(radians, [
            origin.longitude, origin.latitude, 
            destination.longitude, destination.latitude
        ])

        dlon = lon2 - lon1
        dlat = lat2 - lat1
        
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a))
        
        return round(c * self.EARTH_RADIUS_KM, 2)

    def analyze_shipment(
        self, 
        route: List[Location], 
        mode: TransportMode, 
        weight_tons: float = 1.0
    ) -> ShipmentMetrics:
        """
        Aggregates data for a multi-stop route.
        """
        if len(route) < 2:
            raise ValueError("A route must contain at least an origin and a destination.")

        total_km = 0.0
        for i in range(len(route) - 1):
            total_km += self.calculate_haversine_distance(route[i], route[i+1])

        # Business Logic: Costs scale with distance and weight
        cost = total_km * self.base_rate_per_km * (1 + (weight_tons * 0.1))
        
        # ESG Logic: Carbon emissions
        emissions = total_km * mode.value * weight_tons

        return ShipmentMetrics(
            total_distance_km=round(total_km, 2),
            estimated_cost_usd=round(cost, 2),
            carbon_footprint_kg=round(emissions, 2)
        )


# Example Usage
if __name__ == "__main__":
    optimizer = RouteOptimizer(base_rate_per_km=1.50)
    
    warehouses = [
        Location("NYC_Hub", 40.7128, -74.0060),
        Location("Philly_Dist", 39.9526, -75.1652),
        Location("DC_Terminal", 38.9072, -77.0369)
    ]
    
    analysis = optimizer.analyze_shipment(
        route=warehouses, 
        mode=TransportMode.HEAVY_TRUCK,
        weight_tons=5.5
    )
    
    print(f"Route Summary for {warehouses[0].name} to {warehouses[-1].name}:")
    print(f"Distance: {analysis.total_distance_km} km")
    print(f"Est. Cost: ${analysis.estimated_cost_usd}")
    print(f"CO2 Impact: {analysis.carbon_footprint_kg} kg")
```
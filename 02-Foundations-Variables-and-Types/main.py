# ---------------------------------------------------------
# SDE-2 FOUNDATIONS: HERO INVENTORY SYSTEM
# This script demonstrates variables, types, and f-strings.
# ---------------------------------------------------------

# 1. Variable Initialization (Various Types)
hero_name = "Spartan-117"      # String
level = 50                     # Integer
shield_strength = 75.25        # Float
has_keycard = False            # Boolean

# 2. Pythonic Variable Manipulation
# We can update variables based on their current value
shield_strength = shield_strength + 10.0  # Leveling up the shield

# 3. Type Inspection
# As an SDE, we often debug by checking types
print("--- DEBUG INFO ---")
print(f"Variable 'hero_name' is type: {type(hero_name)}")
print(f"Variable 'level' is type: {type(level)}")
print(f"Variable 'shield_strength' is type: {type(shield_strength)}")
print(f"Variable 'has_keycard' is type: {type(has_keycard)}")
print("------------------\n")

# 4. The Output (Using f-strings for clean display)
print("--- MISSION BRIEFING ---")
print(f"Hero Name: {hero_name}")
print(f"Current Level: {level}")
print(f"Shield Status: {shield_strength}%")
print(f"Objective Complete: {has_keycard}")

# 5. Demonstrating Dynamic Typing
# Note: Just because you CAN change a type, doesn't mean you always should!
level = "Maximum Level" 
print(f"\nUpdate: Hero has reached {level}.")
# ---------------------------------------------------------
# SDE-2 FOUNDATIONS: SYNTAX AND OUTPUT
# Project: The Digital Business Card
# ---------------------------------------------------------

# 1. Defining our data (The "Variables")
developer_name = "Alex"
role = "Software Development Engineer"
company = "Microsoft"
languages = "Python, C#, TypeScript"
years_exp = 2

# 2. Level 4 Multi-line String for the Card Layout
header = """
*****************************************
*        PROFESSIONAL PROFILE           *
*****************************************
"""

# 3. Using F-Strings for clean, readable output (Level 2)
# We use \n for spacing and \t for indentation (Level 4)
print(header)
print(f"Name:\t\t{developer_name}")
print(f"Position:\t{role}")
print(f"Company:\t{company}")
print(f"Experience:\t{years_exp} Years")
print(f"Tech Stack:\t{languages}")

# 4. Finalizing with a footer (Level 0/1)
footer_msg = "System Status: Online & Verified"
print("\n" + "-" * 41)
print(footer_msg)
print("-" * 41)

# End of script
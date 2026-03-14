import streamlit as st
import time

# --- STREAMLIT UI SETUP ---
st.set_page_config(page_title="Maze Solver SDE Edition")
st.title("🧩 Maze Solver: Backtracking Visualizer")
st.write("Watch how the computer 'thinks' and 'backtracks' when it hits a wall!")

# 1. THE MAZE DATA (0 = Path, 1 = Wall, 2 = Solution Path)
# You can change this grid to make it harder!
MAZE = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

N = len(MAZE)

def draw_maze(grid, current_pos=None):
    """Helper function to draw the maze with colors"""
    display_grid = []
    for r in range(N):
        row_icons = []
        for c in range(N):
            if (r, c) == current_pos:
                row_icons.append("🤖") # Robot location
            elif grid[r][c] == 1:
                row_icons.append("⬛") # Wall
            elif grid[r][c] == 2:
                row_icons.append("🟩") # Path found
            else:
                row_icons.append("⬜") # Empty space
        display_grid.append(row_icons)
    return display_grid

# 2. THE BACKTRACKING LOGIC
def solve_maze(grid, r, c, placeholder):
    # Base Case: If we reached the bottom-right corner
    if r == N - 1 and c == N - 1:
        grid[r][c] = 2
        return True

    # Check if current position is valid
    if r >= 0 and c >= 0 and r < N and c < N and grid[r][c] == 0:
        # Mark as part of the path (The "Breadcrumb")
        grid[r][c] = 2
        
        # Visualize the step
        placeholder.table(draw_maze(grid, (r, c)))
        time.sleep(0.3)

        # Move Down
        if solve_maze(grid, r + 1, c, placeholder):
            return True
        # Move Right
        if solve_maze(grid, r, c + 1, placeholder):
            return True
        # Move Up
        if solve_maze(grid, r - 1, c, placeholder):
            return True
        # Move Left
        if solve_maze(grid, r, c - 1, placeholder):
            return True

        # BACKTRACKING: If none of the moves worked, unmark this spot
        grid[r][c] = 0
        placeholder.table(draw_maze(grid, (r, c)))
        st.toast(f"Backtracking from {r}, {c}...", icon="⚠️")
        time.sleep(0.2)
        return False

    return False

# --- STREAMLIT INTERACTION ---
if st.button("Start Solving!"):
    # Create a copy of the maze so we don't ruin the original
    maze_copy = [row[:] for row in MAZE]
    visual_placeholder = st.empty()
    
    if solve_maze(maze_copy, 0, 0, visual_placeholder):
        st.success("🎉 Exit Found! The algorithm backtracked where needed and found the goal.")
        st.balloons()
    else:
        st.error("No path exists for this maze.")

st.info("""
**Legend:**
- ⬛ = Wall (No entry)
- ⬜ = Unexplored Path
- 🟩 = Breadcrumb (Current Path)
- 🤖 = The Algorithm's Current Focus
""")
import os

def fix_old_projects():
    # Change this to your specific lab URL
    base_url = "https://ganesha-ai-lab.streamlit.app/" 
    
    # Get all project folders (those starting with numbers)
    projects = [d for d in os.listdir('.') if os.path.isdir(d) and d[0].isdigit()]

    for project in projects:
        learn_path = f"{project}/LEARN.md"
        if os.path.exists(learn_path):
            with open(learn_path, "r") as f:
                lines = f.readlines()

            # Check if link already exists to avoid double-adding
            if any("CHECK LIVE RESULT" in line for line in lines):
                print(f"✅ Skipping {project}: Link already exists.")
                continue

            # We want to insert the link after the Summary (usually line 3)
            # Format: ### [🚀 CHECK LIVE RESULT](URL?path=Project-Name)
            live_link = f"### [🚀 CHECK LIVE RESULT]({base_url}?path={project})\n\n---\n\n"
            
            # Insert at index 3 (after the title and summary)
            lines.insert(3, live_link)

            with open(learn_path, "w") as f:
                f.writelines(lines)
            print(f"✨ Fixed: {project}")

if name == "main":
    fix_old_projects()

import os

def load_content(topic):
    # Normalize topic name to match file naming
    filename = topic.lower().replace(" ", "_") + ".md"

    # Try both class folders
    for class_folder in ["class11", "class12"]:
        path = os.path.join("content", class_folder, filename)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return f.read()

    return "🚫 Content not available yet."

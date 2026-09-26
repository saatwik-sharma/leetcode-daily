import os
import re
from datetime import date

# --------------------------------------------------
# Find today's Day number
# --------------------------------------------------

existing_days = []

for item in os.listdir("."):
    match = re.match(r"Day-(\d+)", item)

    if match and os.path.isdir(item):
        existing_days.append(int(match.group(1)))

day = max(existing_days, default=0) + 1

folder = f"Day-{day:03d}"
os.makedirs(folder, exist_ok=True)

today = date.today().strftime("%d %b %Y")

print("=" * 50)
print(f"🚀 LEETCODE DAY {day:03d}")
print(f"📅 {today}")
print("=" * 50)

# --------------------------------------------------
# Number of problems
# --------------------------------------------------

while True:
    try:
        count = int(input("\nHow many problems did you solve today? "))
        if count > 0:
            break
        print("Enter a number greater than 0.")
    except ValueError:
        print("Please enter a valid number.")

problems = []

# --------------------------------------------------
# Get information for each problem
# --------------------------------------------------

for i in range(1, count + 1):

    print(f"\n--- Problem {i} ---")

    problem = input("Problem name: ").strip()
    difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
    topic = input("Topic: ").strip()
    link = input("LeetCode link: ").strip()

    # Convert problem name into filename
    filename = problem.lower()
    filename = re.sub(r"[^a-z0-9]+", "-", filename)
    filename = filename.strip("-")

    file_path = os.path.join(folder, filename + ".cpp")

    # Create C++ file
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"""/*
Day: {day:03d}
Date: {today}

Problem: {problem}
Difficulty: {difficulty}
Topic: {topic}
LeetCode: {link}
*/

#include <bits/stdc++.h>
using namespace std;

class Solution {{
public:

    // Write your solution here

}};
""")

    problems.append({
        "name": problem,
        "difficulty": difficulty,
        "topic": topic,
        "link": link,
        "file": filename + ".cpp"
    })

    print(f"✅ Created {folder}/{filename}.cpp")


# --------------------------------------------------
# Update README
# --------------------------------------------------

readme_path = "README.md"

if os.path.exists(readme_path):

    with open(readme_path, "r", encoding="utf-8") as f:
        readme = f.read()

else:

    readme = """# 🚀 LeetCode Daily

My daily LeetCode journey.

## 📊 Progress

| Day | Date | Problems | Topics |
|---|---|---:|---|
"""

# Find the progress table
table_marker = "| Day | Date | Problems | Topics |"

if table_marker not in readme:

    readme += f"""

## 📊 Progress

{table_marker}
|---|---|---:|---|
"""

# Create today's row
topics = ", ".join(sorted(set(p["topic"] for p in problems)))

new_row = f"| {day:03d} | {today} | {len(problems)} | {topics} |"

# Insert row immediately after table separator
lines = readme.splitlines()

for i, line in enumerate(lines):

    if line.strip() == "|---|---|---:|---|":

        lines.insert(i + 1, new_row)
        break

readme = "\n".join(lines) + "\n"

# --------------------------------------------------
# Save README
# --------------------------------------------------

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme)

print("\n" + "=" * 50)
print(f"🔥 DAY {day:03d} COMPLETED")
print(f"📚 Problems solved: {len(problems)}")
print(f"📁 Folder: {folder}")
print("📝 README updated")
print("=" * 50)

print("\nNext steps:")
print("1. Put your accepted solutions into the .cpp files.")
print("2. Run:")
print("   git add .")
print(f'   git commit -m "Day {day:03d}: {len(problems)} LeetCode problems"')
print("   git push")
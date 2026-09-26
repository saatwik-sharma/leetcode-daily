import os
import re
from datetime import date

# ==================================================
# SETTINGS
# ==================================================

today = date.today()

# ==================================================
# FIND / CREATE TODAY'S DAY
# ==================================================

# Look for a file that stores the last date
state_file = ".leetcode_state"

if os.path.exists(state_file):

    with open(state_file, "r", encoding="utf-8") as f:
        last_date, day_number = f.read().strip().split(",")

    day_number = int(day_number)

    if last_date == str(today):
        # Same day → use the same Day folder
        current_day = day_number
    else:
        # New day → increase day number
        current_day = day_number + 1

else:

    # First time running the script
    current_day = 1


folder = f"Day-{current_day:03d}"
os.makedirs(folder, exist_ok=True)

# Save today's date and day number
with open(state_file, "w", encoding="utf-8") as f:
    f.write(f"{today},{current_day}")


# ==================================================
# DISPLAY
# ==================================================

print("=" * 50)
print(f"🚀 LEETCODE DAY {current_day:03d}")
print(f"📅 {today.strftime('%d %B %Y')}")
print(f"📁 Folder: {folder}")
print("=" * 50)


# ==================================================
# NUMBER OF PROBLEMS
# ==================================================

while True:

    try:

        count = int(input("\nHow many problems are you adding today? "))

        if count > 0:
            break

        print("Enter a number greater than 0.")

    except ValueError:

        print("Please enter a valid number.")


# ==================================================
# ADD PROBLEMS
# ==================================================

problems = []

for i in range(1, count + 1):

    print(f"\n--- Problem {i} ---")

    problem = input("Problem name: ").strip()

    difficulty = input(
        "Difficulty (Easy/Medium/Hard): "
    ).strip()

    topic = input("Topic: ").strip()

    link = input("LeetCode link: ").strip()


    # ------------------------------------------------
    # Convert problem name → filename
    # ------------------------------------------------

    filename = problem.lower()

    filename = re.sub(
        r"[^a-z0-9]+",
        "-",
        filename
    )

    filename = filename.strip("-")


    file_path = os.path.join(
        folder,
        filename + ".cpp"
    )


    # ------------------------------------------------
    # Avoid overwriting an existing solution
    # ------------------------------------------------

    if os.path.exists(file_path):

        print(
            f"⚠️ {filename}.cpp already exists."
        )

        continue


    # ------------------------------------------------
    # Create C++ file
    # ------------------------------------------------

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
f"""/*
Day: {current_day:03d}
Date: {today.strftime('%d %B %Y')}

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
"""
        )


    problems.append({
        "name": problem,
        "difficulty": difficulty,
        "topic": topic,
        "link": link,
        "file": filename + ".cpp"
    })


    print(
        f"✅ Created {folder}/{filename}.cpp"
    )


# ==================================================
# UPDATE README
# ==================================================

readme_path = "README.md"


if os.path.exists(readme_path):

    with open(
        readme_path,
        "r",
        encoding="utf-8"
    ) as f:

        readme = f.read()

else:

    readme = """# 🚀 LeetCode Daily

My daily LeetCode journey.

## 📊 Progress

| Day | Date | Problems | Topics |
|---|---|---:|---|
"""


# ==================================================
# MAKE SURE TABLE EXISTS
# ==================================================

table_header = "| Day | Date | Problems | Topics |"

table_separator = "|---|---|---:|---|"


if table_header not in readme:

    readme += f"""

## 📊 Progress

{table_header}
{table_separator}
"""


# ==================================================
# CHECK WHETHER TODAY IS ALREADY IN README
# ==================================================

lines = readme.splitlines()

day_string = f"| {current_day:03d} |"

already_exists = any(
    line.startswith(day_string)
    for line in lines
)


# ==================================================
# ADD / UPDATE README ROW
# ==================================================

if problems:

    topics = ", ".join(
        sorted(
            set(
                p["topic"]
                for p in problems
            )
        )
    )

    new_row = (
        f"| {current_day:03d} | "
        f"{today.strftime('%d %B %Y')} | "
        f"{len(problems)} | "
        f"{topics} |"
    )


    if not already_exists:

        for i, line in enumerate(lines):

            if line.strip() == table_separator:

                lines.insert(
                    i + 1,
                    new_row
                )

                break

    else:

        # Find today's row and update it
        for i, line in enumerate(lines):

            if line.startswith(day_string):

                lines[i] = new_row

                break


    readme = "\n".join(lines) + "\n"


# ==================================================
# SAVE README
# ==================================================

with open(
    readme_path,
    "w",
    encoding="utf-8"
) as f:

    f.write(readme)


# ==================================================
# FINISHED
# ==================================================

print("\n" + "=" * 50)

print(
    f"🔥 DAY {current_day:03d} UPDATED"
)

print(
    f"📚 Problems added: {len(problems)}"
)

print(
    f"📁 Folder: {folder}"
)

print(
    "📝 README updated"
)

print("=" * 50)

print("\nNext:")
print("1. Put your accepted solutions in the .cpp files.")
print("2. Run:")
print("   git add .")
print(
    f'   git commit -m "Day {current_day:03d}: '
    f'{len(problems)} LeetCode problems"'
)
print("   git push")
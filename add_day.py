import os
import re

# Find the next day number
existing_days = []

for item in os.listdir("."):
    match = re.match(r"Day-(\d+)$", item)

    if match and os.path.isdir(item):
        existing_days.append(int(match.group(1)))

day = max(existing_days, default=0) + 1

print(f"\n🚀 Starting Day {day:03d}\n")

problem = input("Problem name: ").strip()
difficulty = input("Difficulty (Easy/Medium/Hard): ").strip()
topic = input("Topic: ").strip()
leetcode_link = input("LeetCode link: ").strip()
filename = input("Solution filename (without extension): ").strip()

folder = f"Day-{day:03d}"
os.makedirs(folder, exist_ok=True)

file_path = os.path.join(folder, f"{filename}.cpp")

# Create solution file
with open(file_path, "w", encoding="utf-8") as f:
    f.write(f"""/*
Day: {day:03d}
Problem: {problem}
Difficulty: {difficulty}
Topic: {topic}
LeetCode: {leetcode_link}
*/

#include <bits/stdc++.h>
using namespace std;

class Solution {{
public:

    // Write your solution here

}};
""")

print(f"\n✅ Created {file_path}")
print(f"🔥 Day {day:03d} added successfully!")
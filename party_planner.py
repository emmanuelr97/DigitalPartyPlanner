#!/usr/bin/env python3
import cgi

items = [
    "Cake", "Balloons", "Music System", "Lights", "Catering Service",
    "DJ", "Photo Booth", "Tables", "Chairs", "Drinks", "Party Hats",
    "Streamers", "Invitation Cards", "Party Games", "Cleaning Service"
]
values = [20, 21, 10, 5, 8, 3, 15, 7, 12, 6, 9, 18, 4, 2, 11]

form = cgi.FieldStorage()
indices_input = form.getvalue('indices', '')
selected_indices = [int(idx.strip()) for idx in indices_input.split(',') if idx.strip().isdigit()]

selected_values = []
valid_indices = []
for idx in selected_indices:
    if 0 <= idx < len(values):
        selected_values.append(values[idx])
        valid_indices.append(idx)

if not selected_values:
    base_code = 0
else:
    base_code = selected_values[0]
    for val in selected_values[1:]:
        base_code &= val

adjusted_code = base_code
message = ""
if base_code == 0:
    adjusted_code += 5
    message = "Epic Party Incoming!"
elif base_code > 5:
    adjusted_code -= 2
    message = "Let's keep it classy!"
else:
    message = "Chill vibes only!"

print("Content-Type: text/html\n\n")
print("<html><body>")
print("<h1>Digital Party Planner</h1>")
print("<h2>Selected Items:</h2>")
print(", ".join([items[i] for i in valid_indices]))
print(f"<p>Base Party Code: {base_code}</p>")
print(f"<p>Adjusted Party Code: {adjusted_code}</p>")
print(f"<p>Message: {message}</p>")
print("</body></html>")
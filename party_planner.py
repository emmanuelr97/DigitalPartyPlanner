#!/usr/bin/env python3

import cgi
import cgitb

cgitb.enable()

print("Content-type: text/html\n\n") 

party_items = [
    ("Cake", 20),
    ("Balloons", 21),
    ("Music System", 10),
    ("Lights", 5),
    ("Catering Service", 8),
    ("DJ", 3),
    ("Photo Booth", 15),
    ("Tables", 7),
    ("Chairs", 12),
    ("Drinks", 6),
    ("Party Hats", 9),
    ("Streamers", 18),
    ("Invitation Cards", 4),
    ("Party Games", 2),
    ("Cleaning Service", 11)
]

print("<h1>Webserver 1:</h1>")

print("<h2>Available Party Items:</h2>")
print("<ul>")
for i, (item, value) in enumerate(party_items):
    print(f"<li>{i}: {item} (value = {value})</li>")
print("</ul>")

form = cgi.FieldStorage()

item_indices = form.getvalue("items", "") 

if item_indices.strip():
    indices = [idx.strip() for idx in item_indices.split(",")]
    valid_indices = []
    for idx in indices:
        if idx.isdigit():
            idx_val = int(idx)
            if 0 <= idx_val < len(party_items):
                valid_indices.append(idx_val)
    
    if valid_indices:
        selected_values = [party_items[idx][1] for idx in valid_indices]
        base_code = selected_values[0]
        for val in selected_values[1:]:
            base_code = base_code & val
        
        selected_names = [party_items[idx][0] for idx in valid_indices]
        
        print("<h2>Selected Items:</h2>")
        print(f"<p>{', '.join(selected_names)}</p>")
        
        if len(selected_values) > 1:
            bitwise_str = " & ".join(str(v) for v in selected_values)
            print(f"<p><strong>Base Party Code:</strong> {bitwise_str} = {base_code}</p>")
        else:
            print(f"<p><strong>Base Party Code:</strong> {base_code}</p>")
        
        message = ""
        adjusted_code = base_code
        
        if base_code == 0:
            adjusted_code += 5
            message = "Epic Party Incoming!"
        elif base_code > 5:
            adjusted_code -= 2
            message = "Let's keep it classy!"
        else:
            message = "Chill vibes only!"
        
        if base_code != adjusted_code:
            print(f"<p><strong>Adjusted Party Code:</strong> {base_code} -> {adjusted_code}</p>")
        
        print(f"<h3>Final Party Code: {adjusted_code}</h3>")
        print(f"<p><strong>Message:</strong> {message}</p>")
    else:
        print("<p>No valid item indices were selected!</p>")
else:
    print("<p>No items selected. Please provide item indices in the query string.</p>")
    print("<p>Example usage: ?items=0,1</p>")

<!DOCTYPE html>
<html>
<head>
    <title>Party Planner</title>
</head>
<body>
    <h1>Select Party Items</h1>
    <form action="/party_planner.py" method="GET">
        <div>
            <label>Indices (comma-separated):</label>
            <input type="text" name="indices" placeholder="e.g., 0, 2">
        </div>
        <button type="submit">Calculate</button>
    </form>
</body>
</html>
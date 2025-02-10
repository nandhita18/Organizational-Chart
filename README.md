Overview
A web-based application for visualizing hierarchical data using Flask, GoJS, and Pandas. It dynamically renders organizational structures and supports interactive exploration.

Features:
>Expandable and collapsible tree structure
>Interactive UI using GoJS
>Data processing from Excel
>REST API for fetching hierarchy

Installation:
git clone https://github.com/yourusername/organizational-chart.git
cd organizational-chart
pip install flask pandas openpyxl
python app.py

API Endpoints
GET /api/get-top-level - Fetches the root node
GET /api/get-children/<parent_id> - Fetches child nodes

Applications
Organizational Hierarchy
Business Dashboards
IT Infrastructure Mapping

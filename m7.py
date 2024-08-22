from graphviz import Digraph

# Create a new Digraph object with attributes to improve layout and style
mindmap = Digraph(comment='Aggressive Learning Mechanism', format='pdf')

# Set global graph attributes for style and layout
mindmap.attr(rankdir='TB', size='16,9!', pad='2.5', splines='true', nodesep='2', ranksep='8')
mindmap.attr('graph', bgcolor='lightgrey')  # Change background color to light gray
mindmap.attr('node', shape='ellipse', style='filled', color='lightblue', fontname='Arial', fontsize='100', margin='0.3')
mindmap.attr('edge', color='gray', penwidth='2')

# Root node
mindmap.node('A', 'Aggressive Learning Mechanism', shape='ellipse', style='filled', color='orange', fontcolor='white', fontsize='144', width='2')

# Main categories with different colors for visual distinction
mindmap.node('B1', 'Self-Motivation', color='lightcoral', fontsize='100')
mindmap.node('B2', 'Goal Setting', color='lightseagreen', fontsize='100')
mindmap.node('B3', 'Active Engagement', color='lightpink', fontsize='100')
mindmap.node('B4', 'Efficient Resource Utilization', color='lightsalmon', fontsize='100')
mindmap.node('B5', 'Time Management', color='lightsteelblue', fontsize='100')
mindmap.node('B6', 'Critical Thinking', color='lightgoldenrod', fontsize='100')
mindmap.node('B7', 'Feedback and Reflection', color='lightgreen', fontsize='100')

# Subcategories for Self-Motivation
mindmap.node('C1', 'Drive', color='lightcoral', fontsize='100')
mindmap.node('C2', 'Initiative', color='lightcoral', fontsize='100')

# Subcategories for Goal Setting
mindmap.node('C3', 'Clear Objectives', color='lightseagreen', fontsize='100')
mindmap.node('C4', 'Prioritization', color='lightseagreen', fontsize='100')

# Subcategories for Active Engagement
mindmap.node('C5', 'Participation', color='lightpink', fontsize='100')
mindmap.node('C6', 'Questioning', color='lightpink', fontsize='100')

# Subcategories for Efficient Resource Utilization
mindmap.node('C7', 'Diverse Sources', color='lightsalmon', fontsize='100')
mindmap.node('C8', 'Technology', color='lightsalmon', fontsize='100')

# Subcategories for Time Management
mindmap.node('C9', 'Schedule', color='lightsteelblue', fontsize='100')
mindmap.node('C10', 'Balance', color='lightsteelblue', fontsize='100')

# Subcategories for Critical Thinking
mindmap.node('C11', 'Analysis', color='lightgoldenrod', fontsize='100')
mindmap.node('C12', 'Application', color='lightgoldenrod', fontsize='100')

# Subcategories for Feedback and Reflection
mindmap.node('C13', 'Seek Feedback', color='lightgreen', fontsize='100')
mindmap.node('C14', 'Reflect', color='lightgreen', fontsize='100')

# Connect nodes
mindmap.edges([
    ('A', 'B1'), ('A', 'B2'), ('A', 'B3'), ('A', 'B4'), ('A', 'B5'), ('A', 'B6'), ('A', 'B7'),
    ('B1', 'C1'), ('B1', 'C2'),
    ('B2', 'C3'), ('B2', 'C4'),
    ('B3', 'C5'), ('B3', 'C6'),
    ('B4', 'C7'), ('B4', 'C8'),
    ('B5', 'C9'), ('B5', 'C10'),
    ('B6', 'C11'), ('B6', 'C12'),
    ('B7', 'C13'), ('B7', 'C14'),
])

# Render the mind map to a file with 16:9 aspect ratio
mindmap.render('Aggressive_Learning_Mechanism_16_9_CoolBGv2')

print("Mind map created successfully as 'Aggressive_Learning_Mechanism_16_9_CoolBGv2.pdf'")

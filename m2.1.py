from graphviz import Digraph

# Create a new Digraph object with attributes to improve layout and style
mindmap = Digraph(comment='How to Develop Your Mechanism', format='pdf')

# Set global graph attributes for style and layout
mindmap.attr(rankdir='TB', size='16,9!', pad='1.5', splines='true', nodesep='1', ranksep='1.5')
mindmap.attr('graph', bgcolor='lightblue')  # Change background color to light blue
mindmap.attr('node', shape='ellipse', style='filled', color='lightblue', fontname='Arial', fontsize='22', margin='0.3')
mindmap.attr('edge', color='gray', penwidth='2')

# Root node
mindmap.node('A', 'How to Develop Your Mechanism', shape='ellipse', style='filled', color='orange', fontcolor='white', fontsize='28', width='2')

# Main steps with different colors for visual distinction
mindmap.node('B1', 'Assess Your Current Approach', color='lightcoral', fontsize='24')
mindmap.node('B2', 'Experiment', color='lightseagreen', fontsize='24')
mindmap.node('B3', 'Adapt', color='lightpink', fontsize='24')
mindmap.node('B4', 'Commit', color='lightsteelblue', fontsize='24')

# Sub-points for Assess Your Current Approach
mindmap.node('C1', 'Identify what’s working', color='lightcoral', fontsize='22')
mindmap.node('C2', 'Identify what isn’t working', color='lightcoral', fontsize='22')

# Sub-points for Experiment
mindmap.node('C3', 'Try different techniques', color='lightseagreen', fontsize='22')
mindmap.node('C4', 'Use various tools', color='lightseagreen', fontsize='22')

# Sub-points for Adapt
mindmap.node('C5', 'Be flexible', color='lightpink', fontsize='22')
mindmap.node('C6', 'Change strategies as needed', color='lightpink', fontsize='22')

# Sub-points for Commit
mindmap.node('C7', 'Develop a routine', color='lightsteelblue', fontsize='22')
mindmap.node('C8', 'Ensure consistent progress', color='lightsteelblue', fontsize='22')

# Connect nodes
mindmap.edges([
    ('A', 'B1'), ('A', 'B2'), ('A', 'B3'), ('A', 'B4'),
    ('B1', 'C1'), ('B1', 'C2'),
    ('B2', 'C3'), ('B2', 'C4'),
    ('B3', 'C5'), ('B3', 'C6'),
    ('B4', 'C7'), ('B4', 'C8'),
])

# Render the mind map to a file with 16:9 aspect ratio
mindmap.render('Develop_Your_Mechanism_16_9_CoolBG')

print("Mind map created successfully as 'Develop_Your_Mechanism_16_9_CoolBG.pdf'")

# Graphviz Mind Maps

This repository contains examples of how to create visually appealing mind maps using Graphviz. The examples provided here were generated with the help of a custom Python script using the `graphviz` library.

## Files

### 1. **Aggressive Learning Mechanism**

- **File:** `Aggressive_Learning_Mechanism.pdf`
- **Description:** A mind map illustrating an aggressive learning mechanism, showing the various components and their interrelationships. The diagram uses colors and a 16:9 aspect ratio for improved readability.

### 2. **How to Develop Your Mechanism**

- **File:** `Develop_Your_Mechanism_16_9_CoolBG.pdf`
- **Description:** A mind map that outlines steps for developing a personal learning mechanism, such as assessing your current approach, experimenting, adapting, and committing to a routine. The diagram features a cool blue background and a 16:9 aspect ratio.

## Getting Started

To create similar mind maps using Graphviz, follow the steps below:

### Prerequisites

1. **Python 3.x**: Make sure you have Python installed on your system.
2. **Graphviz**: Install the Graphviz tool and library.

   ```bash
   sudo apt-get install graphviz
   pip install graphviz
   ```   
## Example Script
Below is an example script used to create a mind map:

   ```bash
   from graphviz import Digraph
   
   # Create a new Digraph object
   mindmap = Digraph(format='pdf')
   
   # Set global graph attributes for style and layout
   mindmap.attr(rankdir='TB', size='16,9!', pad='1.5', splines='true')
   mindmap.attr('graph', bgcolor='lightblue')
   mindmap.attr('node', shape='ellipse', style='filled', color='lightblue', fontname='Arial', fontsize='22', margin='0.3')
   mindmap.attr('edge', color='gray', penwidth='2')
   
   # Root node
   mindmap.node('A', 'Your Central Idea', shape='ellipse', style='filled', color='orange', fontcolor='white', fontsize='28')
   
   # Add more nodes and edges
   mindmap.node('B1', 'Main Idea 1', color='lightcoral')
   mindmap.node('B2', 'Main Idea 2', color='lightseagreen')
   
   mindmap.edge('A', 'B1')
   mindmap.edge('A', 'B2')
   
   # Render the mind map to a file
   mindmap.render('output_filename')
   ```

How to Use
Clone the Repository:

bash
Copy code
git clone https://github.com/rksiitd1/graphviz.git
cd graphviz
Create Your Own Mind Map:

You can use the provided script as a template. Modify the node names, colors, and structure according to your needs. Once done, run the script to generate your mind map.

bash
Copy code
python3 your_script.py
The output PDF file will be saved in the current directory.

# Getting Help from ChatGPT

You can use ChatGPT to generate the Graphviz code for your mind map by providing prompts like the following:

1. **Prompt for Mind Map Structure:**
"I need to create a mind map for [topic]. The main points are [Point 1, Point 2, ...], and under each main point, there are subpoints [Subpoint 1, Subpoint 2, ...]. Please provide a Graphviz script to create this mind map."

2. **Prompt for Customization:**
"Please help me customize the Graphviz script to add background colors, change font sizes, and adjust the layout to a 16:9 aspect ratio."

3. **Prompt for Improving Visuals:**
"How can I make the mind map more visually appealing with different colors for each main point and an overall cool background?"

By using these prompts, you can get tailored Graphviz scripts generated by ChatGPT to suit your specific requirements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

Special thanks to ChatGPT for assisting in generating the Graphviz scripts and ideas for improving the visuals.


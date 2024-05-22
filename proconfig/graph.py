import dash
import dash_cytoscape as cyto
from dash import html

def dash_cytoscape_graph(data):
    nodes = []
    edges = []

    root_transitions = data.get('transitions', {})

    for state, state_info in data['states'].items():
        nodes.append({"data": {"id": state, "label": state}})

        # 处理 transitions
        if 'transitions' in state_info:
            for transition, target in state_info['transitions'].items():
                if isinstance(target, list):
                    for t in target:
                        if isinstance(t, dict) and 'condition' in t:
                            edge_label = f"{transition} ({t['condition']})"
                        else:
                            edge_label = transition
                        edges.append({"data": {"source": state, "target": t['target'], "label": edge_label}})
                elif isinstance(target, dict):
                    for sub_target, sub_info in target.items():
                        if isinstance(sub_info, dict) and 'condition' in sub_info:
                            edge_label = f"{transition} ({sub_info['condition']})"
                        else:
                            edge_label = transition
                        edges.append({"data": {"source": state, "target": sub_target, "label": edge_label}})
                else:
                    edges.append({"data": {"source": state, "target": target, "label": transition}})

        # handle on_click
        if 'render' in state_info and 'buttons' in state_info['render']:
            for button in state_info['render']['buttons']:
                if 'on_click' in button:
                    on_click = button['on_click']
                    if isinstance(on_click, dict):
                        target_state = on_click['event']
                        edges.append({"data": {"source": state, "target": target_state, "label": f"on_click ({on_click['event']})"}})
                    elif on_click in root_transitions:
                        target_state = root_transitions[on_click]
                        edges.append({"data": {"source": state, "target": target_state, "label": f"on_click ({on_click})"}})

    app = dash.Dash(__name__)

    app.layout = html.Div([
        cyto.Cytoscape(
            id='cytoscape',
            elements=nodes + edges,
            layout={'name': 'cose'},
            style={'width': '100%', 'height': '100vh'},
            stylesheet=[
                {
                    'selector': 'node',
                    'style': {
                        'label': 'data(label)',
                        'background-color': '#0074D9',
                        'color': '#FFFFFF',
                        'text-valign': 'center',
                        'text-halign': 'center',
                        'font-size': '1px',
                        "width": "20px",
                        "height": "8px"
                    }
                },
                {
                    'selector': 'edge',
                    'style': {
                        'label': 'data(label)',
                        'line-color': '#0074D9',
                        'target-arrow-color': '#0074D9',
                        'target-arrow-shape': 'triangle',
                        'curve-style': 'bezier',
                        'font-size': '1px',
                        "width": "0.3px",
                        'arrow-scale': 0.2
                    }
                }
            ]
        )
    ],style={'width': '100%', 'height': '100vh'})

    app.run_server(debug=True)


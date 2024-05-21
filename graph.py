import json
import networkx as nx
import matplotlib.pyplot as plt

# 从文件中读取 JSON 数据
with open('./myshell-examples/advanced.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 创建一个有向图
G = nx.DiGraph()

# 获取根路径上的 transitions 映射关系
root_transitions = data.get('transitions', {})

# 添加节点和边
for state, state_info in data['states'].items():
    G.add_node(state)

    # 处理 transitions
    if 'transitions' in state_info:
        for transition, target in state_info['transitions'].items():
            if isinstance(target, list):
                for t in target:
                    edge_label = f"{transition} ({t['condition']})"
                    G.add_edge(state, t['target'], label=edge_label)
            else:
                if isinstance(target, dict):
                    # 如果 target 是字典，处理其内容
                    for sub_target, sub_info in target.items():
                        if isinstance(sub_info, dict) and 'condition' in sub_info:
                            edge_label = f"{transition} ({sub_info['condition']})"
                        else:
                            edge_label = transition
                        G.add_edge(state, sub_target, label=edge_label)
                else:
                    G.add_edge(state, target, label=transition)

    # 处理 buttons 的 on_click
    if 'render' in state_info and 'buttons' in state_info['render']:
        for button in state_info['render']['buttons']:
            if 'on_click' in button:
                on_click = button['on_click']
                if isinstance(on_click, dict):
                    target_state = on_click['event']
                    G.add_edge(state, target_state, label=f"on_click ({on_click['event']})")
                elif on_click in root_transitions:
                    target_state = root_transitions[on_click]
                    G.add_edge(state, target_state, label=f"on_click ({on_click})")

## 绘制图形
##pos = nx.spring_layout(G)  # 节点位置布局
## pos = nx.spring_layout(G, k=3)  # 调整 k 值来增加节点之间的距离
##pos = nx.planar_layout(G)# , k=3)  # 调整 k 值来增加节点之间的距离
#pos = nx.kamada_kawai_layout(G)
#
#nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
#
## 添加边标签
#edge_labels = nx.get_edge_attributes(G, 'label')
#nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
#
## 显示图形
#plt.show()


# 使用 spring_layout 布局
pos_spring = nx.spring_layout(G, k=2)  # 调整 k 值来增加节点之间的距离
plt.figure(figsize=(12, 8))
nx.draw(G, pos_spring, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos_spring, edge_labels=edge_labels, font_color='red')
plt.title('Spring Layout')
plt.show()

# 使用 kamada_kawai_layout 布局
pos_kamada_kawai = nx.kamada_kawai_layout(G)
plt.figure(figsize=(12, 8))
nx.draw(G, pos_kamada_kawai, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", arrows=True)
edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos_kamada_kawai, edge_labels=edge_labels, font_color='red')
plt.title('Kamada-Kawai Layout')
plt.show()

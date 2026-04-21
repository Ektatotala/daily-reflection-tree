import csv

def load_tree(file_path):
    tree = {}
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file, delimiter='\t')
        for row in reader:
            tree[row['id']] = row
    return tree

def run_tree(tree):
    current = "START"
    state = {}

    while True:
        node = tree[current]
        node_type = node['type']

        if node_type == "start":
            print(node['text'])
            current = "A1_Q1"

        elif node_type == "question":
            print("\n" + node['text'])
            options = node['options'].split('|')
            for i, opt in enumerate(options):
                print(f"{i+1}. {opt}")

            choice = int(input("Choose option: ")) - 1
            answer = options[choice]
            state[current] = answer

            # move to next node
            for nid, n in tree.items():
                if n['parentId'] == current:
                    current = nid
                    break

        elif node_type == "decision":
            rules = node['text'].split(';')
            prev = list(state.values())[-1]

            for rule in rules:
                cond, target = rule.split(':')
                cond = cond.replace("answer=", "")
                if prev in cond.split('|'):
                    current = target
                    break

        elif node_type == "reflection":
            print("\n💡 Reflection:", node['text'])
            for nid, n in tree.items():
                if n['parentId'] == current:
                    current = nid
                    break

        elif node_type == "bridge":
            current = node['target']

        elif node_type == "summary":
            print("\n📊 Summary:")
            print(node['text'])
            current = "END"

        elif node_type == "end":
            print("\nSession ended.")
            break

if __name__ == "__main__":
    tree = load_tree("../tree/reflection-tree.tsv")
    run_tree(tree)

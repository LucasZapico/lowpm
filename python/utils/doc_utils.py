import yaml

def update_doc(path, doc):
    
    with open(path, 'w') as file:
        file.write(doc)

def make_doc(markdown_content, frontmatter_data):
    frontmatter_yaml = yaml.dump(frontmatter_data)
    doc = f"---\n{frontmatter_yaml}---\n\n{markdown_content}" 
    return doc

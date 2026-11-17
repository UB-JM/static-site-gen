

class HTMLNode:
    def __init__(
            self, 
            tag: str|None, 
            value:str|None, 
            props: dict|None = None, 
            children: list["HTMLNode"]|None = None):
        self.tag = tag
        self.value = value
        self.props = props if props is not None else {}
        self.children = children if children is not None else []

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props}, children={self.children})"

    def to_html(self):
        raise NotImplementedError("to_html method isn't implemented yet")

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        return " ".join(f'{key}="{value}"' for key, value in self.props.items())

class LeafNode(HTMLNode):
    def __init__(self, tag: str|None, value:str|None, props: dict|None = None):
        super().__init__(tag, value, props, children=None)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return str(self.value)
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, props={self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str|None, props: dict|None = None, children: list[HTMLNode]|None = None):
        super().__init__(
            tag, 
            value=None, 
            props=props, 
            children=children)

    def to_html(self):
        if self.tag is None:
            raise ValueError("All parent nodes must have a tag.")
        if self.children is None or len(self.children) == 0:
            raise ValueError("All parents must have children.")
        html_output = f"<{self.tag}>"
        for child in self.children:
            html_output += child.to_html()
        html_output += f"</{self.tag}>"
        return html_output

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, props={self.props}, children={self.children})"   
    

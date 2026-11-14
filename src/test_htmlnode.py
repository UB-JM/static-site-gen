import unittest
from htmlnode import HTMLNode, LeafNode   

#tag: str|None, value:str|None, props: dict|None = None, children: list[object]|None = None
class TestHTMLNode(unittest.TestCase):
    def test_eq_1(self):
        node = HTMLNode("p", "None", None, None)
        output = ""
        #"href="https://www.google.com" target="_blank""
        self.assertEqual(HTMLNode.props_to_html(node), output)

    def test_eq_2(self):
        node = HTMLNode("a", "None", {"href": "https://www.google.com", "target": "_blank"}, None)
        output = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(HTMLNode.props_to_html(node), output)

    def test_eq_3(self):
        node = HTMLNode("div", "None", {"class": "container"}, [HTMLNode("p", "Hello World", None, None)])
        output = 'class="container"'
        self.assertEqual(HTMLNode.props_to_html(node), output)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_b(self):
        node = LeafNode("b", "A bold choice, that one!")
        self.assertEqual(node.to_html(), "<b>A bold choice, that one!</b>")

    def test_leaf_to_html_i(self):
        node = LeafNode("i", "Italic doesn't actually mean the peninsula!")
        self.assertEqual(node.to_html(), "<i>Italic doesn't actually mean the peninsula!</i>")

    


if __name__ == "__main__":
    unittest.main()

""" TEXT = "text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code"
    LINK = "link"
    IMAGE = "image" """
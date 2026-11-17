import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode   

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

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", children=[child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", children=[grandchild_node])
        parent_node = ParentNode("div", children=[child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_some_children(self):
        child_node1 = LeafNode("b", "Bold text")
        child_node2 = LeafNode(None, "Normal text")
        child_node3 = LeafNode("i", "italic text")
        child_node4 = LeafNode(None, "Normal text")
        parent_node = ParentNode("div", children=[child_node1, child_node2, child_node3, child_node4])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>Bold text</b>Normal text<i>italic text</i>Normal text</div>",
        )

        


if __name__ == "__main__":
    unittest.main()

""" TEXT = "text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code"
    LINK = "link"
    IMAGE = "image" """
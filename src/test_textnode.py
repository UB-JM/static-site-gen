import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url_none(self):
            node = TextNode("This is a text node", TextType.BOLD, None)
            node2 = TextNode("This is a text node", TextType.BOLD)
            self.assertEqual(node, node2)

    def test_uneq(self):
            node = TextNode("This is a text node", TextType.BOLD)
            node2 = TextNode("This is no text node", TextType.CODE)
            self.assertNotEqual(node, node2)

    def test_bold_it(self):
            node = TextNode("This is a text node", TextType.BOLD, None)
            node2 = TextNode("This is a text node", TextType.ITALIC, None)
            self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
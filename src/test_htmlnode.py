import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_values(self):
        n0 = HTMLNode("p", "Hello world!")
        
        self.assertEqual(n0.tag, "p")
        self.assertEqual(n0.value, "Hello world!")
        self.assertEqual(n0.children, None)
        self.assertEqual(n0.props, None)
        
    def test_props_to_html(self):
        n2 = HTMLNode("a", "My blog", None, {"href": "www.myblog.com", "target": "_blank"})
        n3 = HTMLNode("img", "Author's photo", None, {"src": "author.jpg", "width": "500", "height": "500"})
    
        self.assertEqual(n2.props_to_html(), " href=\"www.myblog.com\" target=\"_blank\"")
        self.assertEqual(n3.props_to_html(), " src=\"author.jpg\" width=\"500\" height=\"500\"")

    def test_repr(self):
        n4 = HTMLNode(None, None, None, None)

        self.assertEqual(n4.__repr__(), "HTMLNode(None, None, children: None, None)")

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node0 = LeafNode("p", "Hello world!")
        node1 = LeafNode("a", "Click me!", {"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(node0.to_html(), "<p>Hello world!</p>")
        self.assertEqual(node1.to_html(), "<a href=\"https://www.google.com\" target=\"_blank\">Click me!</a>")
    
    def test_repr(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.__repr__(), "LeafNode(p, This is a paragraph., None)")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_untagged_leaf_node(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "Italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>Italic text</i>Normal text</p>")
        
if __name__ == "__main__":
    unittest.main()

import unittest
from textnode import TextNode, TextType, text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        n0 = TextNode("This is a text node", TextType.BOLD)
        n1 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(n0, n1)

        n2 = TextNode("NASA", TextType.LINK, "https://www.nasa.gov/")
        n3 = TextNode("NASA", TextType.LINK, "https://www.nasa.gov/")
        self.assertEqual(n2, n3)
        
    def test_not_eq(self):
        a = TextNode("hello", TextType.TEXT)
        b = TextNode("hello", TextType.BOLD)
        self.assertNotEqual(a, b)
        
        n = TextNode("hello", TextType.BOLD)
        m = TextNode("world", TextType.BOLD)
        self.assertNotEqual(n, m)

        x = TextNode("The White House", TextType.LINK, "www.whitehouse.gov")
        y = TextNode("The White House", TextType.LINK, "www.whitehaus.gov")
        self.assertNotEqual(x, y)
        
    def test_repr(self):
        hi = TextNode("Hi Mom!", TextType.TEXT)
        self.assertEqual(hi.__repr__(), "TextNode(Hi Mom!, text, None)")

    def test_text_node_to_html_node(self):
        plain_node = TextNode("Hello world!", TextType.TEXT)
        self.assertEqual(
            text_node_to_html_node(plain_node).tag,
            None
        )
        self.assertEqual(
            text_node_to_html_node(plain_node).value,
            "Hello world!"
        )

        bold_node = TextNode("Emphasize this!", TextType.BOLD)
        self.assertEqual(
            text_node_to_html_node(bold_node).tag,
            "b"
        )
        self.assertEqual(
            text_node_to_html_node(bold_node).value,
            "Emphasize this!"
        )

        italic_node = TextNode("a subtler emphasis", TextType.ITALIC)
        self.assertEqual(
            text_node_to_html_node(italic_node).tag,
            "i"
        )
        self.assertEqual(
            text_node_to_html_node(italic_node).value,
            "a subtler emphasis"
        )

        code_node = TextNode("main()", TextType.CODE)
        self.assertEqual(
            text_node_to_html_node(code_node).tag,
            "code"
        )
        self.assertEqual(
            text_node_to_html_node(code_node).value,
            "main()"
        )

        link_node = TextNode("Click me", TextType.LINK, "https://www.google.com")
        link_node_to_html = text_node_to_html_node(link_node)
        self.assertEqual(
            link_node_to_html.tag,
            "a"
        )
        self.assertEqual(
            link_node_to_html.value,
            "Click me"
        )
        self.assertEqual(
            link_node_to_html.props["href"],
            "https://www.google.com"
        )

        image_node = TextNode("Author's photo", TextType.IMAGE, "author.jpg")
        image_node_to_html = text_node_to_html_node(image_node)
        self.assertEqual(
            image_node_to_html.tag,
            "img"
        )
        self.assertEqual(
            image_node_to_html.value,
            ""
        )
        self.assertEqual(
            image_node_to_html.props["src"],
            "author.jpg"
        )
        self.assertEqual(
            image_node_to_html.props["alt"],
            "Author's photo"
        )
        
if __name__ == "__main__":
    unittest.main()

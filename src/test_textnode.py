import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        n0 = TextNode("This is a text node", TextType.BOLD)
        n1 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(n0, n1)

        n2 = TextNode("NASA", TextType.LINK, "www.nasa.gov")
        n3 = TextNode("NASA", TextType.LINK, "www.nasa.gov")
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

if __name__ == "__main__":
    unittest.main()

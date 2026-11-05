class HTMLNode:
    def __init__(
            self,
            tag: str | None = None,
            value: str | None = None,
            children: list["HTMLNode"] | None = None,
            props: dict[str, str] | None = None
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> str:
        print("parent.to_html()")
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self) -> str:
        if not self.props:
            return ""
        else:
            sout = ""
            for k in self.props:
                sout += f" {k}=\"{self.props[k]}\""
            return sout

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(
            self,
            tag: str | None,
            value: str,
            props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self) -> str:
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            # return a string with properly formatted properties,
            #  or an empty string if props == None
            def format_props(props0: dict[str, str]) -> str:
                if not props0:
                    return ""
                else:
                    sout0 = ""
                    for k in props0:
                        sout0 += f" {k}=\"{props0[k]}\""
                    return sout0
                
            sout = f"<{self.tag}{self.props_to_html()}>"
            sout += self.value
            sout += f"</{self.tag}>"

            return sout

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(
            self,
            tag: str,
            children: list["HTMLNode"],
            props: dict[str, str] | None = None
    ) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("invalid HTML: no tag")

        if self.children is None:
            raise ValueError("invalid HTML: missing child nodes")

        sout = ""
        sout += f"<{self.tag}{self.props_to_html()}>"
        for node in self.children:
            sout += node.to_html()
        sout += f"</{self.tag}>"

        return sout
        

p0 = ParentNode("div", [LeafNode("p", "Paragraph 1"), LeafNode("p", "Paragraph 2")], {"prop1": "hello", "prop2": "world"})
print(p0)
print(p0.to_html())

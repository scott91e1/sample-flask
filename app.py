from molten import App, Route


def hello(name: str) -> str:
    return f"Hello {name}!"

app = App(routes=[Route("/hello/{name}", hello)])

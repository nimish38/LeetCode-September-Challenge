class BrowserHistory:

    def __init__(self, homepage: str):
        self.pages, self.curr = [homepage], 0

    def visit(self, url: str) -> None:
        del self.pages[self.curr + 1:]
        self.pages.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        self.curr -= min(steps, self.curr)
        return self.pages[self.curr]

    def forward(self, steps: int) -> str:
        self.curr += min(steps, len(self.pages) - self.curr)
        return self.pages[self.curr]



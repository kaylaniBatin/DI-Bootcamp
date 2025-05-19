#Daily Challenge : Pagination

import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        if items is None:
            items = []
        self.items = items
        self.page_size = page_size
        self.current_idx = 0  # 0-based index for the current page
        self.total_pages = math.ceil(len(self.items) / self.page_size)

    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num):
        if not isinstance(page_num, int):
            raise ValueError("Page number must be an integer.")
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page number must be between 1 and {self.total_pages}")
        self.current_idx = page_num - 1  # Convert to 0-based index

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return '\n'.join(str(item) for item in self.get_visible_items())


# Example usage
if __name__ == "__main__":
    alphabetList = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabetList, 4)

    print("Initial Page:")
    print(str(p))  # Should print a b c d each on a new line

    print("\nNext Page:")
    print(str(p.next_page()))

    print("\nGo to Page 3:")
    p.go_to_page(3)
    print(str(p))

    print("\nLast Page:")
    print(str(p.last_page()))

    print("\nFirst Page Again (Chained):")
    print(str(p.last_page().first_page()))

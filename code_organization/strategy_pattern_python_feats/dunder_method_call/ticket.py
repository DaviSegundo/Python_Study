import random
import string
from dataclasses import dataclass, field


def generate_id():
    return ''.join(random.choices(string.ascii_uppercase, k=6))

@dataclass
class SupportTicket:

    customer: str
    issue: str
    id: str = field(init=False)

    def __post_init__(self):
        self.id = generate_id()

    def process(self):
        print("==================================")
        print(f"Processing ticket id: {self.id}")
        print(f"Customer: {self.customer}")
        print(f"Issue: {self.issue}")
        print("==================================")

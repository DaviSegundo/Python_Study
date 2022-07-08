import string
import random
from typing import List, Callable
from dataclasses import dataclass, field


def generate_id(length=8) -> str:
    """helper function for generating an id."""
    return ''.join(random.choices(string.ascii_uppercase, k=length))


@dataclass
class SupportTicket:
    id: str = field(init=False)
    customer: str
    issue: str

    def __post_init__(self):
        self.id = generate_id()


def fifo_ordering(tickets_list: List[SupportTicket]) -> List[SupportTicket]:
    """Return list of tickets in fifo order."""
    return tickets_list.copy()

def filo_ordering(tickets_list: List[SupportTicket]) -> List[SupportTicket]:
    """Return list of tickets in filo order."""
    list_copy = tickets_list.copy()
    list_copy.reverse()
    return list_copy

def random_ordering(tickets_list: List[SupportTicket]) -> List[SupportTicket]:
    """Return list of tickets in random order."""
    list_copy = tickets_list.copy()
    random.shuffle(list_copy)
    return list_copy

def black_hole_ordering(tickets_list: List[SupportTicket]) -> List[SupportTicket]:
    """Return list of tickets empty."""
    return []


@dataclass
class CustomerSupport:
    tickets: List[SupportTicket] = field(default_factory=list)

    def create_ticket(self, customer, issue):
        """Add a new ticket to the list of tickets to process."""
        self.tickets.append(SupportTicket(customer=customer, issue=issue))

    def process_tickets(self, processing_strategy_function: Callable[[List[SupportTicket]], List[SupportTicket]]):
        """Process the tickets by a given type of strategy."""
        tickets_list = processing_strategy_function(self.tickets)
        
        if len(tickets_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in tickets_list:
            self.__process_ticket(ticket)

    def __process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")

if __name__ == '__main__':
    cs = CustomerSupport()
    cs.create_ticket(customer='Davi', issue='Fan')
    cs.create_ticket(customer='Segundo', issue='Battery')
    cs.create_ticket(customer='Pinheiro', issue='Speakers')
    
    cs.process_tickets(processing_strategy_function=filo_ordering)

from __future__ import annotations

from typing import Any


class Node:
    def __init__(self, data: Any = None, next: Node = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.volume = 0
        self.head = None
        self.current = None

    def __len__(self) -> int:
        return self.volume

    def __contains__(self, data: Any) -> bool:
        """ implementation 'in' """
        return self.search(data) >= 0

    def search(self, data: Any) -> int:
        count = 0
        pointer = self.head
        while pointer is not None:
            if pointer.data == data:
                self.current = pointer
                return count
            count += 1
            pointer = pointer.next
        return -1

    def add_first(self, data: Any) -> None:
        pointer = self.head
        self.head = self.current = Node(data, pointer)
        self.volume += 1

    def add_last(self, data: Any) -> None:
        if self.head is None:
            self.add_first(data)
        else:
            pointer = self.head
            while pointer.next is not None:
                pointer = pointer.next
            pointer.next = self.current = Node(data, None)
            self.volume += 1

    def remove_first(self) -> None:
        if self.head is not None:
            self.head = self.current = self.head.next
            self.volume -= 1

    def remove_last(self) -> None:
        if self.head is not None:
            if self.head.next is not None:
                self.remove_first()
            else:
                pointer = self.head
                previous_pointer = self.head

                while pointer.next is not None:
                    previous_pointer = pointer
                    pointer = pointer.next

                previous_pointer.next = None
                self.current = previous_pointer
                self.volume -= 1

    def remove(self, target: Node) -> None:
        if self.head is not None:
            if target is self.head:
                self.remove_first()
            else:
                pointer = self.head

                while pointer.next is not target:
                    pointer = pointer.next
                    if pointer is None:
                        return
                    pointer.next = target.next
                    self.current = pointer
                    self.volume -= 1

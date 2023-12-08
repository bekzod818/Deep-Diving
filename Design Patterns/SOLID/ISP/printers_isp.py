from abc import ABC, abstractmethod

"""Consider the following example of class hierarchy to model printing machines:"""


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white ...")

    def fax(self, document):
        raise NotImplementedError("Fax functionality not supported")

    def scan(self, document):
        raise NotImplementedError("Scan functionality not supported")


class ModernPrinter(Printer):
    def print(self, document):
        print(f"Printing {document} in color ...")

    def fax(self, document):
        print(f"Faxing {document} in ...")

    def scan(self, document):
        print(f"Scanning {document} in ...")


"""In this example, the base class, Printer, provides the interface that its subclasses must implement. OldPrinter inherits from Printer and must implement the same interface. However, OldPrinter doesn’t use the .fax() and .scan() methods because this type of printer doesn’t support these functionalities."""

"""This implementation violates the ISP because it forces OldPrinter to expose an interface that the class doesn’t implement or need. To fix this issue, you should separate the interfaces into smaller and more specific classes. Then you can create concrete classes by inheriting from multiple interface classes as needed:"""


class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass


class Fax(ABC):
    @abstractmethod
    def fax(self, document):
        pass


class Scan(ABC):
    @abstractmethod
    def scan(self, document):
        pass


class OldPrinter2(Printer):
    def print(self, document):
        print(f"Printing {document} in black and white ...")


class ModernPrinter2(Printer, Fax, Scan):
    def print(self, document):
        print(f"Printing {document} in color ...")

    def fax(self, document):
        print(f"Faxing {document} in ...")

    def scan(self, document):
        print(f"Scanning {document} in ...")


"""Now Printer, Fax, and Scanner are base classes that provide specific interfaces with a single responsibility each. To create OldPrinter, you only inherit the Printer interface. This way, the class won’t have unused methods. To create the ModernPrinter class, you need to inherit from all the interfaces. In short, you’ve segregated the Printer interface."""

"""This class design allows you to create different machines with different sets of functionalities, making your design more flexible and extensible."""

"""
Adapter pattern example: Adapting an XML printer to a JSON printer interface.
"""


class JSONPrinter:
    def print(self) -> str:
        return '{"message": "Hello, World!"}'


class XMLPrinter:
    def print(self) -> str:
        return "<message>Hello, World!</message>"


class XMLToJSONPrinterAdapter(JSONPrinter):
    def __init__(self, legacy_printer: XMLPrinter) -> None:
        self.legacy_printer = legacy_printer

    def print(self) -> str:
        output = self.legacy_printer.print()
        key = output[1 : output.find(">")]
        value = output[output.find(">") + 1 : output.rfind("<")]
        return f'{{"{key}": "{value}"}}'


def print_data(printer: JSONPrinter):
    return printer.print()


if __name__ == "__main__":
    json_printer = JSONPrinter()
    print(print_data(json_printer))

    xml_printer = XMLPrinter()
    xml_printer_with_adapter = XMLToJSONPrinterAdapter(xml_printer)
    print(print_data(xml_printer_with_adapter))

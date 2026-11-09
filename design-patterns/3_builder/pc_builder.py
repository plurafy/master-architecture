class Computer:
    def __init__(self) -> None:
        self.cpu: str | None = None
        self.ram: int | None = None
        self.storage: int | None = None
        self.gpu: str | None = None
        self.os = "Linux"

    def __str__(self) -> str:
        specs = [
            f"CPU: {self.cpu}",
            f"RAM: {self.ram}GB",
            f"STORAGE: {self.storage}GB",
            f"GPU: {self.gpu}" if self.gpu else "GPU: Integrated",
            f"OS: {self.os}",
        ]

        return f"Computer Specs: [{', '.join(specs)}]"


class ComputerBuilder:
    def __init__(self) -> None:
        self.computer = Computer()

    def add_cpu(self, cpu: str):
        self.computer.cpu = cpu
        return self

    def add_ram(self, ram: int):
        self.computer.ram = ram
        return self

    def add_storage(self, storage: int):
        self.computer.storage = storage
        return self

    def add_gpu(self, gpu: str):
        self.computer.gpu = gpu
        return self

    def add_os(self, os: str):
        self.computer.os = os
        return self

    def build(self) -> Computer:
        # Step-level validation can happen right before returning
        if not self.computer.cpu or not self.computer.ram:
            raise ValueError("CPU and RAM are mandatory components.")
        return self.computer


if __name__ == "__main__":
    # Building a high-end gaming PC using method chaining
    gaming_pc = (
        ComputerBuilder()
        .add_cpu("Intel Core i9")
        .add_ram(32)
        .add_storage(2000)
        .add_gpu("NVIDIA RTX 4090")
        .add_os("Windows 11")
        .build()
    )

    print(gaming_pc)

    # Building a basic budget PC (skipping optional fields like GPU)
    office_pc = (
        ComputerBuilder().add_cpu("AMD Ryzen 5").add_ram(16).add_storage(512).build()
    )

    print(office_pc)

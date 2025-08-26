class CustomContext:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def open_resource(self):
        """This replaces __enter__, internally."""
        print(f"[Opening resource]: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def close_resource(self, exc_type, exc_value, traceback):
        """This replaces __exit__, internally."""
        print(f"[Closing resource]: {self.filename}")
        if self.file:
            self.file.close()


    def __enter__(self):
        return self.open_resource()

    def __exit__(self, exc_type, exc_value, traceback):
        self.close_resource(exc_type, exc_value, traceback)


if __name__ == "__main__":
    filename = "example_custom.txt"

    with CustomContext(filename, "w") as f:
        f.write("This file was written using a custom-named context manager.\n")
        f.write("It uses open_resource() and close_resource() internally.\n")

    with CustomContext(filename, "r") as f:
        print("\n[File Content]:")
        print(f.read())

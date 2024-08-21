class Database:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.dict = self.dictionary()

    def dictionary(self) -> dict:
        with open(self.file_path, "r") as file:
            out = {}
            lst = file.read().split()
            for entry in lst:
                name = entry.split("|")[0]
                hash = entry.split("|")[1]
                out[name] = hash
            return out

    def add_entry(self, entry: tuple) -> None:
        with open(self.file_path, 'a') as file:
            file.write(f"{entry[0]}|{entry[1]}\n")

    def find_entry(self, username) -> tuple:
        for entry in self.dictionary().items():
            if entry[0] == username:
                return entry
        return None


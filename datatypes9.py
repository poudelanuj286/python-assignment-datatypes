class Exchange:
    def __init__(self, string):
        self.string = string

    def form_string(self):
        first_character = self.string[0]
        last_character = self.string[-1]
        new_string = last_character + self.string[1:-1] + first_character
        return new_string


if __name__ == "__main__":
    string = input("Enter a string: ")
    obj = Exchange(string)
    new_string = obj.form_string()
    print("New String:", new_string)
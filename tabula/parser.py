class Comment:
    def __init__(self):
        self.data = dict()

    def __repr__(self):
        return "{}".format(self.data)

    def read(self, com):
        if com.startswith("@brief"):
            self.data["brief"] = com


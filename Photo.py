class Photo:

    def __init__(self, id, orientation, tags) -> None:
        self.id = id
        self.tags = tags
        self.orientation = orientation
        # print(f'Create photo id={self.id} orientation={self.orientation} tags={self.tags}')
class Product:

    def __init__(self, title, price, about, link, images) -> None:
        self.title = title
        self.price = price
        self.about = about
        self.link = link
        self.images = images

    def get_field_lst(self):
        return [self.title, self.price, self.about, self.link, self.images]

    def __repr__(self) -> str:
        return f'Product{{ title={self.title}, link={self.link} }}'
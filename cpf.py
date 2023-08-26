
class Cpf:
    def __init__(self, documento):
        self.cpf = self.is_valid(str(documento))

    def __str__(self):
        return self.format()

    def is_valid(self, documento):
        if len(documento) == 11:
            return documento
        else:
            raise ValueError('Cpf invalido!')

    def format(self):
        slice_one = self.cpf[:3]
        slice_two = self.cpf[3:6]
        slice_three = self.cpf[6:9]
        slice_for = self.cpf[9:]
        return '{}.{}.{}-{}'.format(slice_one, slice_two, slice_three, slice_for)

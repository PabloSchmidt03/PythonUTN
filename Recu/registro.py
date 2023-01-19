class Cliente():
    def __init__(self, cod, tipoc, tipop, monto):
        self.codigo = cod
        self.tipo_cliente = tipoc
        self.tipo_pago = tipop
        self.monto = monto

    def __str__(self):
        r = "Codigo: {} - Tipo cliente: {} - Tipo pago: {} - Monto: {}"
        return r.format(self.codigo, self.tipo_cliente, self.tipo_pago, self.monto)
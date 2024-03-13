def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto de descuento aplicando el porcentaje al monto total de la compra.

    Args:
    - monto_total (float): El monto total de la compra.
    - porcentaje_descuento (float, optional): El porcentaje de descuento a aplicar. Por defecto es 10.

    Returns:
    - float: El monto de descuento.
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def main():
    # Llamada a la función con solo el monto total de la compra
    monto_total1 = float(input("Ingrese el monto total de la compra 1: "))
    descuento1 = calcular_descuento(monto_total1)
    monto_final1 = monto_total1 - descuento1
    print("Monto de descuento 1:", descuento1)
    print("Monto final a pagar después del descuento 1:", monto_final1)

    # Llamada a la función con el monto total de la compra y el porcentaje de descuento
    monto_total2 = float(input("Ingrese el monto total de la compra 2: "))
    porcentaje_descuento2 = float(input("Ingrese el porcentaje de descuento para la compra 2: "))
    descuento2 = calcular_descuento(monto_total2, porcentaje_descuento2)
    monto_final2 = monto_total2 - descuento2
    print("Monto de descuento 2:", descuento2)
    print("Monto final a pagar después del descuento 2:", monto_final2)


if __name__ == "__main__":
    main()



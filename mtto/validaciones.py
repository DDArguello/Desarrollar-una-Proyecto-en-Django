from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_even(value):
    x=str(value)
    if len(x)!=10:
        raise ValidationError(
             "Cédula Incorrecta"
        )

def validate_nombre(value):
    for i in value:
        x=(i.isdigit())
        if x==True:
            raise ValidationError(
                "Nombre Incorrecto"
            )

def validate_cardepa(value):
    for i in value:
        x=(i.isdigit())
        if x==True:
            raise ValidationError(
                "Ingrese solo letras"
            )

        
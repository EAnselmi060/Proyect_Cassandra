#from django.db import models

# Create your models here.

from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine import columns

class VentaMensual(DjangoCassandraModel):
    id_venta = columns.Integer(primary_key=True)
    fecha = columns.Date(primary_key=True)
    unidades = columns.Integer()

class PromedioCredito(DjangoCassandraModel):
    id_p_credito = columns.Integer(primary_key=True)
    sexo = columns.Text(primary_key=True)
    edad = columns.Integer(primary_key=True)
    monto = columns.Decimal()

class ProductoEdadSexo(DjangoCassandraModel):
    id_compra = columns.Integer(primary_key=True)
    edad = columns.Integer(primary_key=True)
    sexo = columns.Text(primary_key=True)
    cantidad = columns.Integer()
    nom_producto = columns.Text()

class ProductoVendidoPromo(DjangoCassandraModel):
    id_venta = columns.Integer(primary_key=True)
    promocion = columns.Boolean(primary_key=True)
    cantidad = columns.Integer(primary_key=True)
    producto = columns.Text()

class CreditoMes(DjangoCassandraModel):
    id_credito = columns.Integer(primary_key=True)
    fecha = columns.Date(primary_key=True)
    monto = columns.Decimal()

class EdadPromedioCompra(DjangoCassandraModel):
    id_compra = columns.Integer(primary_key=True)
    fecha = columns.Text(primary_key=True)
    edad_comprador = columns.Integer()

class ComparacionHM(DjangoCassandraModel):
    id_ventas = columns.Integer(primary_key=True)
    cantidad = columns.Integer(primary_key=True)
    sexo = columns.Text(primary_key=True)

class ProductoCompradoEdad(DjangoCassandraModel):
    id_venta = columns.Integer(primary_key=True)
    cantidad = columns.Integer(primary_key=True)
    edad = columns.Integer(primary_key=True)

class MontoTotalEdad(DjangoCassandraModel):
    id_venta = columns.Integer(primary_key=True)
    edad = columns.Integer(primary_key=True)
    monto = columns.Decimal()

class VentasAcumProduc(DjangoCassandraModel):
    id_venta = columns.Integer(primary_key=True)
    cantidad = columns.Integer(primary_key=True)
    producto = columns.Text()

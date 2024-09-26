print(" examen Alexis Fabian Jimenez Jimenez 22308051281213")

class promociones1213:
    Id_productos1213=0
    descripcion1213=""
    fecha_inicio1213=""
    fecha_fin1213=""
    codigo_promocion1213=0
    producto_ap1213=""
    zona_ap1213=""

    def mostrar_datos1213(self):
        print(f"id:{self.Id_productos1213}, descripcion{self.descripcion1213}, fecha de inicio {fecha_inicio1213}, fecha de fin {fecha_fin1213}, codigo promocional {codigo_promocion1213}, marca del producto {producto_ap1213}, zona de aplicar {zona_ap1213}")

    def listar_promociones_graficas1213(self):
        li_promocion=["50% para descuento en la 3060","25% para descuento en la 3080","15% para descuento en la 2070","5% para descuento en la 4070"]
        print(li_promocion)
        for x in li_promocion:
            print(x)

    def tupla_promociones_marcas1213(self):
        tu_marcas=("50% menos en la marca Nvidia", "10% menos en la marca Asus", "20% menos en la marca hypeX","30% menos en la marca ryzen")
        print(tu_marcas)
        for x in tu_marcas:
            print(x)

    def set_promociones_procesadores1213(self):
        set_procesadores={"50% menos en i3", "10% menos en 15 14600f", "20% menos en i7 13900k","30% menos en Ryzen 9 5600x"}
        print(set_procesadores)
        for x in set_procesadores:
            print(x)
    
    def diccionario_promociones_teclados1213(self):
        dicc_teclados={
            "900w 80 plus gold":"20% en descuento",
            "900w 80 plus bronce":"40% en descuento",
            "750w 80 plus platino":"20% en descuento",
            "500w 80 plus bronce":"60% en descuento"
        }
        print(dicc_teclados)
        for x,y in dicc_teclados.items():
            print(x,y)


    def alta1213():
        print("la operacion se ha realizado correctamente")
    def baja1213():
        print("se ha borrado correctamente")

#objeto
obj=promociones1213()
#asignar datos
Id_productos1213=3283862832
descripcion1213="descuento en toda la marca msi"
fecha_inicio1213="12/09/2024"
fecha_fin1213="22/09/2024"
codigo_promocion1213=47834834
producto_ap1213="MSI"
zona_ap1213="Mexico"
#mostrar datos
obj.mostrar_datos1213()
print("lista")
obj.listar_promociones_graficas1213()
print("tupla")
obj.tupla_promociones_marcas1213()
print("set")
obj.set_promociones_procesadores1213()
print("diccionario")
obj.diccionario_promociones_teclados1213()




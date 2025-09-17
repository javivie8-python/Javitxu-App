from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None  # Aquí guardaremos el mensaje final
    if request.method == "POST":
        # 1️⃣ Recoger los datos del formulario
        nombre = request.form["nombre"]
        distancia_km = int(request.form["distancia_km"])
        distancia_metros = int(request.form["distancia_metros"])
        tiempo_horas = int(request.form["tiempo_horas"])
        tiempo_min = int(request.form["tiempo_min"])
        tiempo_seg = int(request.form["tiempo_seg"])

        # 2️⃣ Tu lógica de cálculo de ritmo
        tiempo_total_seg = tiempo_horas*3600 + tiempo_min*60 + tiempo_seg
        tiempo_total_min = tiempo_total_seg / 60
        distancia_total_km = distancia_km + (distancia_metros / 1000)
        ritmo = tiempo_total_min / distancia_total_km
        minutos = int(ritmo)
        segundos = round((ritmo - minutos)*60, 2)

        # 3️⃣ Crear el mensaje final
        if minutos >= 5:
            mensaje = f"Estas muy flojo, espabila {nombre}!"
        else:
            mensaje = f"Enhorabuena, sigue así {nombre}!!!"

        resultado = f"Tu ritmo es {minutos} min {segundos} seg por km.<br>{mensaje}<br>Made by Javierito"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)

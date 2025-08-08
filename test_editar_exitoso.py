from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from datetime import datetime

BASE_LOGIN_URL = "http://localhost:8000/login.html"

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

try:
    driver.get(BASE_LOGIN_URL)
    time.sleep(1)

    driver.find_element(By.ID, "username").send_keys("Luis Armanando Martinez")

    driver.find_element(By.ID, "password").send_keys("Luis1234")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(2)

    if "compras.html" not in driver.current_url:
        raise Exception("Error en prueba editar")

    producto_original = "Lasagna"
    item_input = driver.find_element(By.ID, "itemInput")
    item_input.send_keys(producto_original)
    driver.find_element(By.CSS_SELECTOR, "#itemForm button[type='submit']").click()

    time.sleep(1)

    editar_btn = driver.find_element(By.CSS_SELECTOR, "#itemList li:first-child button.btn-primary")
    editar_btn.click()

    time.sleep(1)

    edit_input = driver.find_element(By.ID, "edititemInput")
    edit_input.clear()

    producto_editada = "pizza de peperoni con queso"
    edit_input.send_keys(producto_editada)

    guardar_btn = driver.find_element(By.ID, "saveEditBtn")
    guardar_btn.click()

    time.sleep(1)

    productos = driver.find_elements(By.CSS_SELECTOR, "#itemList li span")
    textos = [t.text for t in productos]

    if producto_editada in textos and producto_original not in textos:
        resultado = "editar producto: PASÓ"
        estado = "PASÓ"
        color = "green"

    else:
        resultado = "editar producto: FALLÓ"
        estado = "FALLÓ"
        color = "red"


    screenshot_path = f"screenshots/editar.png"
    driver.save_screenshot(screenshot_path)

    html_content = f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Reporte - Editar producto</title>
    </head>
    <body>
        <h1 style="color:{color};">Resultado: {estado}</h1>
        <p>{resultado}</p>
        <h2>Captura de pantalla:</h2>
        <img src="{screenshot_path}" alt="Captura prueba editar producto" width="500">
    </body>
    </html>
    """

    with open("reporte_editar.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print(resultado)

except Exception as e:
    print("Error editar:", e)

finally:
    time.sleep(3)

    driver.quit()

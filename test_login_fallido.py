from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)


BASE_URL = "file://C:\\Users\\luisa\\OneDrive\\Documentos\\Escritorio\\compras-crud-P3\\login.html"


if not os.path.exists("screenshots"):
    os.makedirs("screenshots")
driver.get(BASE_URL)

driver.find_element(By.ID, "username").send_keys("Luis Armanando Martinez")

driver.find_element(By.ID, "password").send_keys("")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(1)

if "compras.html" in driver.current_url:
    resultado = "login: PASÓ"
    estado = "PASÓ"
    color = "green"

else:
    resultado = "login: FALLÓ"
    estado = "FALLÓ"
    color = "red"

screenshot_path = "screenshots/login.png"
driver.save_screenshot(screenshot_path)



html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Reporte de Prueba - Login</title>
</head>
<body>
    <h1 style="color:{color};">Resultado de la prueba de login: {estado}</h1>
    <p>{resultado}</p>
    <h2>Captura de pantalla:</h2>
    <img src="{screenshot_path}" alt="Captura de prueba" width="500">
</body>
</html>
"""

with open("reporte_login.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print(resultado)

driver.quit()

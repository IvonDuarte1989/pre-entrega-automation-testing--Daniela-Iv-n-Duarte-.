from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_products(login_in_driver):
    try:
        driver = login_in_driver

        # Se agrega producto al carrito de compras.
        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        itemName = products[0].find_element(By.CLASS_NAME, "inventory_item_name ").text
        firstAddToCartButton = products[0].find_elements(By.CSS_SELECTOR, "button.btn.btn_primary.btn_small.btn_inventory")
        driver.execute_script("arguments[0].click();", firstAddToCartButton[0])
        time.sleep(2)
        shoppingCartContainer = driver.find_elements(By.ID, "shopping_cart_container")
        cartBadge = shoppingCartContainer[0].find_element(By.CLASS_NAME, "shopping_cart_badge")
        assert cartBadge.text == "1", "El carrito de compras no actualiza su número correctamente."

        # Comprobación cambio de texto de botón de 'Add to cart' a 'Remove'.
        firstAddToCartButtonWithRemoveText = products[0].find_elements(By.CSS_SELECTOR, "button.btn.btn_secondary.btn_small.btn_inventory")
        assert firstAddToCartButtonWithRemoveText[0].text == "Remove", "El texto del botón agregar al carro no se actualiza."

        # Comprobación de correcta redirección a página del carrito.
        driver.execute_script("arguments[0].click();", shoppingCartContainer[0].find_element(By.TAG_NAME, "a"))
        assert "/cart.html" in driver.current_url, "No se redirgió al carrito de compras."

        # Comprobación que el producto agregado sea el mismo que se seleccionó.
        cartList = driver.find_element(By.CLASS_NAME, "cart_list")
        firstCartItem = cartList.find_elements(By.CLASS_NAME, "cart_item")[0]
        cartItemName = firstCartItem.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert itemName == cartItemName, "El producto del carrito no corresponde con el seleccionado"
        time.sleep(2)
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()
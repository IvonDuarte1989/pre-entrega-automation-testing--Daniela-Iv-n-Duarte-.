from selenium.webdriver.common.by import By
from selenium import webdriver

def test_inventory(login_in_driver):
    try:
        driver = login_in_driver

        assert driver.title == "Swag Labs"

        products = driver.find_elements(By.CLASS_NAME, "inventory_item")
        assert len(products) > 0, "No hay productos visibles en la pagina"

        firstInventoryPrice = products[0].find_elements(By.CLASS_NAME, "inventory_item_price")

        assert len(firstInventoryPrice) > 0, "No existen los precios de los items."

        firstAddToCartButton = products[0].find_elements(By.CSS_SELECTOR, "button.btn.btn_primary.btn_small.btn_inventory")

        assert len(firstAddToCartButton) > 0, "No existen los botones para agregar items al carro de compras."

        assert shoppingCartExists(driver) == True, "El carrito de compras no existe"

        assert filtersExist(driver) == True, "No hay filtros de búsqueda"

        assert menuButtonExists(driver) == True, "El botón de menú no existe"
    except Exception as e:
        print(f"Error en test_inventory: {e}")
        raise
    finally:
        driver.quit()

def shoppingCartExists(driver):
    cartExists = True
    shoppingCartContainer = driver.find_elements(By.ID, "shopping_cart_container")
    if len(shoppingCartContainer) > 0:
        shoppingLink = shoppingCartContainer[0].find_elements(By.TAG_NAME, "a")
        cartExists = len(shoppingLink) > 0
    else:
        cartExists = False
    return cartExists

def filtersExist(driver):
    filtersExists = True
    filtersSelect = driver.find_elements(By.CLASS_NAME, "product_sort_container")
    if len(filtersSelect) > 0:
        filtersOptions = filtersSelect[0].find_elements(By.TAG_NAME, "option")
        filtersExists = len(filtersOptions) > 0
    else:
        filtersExists = False
    return filtersExists

def menuButtonExists(driver):
    menuButton = driver.find_elements(By.ID, "react-burger-menu-btn")
    return len(menuButton) > 0
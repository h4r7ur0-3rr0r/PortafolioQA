import pytest
from utils.driver_manager  import get_driver
from test.pages.home_page  import HomePage
from test.pages.search_page import SearchPage

@pytest.fixture(scope="function")
def setup(request):
    driver = get_driver()
    driver.get("https://mercadolibre.com/")

    def teardown():
        driver.quit()
    
    request.addfinalizer(teardown)
    return driver

def test_search_playstation_5(setup, request):
    driver = setup
    home_page = HomePage(driver)
    search_page = SearchPage(driver)
    home_page.select_country()
    home_page.search_for("Playstation 5")
    search_page.filter_by_new_condition()
    search_page.sort_by_higher_price()
    top_products = search_page.get_top_products(5)
    print("\nTop 5 productos de PlayStation 5:")
    for i, product in enumerate(top_products, 1):
        print(f"{i}. {product['name']} - {product['price']}")
    assert len(top_products) == 5, "No se encontraron 5 productos"
    

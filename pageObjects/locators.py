from selenium.webdriver.common.by import By


class SauceLocators:
    ##Login Page
    username = (By.XPATH, "//input[@id='user-name']")
    password = (By.XPATH, "//input[@id='password']")
    login_btn = (By.XPATH, "//input[@id='login-button']")
    logerror_msg = (By.XPATH, "//h3[@data-test='error']")

    ##Product Page
    item_name = (By.CLASS_NAME, "inventory_item_name")
    addtocart_btn = (By.CLASS_NAME, "btn_inventory")
    sort_btn = (By.XPATH, "//select[@class='product_sort_container']")
    lohi_opt = (By.XPATH, "//option[@value='lohi']")
    hilo_opt = (By.XPATH, "//option[@value='hilo']")
    item_price = (By.CLASS_NAME, "inventory_item_price")
    cart_btn = (By.XPATH, "	//a[@class='shopping_cart_link']")
    items_in_cart = (By.XPATH, "//span[@class='shopping_cart_badge']")
    menu_btn = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    reset_app_menu = (By.XPATH, "//a[@id='reset_sidebar_link']")
    logout_menu = (By.XPATH, "//a[@id='logout_sidebar_link']")
    about_menu = (By.XPATH, "//a[@id='about_sidebar_link']")
    twitter_btn = (By.XPATH, "//a[contains(text(),'Twitter')]")
    fb_btn = (By.XPATH, "//a[contains(text(),'Facebook')]")
    linkedin_btn = (By.XPATH, "//a[contains(text(),'LinkedIn')]")

    ##Checkout Page
    checkout_btn = (By.XPATH, "//button[@id='checkout']")
    cart_item = (By.CLASS_NAME, "inventory_item_name")

    ##Delivery Page
    first_name = (By.XPATH, "//input[@id='first-name']")
    last_name = (By.XPATH, "//input[@id='last-name']")
    postal_code = (By.XPATH, "//input[@id='postal-code']")
    continue_btn = (By.XPATH, "//input[@id='continue']")

    ##Overview Page
    finish_btn = (By.XPATH, "//button[@id='finish']")

    ##Complete Page
    dispatched_text = (By.XPATH, "//div[@class='complete-text']")

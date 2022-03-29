from urllib.parse import urlparse


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.labirint.ru/"
        self.driver.implicitly_wait(5)

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def get_url(self):
        url = urlparse(self.driver.current_url)
        return url.netloc

    def get_link_query(self):
        url = urlparse(self.driver.current_url)
        return url.query

    def get_current_url(self):
        return self.driver.current_url

    def visit(self):
        return self.driver.get(self.url)











    '''def scroll_down(self, offset):
        if offset:
            self.driver.execute_script(f'window.scrollBy(0, {offset});')
        else:
            self.driver.execute_script(f'window.scrollBy(0, document.body.scrollHeight);')


    def get_page(self):
        return self.driver.find_element_by_xpath("//a[@class="b-header-b-menu-e-text" and contains(text(), "Книги")]")


    # нахождение элемента и нажатие на элемент
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    # для отправки ключей в поле ввода
    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)'''






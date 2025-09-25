import pytest
from .base import AuthorsBaseTest
from django.contrib.auth.models import User
from selenium.webdriver.common.by import By

from django.urls import reverse

@pytest.mark.functional_test
class AuthorsLoginTest(AuthorsBaseTest):
    def test_user_valid_data_can_login_successfully(self):
        string_password = "pass"
        user = User.objects.create_user(username="my_user", password=string_password)

        #Usuario abre a página de login
        self.browser.get(self.live_server_url + reverse("authors:login"))

        #Usuario vê o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, "main-form")
        username_field = self.get_by_placeholder(form, "Type your username")
        password_field = self.get_by_placeholder(form, "Type your password")

        #Usuario digita seu usuario e senha
        username_field.send_keys(user.username)
        password_field.send_keys(string_password)

        form.submit()

        #Usuario vê a mensagem de login com sucesso e seu nome
        self.assertIn(
            f"Your are logged in with {user.username}.",
            self.browser.find_element(By.TAG_NAME, "body").text
        )

    def test_login_create_raises_404_if_not_POST_method(self):
        self.browser.get(self.live_server_url + reverse("authors:login_create"))

        self.assertIn(
            "Not Found",
            self.browser.find_element(By.TAG_NAME, "body").text
        )

    def test_form_login_is_invalid(self):
        #Usuario abre a página de login
        self.browser.get(
            self.live_server_url + reverse("authors:login")
        )

        #Usuario vê o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, "main-form")

        #E tenta enviar valores vazios
        username = self.get_by_placeholder(form, "Type your username")
        password = self.get_by_placeholder(form, "Type your password")
        username.send_keys(" ")
        password.send_keys(" ")

        #Envia o formulario
        form.submit()

        # Vê uma menssagem de erro na tela
        self.assertIn(
            "Invalid username or password",
            self.browser.find_element(By.TAG_NAME, "body").text
        )

    def test_form_login_invalid_credentials(self):
        #Usuario abre a página de login
        self.browser.get(
            self.live_server_url + reverse("authors:login")
        )

        #Usuario vê o formulario de login
        form = self.browser.find_element(By.CLASS_NAME, "main-form")

        #E tenta enviar valores com dados que não correspondem
        username = self.get_by_placeholder(form, "Type your username")
        password = self.get_by_placeholder(form, "Type your password")
        username.send_keys("invalid_user")
        password.send_keys("invalid_password")

        #Envia o formulario
        form.submit()

        # Vê uma menssagem de erro na tela
        self.assertIn(
            "Invalid credentials",
            self.browser.find_element(By.TAG_NAME, "body").text
        )
from porteiros.tests.test_base import BaseTest
from usuarios.models import Usuario

from builtins import TypeError

from django.core.exceptions import ValidationError


class UsuariosModelsTest(BaseTest):
    # MODEL Usuario
    def test_usuarios_model_usuario_string_representation(self):
        usuario = self.make_usuario()
        self.assertEqual(
            str(usuario), usuario.email
        )

    def test_usuarios_model_usuario_email_field_max_length_lt_194(self):
        usuario = self.make_usuario()
        usuario.email = ('a' * 194) + '@email.com'

        with self.assertRaises(ValidationError):
            usuario.full_clean()

    # MODEL UsuarioManeger
    def test_usuarios_model_usuario_manager_create_user_without_password(self):
        user = Usuario.objects.create_user('normal@user.com')
        # testando se criou com email correto
        self.assertEqual(
            user.email, 'normal@user.com'
        )

        # testando se esta ativo
        self.assertTrue(user.is_active)
        # testando se é false para superuser e staff
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_usuarios_model_usuario_manager_create_user_with_password(self):
        user = Usuario.objects.create_user('normal@user.com', '12345')
        # testando se criou com email correto
        self.assertEqual(
            user.email, 'normal@user.com'
        )
        # verificando se criou a senha correta e criptografou
        self.assertTrue(user.check_password('12345'))

    def test_usuarios_model_usuario_manager_create_user_without_parameters(self):  # noqa: E501
        with self.assertRaises(TypeError):
            Usuario.objects.create_user()

    def test_usuarios_model_usuario_manager_create_superuser(self):
        user = Usuario.objects.create_superuser('normal@user.com', '12345')
        # testando se criou com email correto
        self.assertEqual(
            user.email, 'normal@user.com'
        )

        # testando se esta ativo
        self.assertTrue(user.is_active)
        # testando se é true para superuser e staff
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_usuarios_model_usuario_manager_create_superuser_without_password_raises_type_error(self):  # noqa: E501
        with self.assertRaises(TypeError):
            Usuario.objects.create_superuser('normal@user.com')

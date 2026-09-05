import os
import tempfile
import unittest

import progress


class TestLoadEnv(unittest.TestCase):

    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def _write_env(self, content):
        path = os.path.join(self.tmp, ".env")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def test_lee_cookie_simple(self):
        self._write_env("THM_CONNECT_SID=abc123\n")
        env = progress._load_env(self.tmp)
        self.assertEqual(env.get("THM_CONNECT_SID"), "abc123")

    def test_quita_comillas(self):
        self._write_env('THM_CONNECT_SID="abc123"\n')
        env = progress._load_env(self.tmp)
        self.assertEqual(env.get("THM_CONNECT_SID"), "abc123")

    def test_quita_comillas_simples(self):
        self._write_env("THM_CONNECT_SID='abc123'\n")
        env = progress._load_env(self.tmp)
        self.assertEqual(env.get("THM_CONNECT_SID"), "abc123")

    def test_ignora_comentarios_y_vacios(self):
        self._write_env("# comentario\n\nOTRA=valor\n")
        env = progress._load_env(self.tmp)
        self.assertNotIn("THM_CONNECT_SID", env)
        self.assertEqual(env.get("OTRA"), "valor")

    def test_ignora_lineas_sin_igual(self):
        self._write_env("SOLO_TEXTO\n")
        env = progress._load_env(self.tmp)
        self.assertEqual(env, {})

    def test_sin_archivo_devuelve_vacio(self):
        env = progress._load_env(self.tmp)
        self.assertEqual(env, {})

    def test_cookie_real_cargada(self):
        env = progress._load_env(progress.BASE_DIR)
        self.assertTrue(env.get("THM_CONNECT_SID"))

    def test_session_cookie_expuesta_al_modulo(self):
        env = progress._load_env(progress.BASE_DIR)
        self.assertEqual(progress.SESSION_COOKIE, env.get("THM_CONNECT_SID", ""))


if __name__ == "__main__":
    unittest.main()
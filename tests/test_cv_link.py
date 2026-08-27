import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CV_PATH = ROOT / "assets" / "cv" / "Qi_Wang_CV.pdf"


class CvLinkTest(unittest.TestCase):
    def test_sidebar_links_to_valid_cv_pdf(self):
        config = (ROOT / "_config.yml").read_text(encoding="utf-8")
        gitignore = (ROOT / ".gitignore").read_text(encoding="utf-8")
        layout = (ROOT / "_layouts" / "homepage.html").read_text(encoding="utf-8")

        self.assertIn("cv_link: /assets/cv/Qi_Wang_CV.pdf", config)
        self.assertNotIn('- "*.pdf"', config)
        self.assertIn("!assets/cv/Qi_Wang_CV.pdf", gitignore)
        self.assertIn("{% if site.cv_link %}", layout)
        self.assertIn("{{ site.cv_link | relative_url }}", layout)
        self.assertIn('aria-label="Curriculum Vitae (PDF)"', layout)
        self.assertIn('class="ai ai-cv"', layout)
        self.assertTrue(CV_PATH.is_file())
        self.assertTrue(CV_PATH.read_bytes().startswith(b"%PDF-"))


if __name__ == "__main__":
    unittest.main()

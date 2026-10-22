"""WCAG contrast check for the per-app legal pages: every text/background pair (body, muted, link/nav text,
on the page and on the tinted summary panel, light and dark) must reach 4.5:1. Prints the table, exits 1 on a
failure. Run from anywhere: python3 tools/check_contrast.py"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_legal_apps import all_apps, print_contrast
sys.exit(0 if print_contrast(all_apps()) else 1)

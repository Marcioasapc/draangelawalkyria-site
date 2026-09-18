#!/usr/bin/env python3
"""Servidor local que imita as clean URLs da Vercel (/coluna -> coluna.html, /blog/x -> blog/x.html)."""
import http.server, os, sys
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765
ROOT = os.path.dirname(os.path.abspath(__file__))
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=ROOT, **k)
    def translate_path(self, path):
        p = path.split('?')[0].rstrip('/')
        if p == '': return os.path.join(ROOT, 'index.html')
        full = os.path.join(ROOT, p.lstrip('/'))
        if os.path.isdir(full): return os.path.join(full, 'index.html')
        if not os.path.exists(full) and os.path.exists(full + '.html'): return full + '.html'
        return super().translate_path(path)
http.server.ThreadingHTTPServer(('127.0.0.1', PORT), H).serve_forever()

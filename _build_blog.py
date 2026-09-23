#!/usr/bin/env python3
"""Gera blog/index.html e os artigos a partir de _header.html/_footer.html.
Para criar um artigo novo: adicione um dicionário em POSTS e rode `python3 _build_blog.py`."""
import os, html, json

ROOT = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_header.html'), encoding='utf-8').read()
FOOTER = open(os.path.join(ROOT, '_footer.html'), encoding='utf-8').read()
SITE = 'https://draangelawalkyria.com.br'

POSTS = []  # sem artigos por enquanto (pedido do Marcio, 22/09/2026). Rascunhos guardados em _rascunhos_blog.py

DISCLAIMER = '<p class="post-disclaimer">Este conteúdo é informativo e não substitui avaliação presencial. Não faço diagnóstico por texto ou vídeo. Em caso de dor intensa, perda de força ou alterações neurológicas, procure atendimento médico.</p>'

def head(title, desc, url, extra=''):
    return f'''<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:url" content="{url}">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(desc)}">
  <meta property="og:image" content="{SITE}/assets/og-image.jpg">
  <meta property="og:locale" content="pt_BR">
  <link rel="canonical" href="{url}">
  <link rel="icon" type="image/png" href="/assets/favicon.png">
  <link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
  {extra}
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="/styles.css?v=20260923a">
</head>
<body>
'''

# ---- posts
for p in POSTS:
    url = f"{SITE}/blog/{p['slug']}"
    schema = f'''<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": {json.dumps(p['title'], ensure_ascii=False)},
    "description": {json.dumps(p['lead'], ensure_ascii=False)},
    "datePublished": "{p['date']}",
    "dateModified": "{p['date']}",
    "author": {{ "@type": "Person", "name": "Dra. Angela Walkyria Cavalcante", "jobTitle": "Fisioterapeuta", "url": "{SITE}/" }},
    "publisher": {{ "@type": "Organization", "name": "Dra. Angela Walkyria - Fisioterapia", "logo": {{ "@type": "ImageObject", "url": "{SITE}/assets/apple-touch-icon.png" }} }},
    "image": "{SITE}/assets/og-image.jpg",
    "mainEntityOfPage": "{url}"
  }}
  </script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {{ "@type": "ListItem", "position": 1, "name": "Início", "item": "{SITE}/" }},
      {{ "@type": "ListItem", "position": 2, "name": "Blog", "item": "{SITE}/blog" }},
      {{ "@type": "ListItem", "position": 3, "name": "{html.escape(p['title'])}", "item": "{url}" }}
    ]
  }}
  </script>'''
    others = [o for o in POSTS if o['slug'] != p['slug']]
    nav = ' · '.join(f'<a href="/blog/{o["slug"]}">{html.escape(o["title"])}</a>' for o in others)
    page = head(f"{p['title']} | Blog Dra. Angela Walkyria", p['lead'], url, schema) + HEADER + f'''
  <main class="post">
    <div class="container">
      <article>
        <header class="post-header">
          <div class="post-meta">{html.escape(p['tag'])} · {p['date_br']} · leitura de {p['read']}</div>
          <h1>{html.escape(p['title'])}</h1>
          <p class="lead">{html.escape(p['lead'])}</p>
          <div class="post-meta" style="margin-top:18px;margin-bottom:0">Por Dra. Angela Walkyria Cavalcante · Fisioterapeuta · CREFITO-3 128782-F</div>
        </header>
        <div class="post-body">
{p['body']}
        </div>
        <div class="post-cta">
          <h2>Quer saber o que está causando a sua dor?</h2>
          <p>Agende uma avaliação no consultório em Alphaville. Atendimento particular, individual e com hora marcada.</p>
          <a href="https://wa.me/5511971762434?text=Ol%C3%A1%2C%20li%20o%20artigo%20no%20site%20e%20quero%20agendar%20uma%20avalia%C3%A7%C3%A3o%20com%20a%20Dra.%20Angela" target="_blank" rel="noopener" class="btn btn-white">Agendar pelo WhatsApp</a>
        </div>
        {DISCLAIMER}
        <p class="post-nav">Leia também: {nav} · <a href="/blog">Todos os artigos</a></p>
      </article>
    </div>
  </main>
''' + FOOTER
    with open(os.path.join(ROOT, 'blog', p['slug'] + '.html'), 'w', encoding='utf-8') as f:
        f.write(page)
    print('ok', p['slug'])

# ---- index
cards = '\n'.join(f'''        <a href="/blog/{p['slug']}" class="post-card">
          <span class="post-tag">{html.escape(p['tag'])}</span>
          <h2>{html.escape(p['title'])}</h2>
          <p>{html.escape(p['lead'])}</p>
          <span class="post-meta">{p['date_br']} · {p['read']}</span>
        </a>''' for p in POSTS)
index = head('Blog | Dra. Angela Walkyria · Coluna, escoliose e dor', 'Artigos da Dra. Angela Walkyria sobre dor na coluna, hérnia de disco, ciático, escoliose e postura. Conteúdo de especialista, sem diquinhas.', f'{SITE}/blog') + HEADER + f'''
  <section class="blog-hero">
    <div class="container">
      <span class="eyebrow">Blog</span>
      <h1>Coluna, escoliose e dor, explicadas por quem trata todos os dias.</h1>
      <p>Aqui eu escrevo o que explico no consultório: por que a dor aparece, o que os exames mostram (e o que não mostram) e como voltar a se mover sem medo. Conteúdo de especialista, sem diquinhas.</p>
    </div>
  </section>
  <section class="blog-list">
    <div class="container">
      {'<div class="blog-grid">' + chr(10) + cards + chr(10) + '</div>' if POSTS else '<div class="callout" style="max-width:720px;margin:0 auto;text-align:center"><h3>Os primeiros artigos estão sendo escritos.</h3><p>Enquanto isso, conheça os tratamentos de <a href="/coluna" style="color:var(--coral-deep);text-decoration:underline">coluna</a>, <a href="/escoliose" style="color:var(--coral-deep);text-decoration:underline">escoliose</a> e <a href="/massagem" style="color:var(--coral-deep);text-decoration:underline">massagem</a>, ou siga a Dra. Angela no <a href="https://www.instagram.com/dra.angelawalkyria" target="_blank" rel="noopener" style="color:var(--coral-deep);text-decoration:underline">Instagram</a>.</p></div>'}
    </div>
  </section>
''' + FOOTER
with open(os.path.join(ROOT, 'blog', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index)
print('ok index')

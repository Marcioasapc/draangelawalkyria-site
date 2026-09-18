#!/usr/bin/env python3
"""Gera blog/index.html e os artigos a partir de _header.html/_footer.html.
Para criar um artigo novo: adicione um dicionário em POSTS e rode `python3 _build_blog.py`."""
import os, html, json

ROOT = os.path.dirname(os.path.abspath(__file__))
HEADER = open(os.path.join(ROOT, '_header.html'), encoding='utf-8').read()
FOOTER = open(os.path.join(ROOT, '_footer.html'), encoding='utf-8').read()
SITE = 'https://draangelawalkyria.com.br'

POSTS = [
  {
    'slug': 'hernia-de-disco-voce-nao-e-o-seu-exame',
    'tag': 'Coluna · Hérnia de disco',
    'title': 'Hérnia de disco: você não é o seu exame',
    'lead': 'Receber um laudo com a palavra "hérnia" assusta. Mas o que a ressonância mostra e o que você sente nem sempre são a mesma coisa. Entenda por que o exame não define o seu futuro.',
    'date': '2026-09-18', 'date_br': '18 de setembro de 2026', 'read': '5 min',
    'body': '''
<p>Quase toda semana entra no meu consultório alguém com a ressonância na mão e a mesma frase: "Doutora, eu tenho hérnia de disco." A pessoa fala como se fosse uma sentença. E eu entendo: o laudo vem cheio de termos difíceis, o médico às vezes recomenda repouso, e a dor está ali todos os dias.</p>
<p>Então deixa eu te contar algo que muda a forma de olhar pra esse exame.</p>

<h2>O que a ressonância mostra não é, necessariamente, o que dói</h2>
<p>Estudos com pessoas <strong>sem nenhuma dor nas costas</strong> encontram alterações de disco em uma parte enorme delas. Abaulamento, protrusão, degeneração: tudo isso aparece em gente que nunca sentiu nada.</p>
<div class="dado"><p><strong>Cerca de 80% das pessoas com 50 anos</strong> apresentam sinais de degeneração de disco no exame de imagem sem sentir dor alguma.</p></div>
<p>Isso significa que o disco alterado faz parte do envelhecimento normal da coluna, como o cabelo branco ou as rugas. Ele não é, sozinho, a explicação da sua dor. A dor tem a ver com a forma como a sua coluna se move, com a força que sustenta ela, com a rigidez, com a postura que você mantém por horas, com o quanto você anda ou deixa de andar.</p>
<p>Por isso eu repito pros meus pacientes: <strong>você não é o seu exame</strong>. O laudo é uma foto. Você é um filme.</p>

<h2>A hérnia pode diminuir com o tempo</h2>
<p>Outra coisa que pouca gente sabe: a hérnia de disco não é uma peça quebrada que fica ali pra sempre. O próprio corpo tem um mecanismo pra reabsorver o material que saiu do disco.</p>
<div class="dado"><p><strong>Até 93% de alguns tipos de hérnia de disco</strong> podem ser reabsorvidos pelo corpo ao longo do tempo, principalmente as maiores e as extrusas.</p></div>
<p>Quando o tratamento devolve movimento, força e circulação pra região, você cria as condições pra esse processo acontecer. Ficar parado faz o contrário.</p>

<h2>Repouso prolongado atrasa a recuperação</h2>
<p>Esse é o ponto que mais me incomoda. Muita gente ouve que precisa ficar semanas ou meses de repouso. Na fase aguda, um ou dois dias de descanso podem ser necessários. Mas <strong>repouso prolongado enfraquece a musculatura, aumenta a rigidez e piora o medo de se mexer</strong>, e o medo é um dos maiores fatores que mantêm a dor crônica.</p>
<p>A minha proposta é diferente: quando você está com dor, você não precisa apenas descansar. Você precisa de <strong>ritmo de movimento junto com o descanso</strong>, no nível certo pro seu caso, senão você para todo o seu avanço.</p>

<h2>O que eu faço na primeira consulta</h2>
<ul>
  <li><strong>Mapeamento Funcional:</strong> avalio como você se move, onde perde força, o que trava e o que dói de verdade, e comparo com o que o exame mostra.</li>
  <li><strong>Intervenção no mesmo dia:</strong> técnicas manuais e mobilizações pra aliviar a dor já na primeira sessão.</li>
  <li><strong>Plano sob medida:</strong> exercícios específicos pro seu caso, sem tabela genérica, e adaptação do seu treino ou esporte em vez de proibição.</li>
</ul>
<p>Hérnia de disco tem tratamento, e na maioria dos casos ele não passa por cirurgia nem por remédio todo dia. Passa por entender a causa e devolver movimento com segurança.</p>
'''
  },
  {
    'slug': 'dor-ciatica-repouso-nao-resolve',
    'tag': 'Coluna · Ciático',
    'title': 'Dor ciática: por que descansar não resolve',
    'lead': 'Aquela dor que desce da lombar pela perna tem nome, tem causa e tem tratamento. O que ela não tem é solução na cama.',
    'date': '2026-09-18', 'date_br': '18 de setembro de 2026', 'read': '4 min',
    'body': '''
<p>A dor ciática é uma das queixas mais comuns que recebo em Alphaville. Começa na lombar ou no glúteo e desce pela parte de trás da coxa, às vezes até o pé. Pode vir com formigamento, queimação ou sensação de fraqueza na perna.</p>
<p>O nome vem do nervo ciático, o maior do corpo, que sai da coluna lombar e percorre toda a perna. Quando alguma estrutura irrita ou comprime esse nervo (um disco, uma articulação inflamada, um músculo muito tenso), ele avisa com dor no trajeto todo.</p>

<h2>A boa notícia</h2>
<div class="dado"><p><strong>Cerca de 70% das dores ciáticas melhoram em poucas semanas</strong> com o tratamento adequado. A maioria não precisa de cirurgia.</p></div>
<p>O detalhe está em "tratamento adequado". Tomar anti-inflamatório e deitar não é tratamento: é adiamento. A dor some por umas horas, volta, você toma de novo, e o ciclo continua. Enquanto isso, a causa segue intocada.</p>

<h2>Por que o repouso não resolve</h2>
<p>O nervo ciático precisa de movimento pra deslizar entre os tecidos, receber circulação e reduzir a sensibilidade. Quando você fica dias deitado:</p>
<ul>
  <li>a musculatura que estabiliza a lombar enfraquece;</li>
  <li>o quadril e a coluna ficam mais rígidos;</li>
  <li>o nervo fica mais sensível, não menos;</li>
  <li>e o medo de se mexer cresce, o que mantém a dor por mais tempo.</li>
</ul>
<p>Não estou dizendo pra você sair correndo com dor. Estou dizendo que existe um <strong>movimento certo, na dose certa</strong>, e é isso que a fisioterapia especializada em coluna faz: encontrar essa dose e conduzir você por ela com segurança.</p>

<h2>Sinais que pedem avaliação rápida</h2>
<p>Alguns sinais merecem atenção imediata: perda de força progressiva na perna, dormência na região íntima ou alteração no controle da urina ou do intestino. Nesses casos, procure atendimento médico de urgência. Fora isso, quanto antes você entender a causa, mais rápida é a recuperação.</p>

<h2>Como eu trato o ciático</h2>
<ol>
  <li><strong>Avaliação completa:</strong> testes que identificam de onde vem a irritação do nervo e o que piora ou alivia a dor.</li>
  <li><strong>Alívio já na primeira sessão:</strong> técnicas manuais, mobilizações neurais e liberação das estruturas que estão comprimindo o nervo.</li>
  <li><strong>Exercícios específicos:</strong> pra devolver força e mobilidade sem irritar o nervo.</li>
  <li><strong>Volta ao treino:</strong> se você corre, pedala, joga tênis ou faz musculação, a gente adapta em vez de proibir.</li>
</ol>
<p>Se a sua dor na perna já dura mais de alguns dias, não espere ela "passar sozinha". Ela pode até passar, mas tende a voltar mais forte se a causa continuar lá.</p>
'''
  },
  {
    'slug': 'sinais-de-escoliose-em-criancas',
    'tag': 'Escoliose · Crianças e adolescentes',
    'title': 'Sinais de escoliose em crianças: como observar em casa',
    'lead': 'A escoliose costuma aparecer na fase de crescimento e quase nunca dói no começo. Por isso os pais são os primeiros a perceber. Veja o que observar.',
    'date': '2026-09-18', 'date_br': '18 de setembro de 2026', 'read': '4 min',
    'body': '''
<p>Durante 13 anos no SUS, criei e coordenei o primeiro ambulatório especializado em escoliose de Santana de Parnaíba. Nesse tempo vi centenas de crianças e adolescentes, e aprendi uma coisa: <strong>quem descobre a escoliose cedo quase sempre é a mãe, o pai ou a avó</strong>, num momento comum do dia, vestindo a criança, na praia, na piscina.</p>
<p>A escoliose é uma curvatura lateral da coluna, geralmente acompanhada de rotação das vértebras. O tipo mais comum, a escoliose idiopática do adolescente, surge entre os 10 e os 16 anos, justamente quando o corpo cresce rápido. E no começo ela não dói. Por isso passa despercebida.</p>

<h2>O que observar em casa</h2>
<p>Peça pra criança ficar em pé, de costas pra você, descalça, com os pés juntos e os braços soltos ao lado do corpo. Observe:</p>
<ul>
  <li><strong>Ombros em alturas diferentes.</strong> Um ombro visivelmente mais alto que o outro.</li>
  <li><strong>Uma escápula (a "asinha" das costas) mais saltada</strong> que a outra.</li>
  <li><strong>Cintura assimétrica.</strong> Um lado mais "curvado pra dentro" e o outro mais reto.</li>
  <li><strong>Quadril desnivelado.</strong> A calça ou a saia parece cair torta.</li>
  <li><strong>Cabeça fora do centro</strong> em relação ao meio do quadril.</li>
</ul>
<p>Depois, peça pra criança se curvar pra frente, com as pernas esticadas e as mãos soltas em direção ao chão, como se fosse tocar os pés. Olhe as costas dela no nível dos seus olhos:</p>
<div class="dado"><p><strong>Se um lado das costas ficar mais alto que o outro</strong> (uma "costela saltada" ou uma elevação de um lado da lombar), esse é o sinal mais importante. Ele indica rotação da coluna e pede avaliação com um profissional.</p></div>

<h2>O que esses sinais não são</h2>
<p>Observar em casa não é diagnóstico. Uma assimetria pequena pode ser apenas postura e desaparece com reeducação. Só a avaliação presencial, e quando necessário a radiografia, confirma se existe escoliose e qual o grau da curvatura. O que você faz em casa é <strong>triagem</strong>: perceber cedo pra avaliar cedo.</p>

<h2>Por que agir cedo faz tanta diferença</h2>
<p>Enquanto a criança está crescendo, a curvatura pode progredir rápido. É exatamente nessa janela que o acompanhamento fisioterapêutico tem mais efeito: exercícios específicos, reeducação postural e, quando indicado pelo médico, o uso de colete. Agir cedo é o que evita que uma curva pequena vire uma curva grande, e que uma curva grande vire cirurgia.</p>
<p>E tem um detalhe que os pais sempre me perguntam: a criança pode continuar no esporte? Na grande maioria dos casos, sim. Movimento faz parte do tratamento.</p>

<h2>Quer um guia pra fazer essa avaliação com calma?</h2>
<p>Eu preparei um ebook gratuito, <strong>"Como avaliar a postura do seu filho em casa"</strong>, com o passo a passo e fotos de referência. <a href="https://chk.eduzz.com/39ZB5BEZ9E" target="_blank" rel="noopener">Baixe aqui</a>. E se você percebeu algum dos sinais acima, agende uma avaliação postural. Ela é rápida, não dói, e a criança costuma se divertir.</p>
'''
  },
]

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
  <link rel="stylesheet" href="/styles.css">
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
      <div class="blog-grid">
{cards}
      </div>
    </div>
  </section>
''' + FOOTER
with open(os.path.join(ROOT, 'blog', 'index.html'), 'w', encoding='utf-8') as f:
    f.write(index)
print('ok index')

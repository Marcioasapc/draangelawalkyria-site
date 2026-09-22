# Dra. Angela Walkyria — Site oficial (versão final 18/09/2026)

Site institucional + 3 landing pages + blog, HTML/CSS/JS puro, hospedado na Vercel (projeto `dra-angela-site`).

```
/                    Home (hero, sintomas, tratamentos, sobre, depoimentos, localização, CTA)
/coluna              LP Tratamento de Coluna
/escoliose           LP Escoliose (+ ebook)
/massagem            LP Massoterapia
/blog                Índice do blog
/blog/<slug>         Artigos (gerados por _build_blog.py)
```

## Como editar
- Textos: direto nos .html. Header e footer do blog ficam em `_header.html` / `_footer.html`.
- Blog: hoje só a página inicial ("em breve"). Para publicar artigos, copiar os rascunhos de `_rascunhos_blog.py` para `POSTS` em `_build_blog.py`, rodar `python3 _build_blog.py` e incluir as URLs no `sitemap.xml`.
- Pré-visualizar: `python3 serve.py 8765` e abrir http://127.0.0.1:8765
- Publicar: `python3 _deploy.py production` (usa o login do Vercel CLI deste Mac).

## Decisões aplicadas (reuniões 08/06 e 24/06 + WhatsApp)
- Paleta bege + azul-marinho aprovada; salmão só como detalhe (pedido da Angela).
- Fonte itálica fina removida (ela achou de difícil leitura) → Playfair Display peso 500.
- Seção "Por que escolher a Dra. Angela" removida; depoimentos reais do Google no lugar.
- Aviso "Atendimento particular · Não atendemos convênios" fixo no topo de todas as páginas + CTA final.
- Blog incluído (pedido dela em 17/09/2026).
- Fotos reais (recortes do site antigo), endereço e CREFITO reais, telefone WhatsApp (11) 97176-2434.

## Pendências
- [ ] Angela validar textos, artigos do blog e o nome "Mapeamento Funcional"/"Protocolo autoral".
- [ ] Confirmar horário de abertura (8h) e se atende sábado.
- [ ] Preços da massagem (hoje "Consultar valor").
- [ ] Fotos novas (ensaio) para substituir os recortes do site antigo, se ela quiser.
- [ ] GA4 / Meta Pixel / Clarity (IDs não definidos).
- [ ] Trocar DNS no registro.br para a Vercel e adicionar o domínio no projeto.
- [ ] Enviar sitemap no Search Console e atualizar o link no Google Meu Negócio.

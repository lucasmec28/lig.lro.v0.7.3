LRO Ligações 0.9.73 · candidata de contato direto e composição nominal

Extraia os quatro arquivos na mesma pasta:
app.py, codigo_lro.zip, requirements.txt e README.md.

Instale e execute:
python -m pip install -r requirements.txt
python -m streamlit run app.py

Candidata local de revisão. Não houve publicação online. As rotas e pacotes anteriores foram preservados.

NOVO: contato direto placa–chumbador, com EN 1993-1-8 complementar; arruela não soldada somente axial. Sem atrito, sem engaste fictício e sem deslocamento total de ELS inventado. Materiais/roscas/As reais, sem equivalência automática A36/EN. Fatores EN, NBR e ACI separados.

Seleção nas bases clássicas: Caminho resistente > Chumbadores > Contato direto placa–chumbador, EN complementar.
Seleção nervurada: Base nervurada · N + M + V · direta · revisão.

Resultado por família:
- I/H Tipo2 interno: fecha o escopo nominal P358 quando todos os consumidores, domínios, estados ACI e ELS atendem. hp é o trecho físico da alma, nunca L.
- I/H Tipo1 externo: fecha o escopo nominal P398 no envelope opcional da implementação e com todos os consumidores atendidos.
- Nas bases simples, qualquer tração de haste mantém pendente a verificação axial local da arruela/porca nesta composição. Não generalizar exemplos sem tração para casos com levantamento.
- Nervurada: fecha N+M+V no domínio publicado dos componentes normais e no envelope opcional de placa basal robusta, com verificação axial real da arruela. Mantém o benefício das nervuras em N/M e V integral na alma; não cria modelo membranar próprio. O exemplo ilustrativo de teste atende aos critérios delimitados; não corresponde a dados de uma obra do usuário.
- U de duas/quatro hastes: componentes diretos e ACI calculados, mas transferência completa da placa ainda parcial.

O envelope basal opcional é limite conservador do aplicativo, NÃO exigência normativa geral de base nervurada. Ele não converte capacidade de tração em capacidade de V; os consumidores de V são independentes. Fora do envelope é pendência de aplicabilidade, não falha física automática.

Somente graute integral curado, furos circulares normais/controlados e sem stand-off. Contornos de furos, filetes e arruelas devem caber fisicamente. Estados uniforme, dianteiro e oposto são conferidos; falhas e pendências são exportáveis em Word/JSON. Exemplos são demonstrações, não certificados de material ou de projeto.

Atendimento do escopo nominal delimitado não aprova fundação, bloco armado, solo, execução, estabilidade global nem rigidez rotacional. Consulte docs/DIRECT_ANCHOR_CANDIDATE.md dentro de codigo_lro.zip para requisitos e referências completos.

REVISÃO EDITORIAL: relatório Word resumido por família e critério, com IDs rastreáveis, fontes, solicitações e capacidades. Condições comuns e todas as falhas/pendências são preservadas. Indicadores internos de desenvolvimento não são apresentados como premissas físicas. O JSON completo permanece disponível como anexo eletrônico opcional. Cálculos resistentes e entradas da candidata anterior não foram alterados.

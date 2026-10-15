# LRO Ligações 0.9.59 — opção SCI para end plate de altura total

Use juntos os quatro arquivos: app.py, codigo_lro.zip, requirements.txt e README.md.

## O que mudou
Na família existente End plate rotulada, escolha o método SCI/Eurocode para cisalhamento vertical na alma de coluna. A opção possui entradas próprias, posição da primeira linha de parafusos, vistas frontal e lateral, projeto JSON próprio, resultados CSV e Word editável. O método NBR anterior e as outras famílias foram preservados.

## Domínio importante
Esta rotina segue SCI/BCSA P358 (2014), §4.7 e Eurocode com Anexos Nacionais UK. Não constitui fechamento da end plate genérica NBR N/V.
- Somente V vertical positivo de cálculo, sem N ou M aplicados, uma viga I laminada sem recortes na alma de coluna I contínua.
- Materiais realmente especificados S275/S355; chapa S275 de 10 ou 12 mm; parafusos M20 classe 8.8 e furos padrão de 22 mm. A confirmação do material inicia pendente.
- Geometria Gerdau não é equivalência de aço EN. ASTM A36, A572 ou A325 não são convertidos para essa opção.
- As verificações e limites de geometria do método continuam obrigatórios. Amarração acidental, apoio em mesa da coluna, N/V simultâneos e estabilidade global não integram esta opção.
- O engenheiro deve confirmar a admissibilidade desse método no projeto e os materiais efetivamente fornecidos.

Referência primária: https://www.steelconstruction.info/images/a/a9/SCI_P358.pdf

Para importar um projeto SCI, escolha essa opção e use “Abrir projeto SCI desta opção”. A autodetecção geral de JSON não foi estendida. Alternar os métodos não autoriza converter dados entre eles.

## Distribuição e testes
Pacote compacto com módulos, catálogos e exemplos completos. Caches, suíte de testes e subpastas de evidências históricas ficam preservados separadamente na fonte completa. Documentos de método e limites permanecem em docs. O manifesto e o vínculo SHA conferem esta distribuição.

Foram realizados testes direcionados de cálculo, limites, importação/exportação, alternância dos métodos e regressões da end plate existente, além do pacote extraído. A suíte integral da .58 não foi repetida porque os demais motores não foram alterados. Consulte docs/VALIDACAO0959.md para cobertura e limites. Testes de software não equivalem à aprovação estrutural de um projeto real.

## Pacote compacto
Distribuição de uso com os mesmos cálculos, recursos e exemplos. A suíte de testes e subpastas de evidências históricas não acompanham este ZIP; foram preservadas na fonte completa. Consulte docs/DISTRIBUICAO_COMPACTA0959.md.

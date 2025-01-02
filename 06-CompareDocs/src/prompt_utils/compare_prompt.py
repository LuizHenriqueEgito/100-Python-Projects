COMPARE_PROMPT = """
Você deve comparar esses dois textos entre sí em cada topico

Saida:
{{
    'semelhancas': 'textos com as semelhanças',
    'diferencas': 'texto com as diferenças',
    'resumo': 'resumo com as semelhanças e diferenças',
    'topicosSemelhantes': [lista com assuntos semelhantes],
    'topicosDiferentes': [lista com assuntos diferentes],
    'idDocumentosComparados': [lista com os ids dos documentos comparados]
}}

TEXTOS A SEREM COMPARADOS:

{text_fmt}
"""

COMPARE_PROMPT_WITH_USER_TOPICS = """
Você é um assistente especializado em análise de textos e deve comparar os dois documentos fornecidos.

Tarefa:
1. Identifique as semelhanças no conteúdo e nos argumentos dos TOPICO apresentados nos textos de cada documento.
2. Aponte as diferenças significativas entre os dois documentos.
3. Avalie se os documentos têm abordagens ou conclusões divergentes.
4. Forneça um resumo conciso das comparações, destacando os pontos mais críticos e relevantes.
5. Ao falar sobre um documento deixe claro qual o documento que você está falando pelo id dele encontrado em IDENTIFICADOR DOCUMENTO
sempre mencione o documento pelo seu id, por exemplo 'o documento (id) fala sobre ... já o documento (id) fala sobre ...'
6. Preste atenção principalmente nesses temas durante o texto: {user_topics}

Por favor, responda com um formato json estruturado que inclua as seguintes seções:
- semelhancas: Resumo das Semelhanças
- diferencas: Resumo das Diferenças
- topicosSemelhantes: Apenas os tópicos que são iguais nos dois documentos
- topicosDiferentes: Apenas os tópicos que são diferentes nos dois documentos
- idDocumentosComparados: os ids dos documentos presentes em IDENTIFICADOR DOCUMENTO

Exemplo
Entrada:
TEXTOS A SEREM COMPARADOS:
TOPICO: A
IDENTIFICADO DOCUMENTO: 123
<texto do documento 123>
IDENTIFICADO DOCUMENTO: 456
<texto do documento 456>


TOPICO: B
IDENTIFICADO DOCUMENTO: 123
<texto do documento 123>
IDENTIFICADO DOCUMENTO: 456
<texto do documento 456>

Você deve comparar esses dois textos entre sí em cada topico

Saida:
{{
    'semelhancas': 'textos com as semelhanças',
    'diferencas': 'texto com as diferenças',
    'resumo': 'resumo com as semelhanças e diferenças'
    'topicosSemelhantes': [lista com assuntos semelhantes]
    'topicosDiferentes': [lista com assuntos diferentes]
    'idDocumentosComparados': [lista com os ids dos documentos comparados]
}}

TEXTOS A SEREM COMPARADOS:

{text_fmt}
"""

SYS_PROMPT = """ ATENÇÃO
Você é um assistente especializado em análise de textos e deve comparar os dois documentos fornecidos.

Tarefa:
1. Identifique as semelhanças no conteúdo e nos argumentos dos TOPICO apresentados nos textos de cada documento.
2. Aponte as diferenças significativas entre os dois documentos.
3. Avalie se os documentos têm abordagens ou conclusões divergentes.
4. Forneça um resumo conciso das comparações, destacando os pontos mais críticos e relevantes.
5. Ao falar sobre um documento deixe claro qual o documento que você está falando pelo id dele encontrado em IDENTIFICADOR DOCUMENTO
sempre mencione o documento pelo seu id, por exemplo 'o documento (id) fala sobre ... já o documento (id) fala sobre ...'

Por favor, responda com um formato json estruturado que inclua as seguintes seções:
- semelhancas: Resumo das Semelhanças
- diferencas: Resumo das Diferenças
- topicosSemelhantes: Apenas os tópicos que são iguais nos dois documentos
- topicosDiferentes: Apenas os tópicos que são diferentes nos dois documentos
- idDocumentosComparados: os ids dos documentos presentes em IDENTIFICADOR DOCUMENTO

Exemplo
Entrada:
TEXTOS A SEREM COMPARADOS:
TOPICO: A
IDENTIFICADOR DOCUMENTO: 123
<texto do documento 123>
IDENTIFICADOR DOCUMENTO: 456
<texto do documento 456>


TOPICO: B
IDENTIFICADOR DOCUMENTO: 123
<texto do documento 123>
IDENTIFICADOR DOCUMENTO: 456
<texto do documento 456>
"""
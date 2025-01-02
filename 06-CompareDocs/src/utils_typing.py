from src.document import Document


type PairDocuments = tuple[Document, Document]
type PoolDocuments = list[PairDocuments]
# isso tem que ser assim porque para 2 documentos o preprocessamento 
# pode ser diferente se não for isso pode ir para a classe Document
# Mas talvez você consiga fazer uma classe para representar o preprocessamento
type PairPreprocessedDocs = list[tuple[dict[str, str]]]
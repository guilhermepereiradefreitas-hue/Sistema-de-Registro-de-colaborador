# Sistema de Registro de Funcionários

Resumo
------
Este projeto implementa um sistema simples de cadastro e gerenciamento de funcionários usando Python, SQLite e uma interface gráfica feita com Tkinter. A interface permite registrar, visualizar, pesquisar, atualizar e remover funcionários, além de anexar uma foto do funcionário.

Objetivo
--------
Fornecer uma ferramenta leve e local para pequenas empresas/ou equipes gerenciarem informações de colaboradores sem necessidade de um servidor externo. É ideal como protótipo, para ensino ou para uso interno.

Funcionalidades principais
-------------------------
- Cadastro de funcionários com os campos: nome, e-mail, telefone, sexo, data de nascimento, endereço, loja, endereço da loja, data de admissão, fim do contrato, cargo, salário e foto.
- Visualização de todos os registros cadastrados.
- Pesquisa de funcionário por ID.
- Atualização de dados do funcionário.
- Exclusão de registros (funcionalidade disponível na lógica, pode ser ativada via interface).
- Armazenamento persistente usando SQLite (arquivo `Funcionario.db`).

Arquitetura e arquivos importantes
---------------------------------
- `Interface.py` — Interface gráfica (Tkinter) com formulários e botões de ação.
- `Projeto_de_Cadastro_de_Funcionarios_main.py` — Lógica de persistência com SQLite e funções para CRUD (criar/ler/atualizar/deletar).
- `logo.png` — (opcional) logotipo exibido na interface se presente no diretório.
- `Descrição_do_Projeto.md` — Este documento.

Tecnologias e bibliotecas
-------------------------
- Python 3.x
- Tkinter — GUI (vem com Python em instalações padrão)
- Pillow (`PIL`) — manipulação de imagens (instalar via pip)
- tkcalendar — widgets de calendário/data para Tkinter (instalar via pip)
- SQLite (módulo `sqlite3` do Python) — banco de dados embarcado

Instalação (ambiente Windows)
-----------------------------
1. Garanta que o Python 3 esteja instalado e disponível no PATH.
2. No terminal (PowerShell), instale as dependências:

```powershell
pip install Pillow tkcalendar
```

3. Coloque o arquivo `logo.png` (opcional) na raiz do projeto para que o logo seja exibido.

Como executar
-------------
- Para rodar a interface gráfica: execute

```powershell
python "d:\\Projeto Python\\Interface.py"
```

- Para testar a lógica de banco (script de exemplo): execute

```powershell
python "d:\\Projeto Python\\Projeto_de_Cadastro_de_Funcionarios_main.py"
```

Observações e boas práticas
--------------------------
- O banco de dados SQLite é criado automaticamente como `Funcionario.db` na pasta do projeto.
- Em desenvolvimento, o script de criação de tabela pode dropar a tabela para garantir a estrutura; em produção remova essa ação para não perder dados.
- Validações de campos (e-mail, telefone, formatos de data) devem ser adicionadas antes de salvar em produção.
- Para integrar a GUI com a lógica de banco, ligue os botões (Salvar/Atualizar/Deletar) às funções correspondentes no módulo principal. Recomenda-se refatorar a lógica de banco para ser instanciável/importável sem executar o bloco `if __name__ == '__main__'`.

Próximos passos sugeridos
------------------------
- Implementar validação de entrada e mensagens de erro informativas na interface.
- Conectar os botões da interface (`Interface.py`) às funções do `Projeto_de_Cadastro_de_Funcionarios_main.py`.
- Adicionar pequenos testes unitários para as funções de banco.
- Pense em adicionar criptografia/backup do arquivo SQLite para proteção de dados.

Licença
-------
Coloque aqui o tipo de licença (por exemplo, MIT) ou uma nota indicando uso privado.

Contato
-------
Projeto mantido localmente. Para dúvidas ou melhorias, abra um issue ou entre em contato com o autor do projeto.

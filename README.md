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
- Adicionar opção de Download de Arquivo pdf ou Word contido o contracheque com os descontos atraves das informações passadas outomaticamente `Funcionario.db` na pasta do projeto
- Implementação de relatórios em PDF
- Criptografia de dados sensíveis
- Filtros avançados de busca
- Integração com sistemas externos
- App mobile para registro de ponto e advertências
- Geração automática de contracheques em PDF
- Dashboard com métricas de RH

Licença
-------
MIT License

Copyright (c) 2025 Guilherme Pereira

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Autor
------
**Guilherme Pereira**
- GitHub: [guilhermepereiradefreitas-hue](https://github.com/guilhermepereiradefreitas-hue)
- Desenvolvedor Full Stack
- Estudanto Python e Desenvolvimento de Sistemas

---
⌨️ Desenvolvido por Guilherme Pereira

© 2025 Guilherme Pereira - Todos os direitos reservados

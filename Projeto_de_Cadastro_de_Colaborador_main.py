import sqlite3
from tkinter import messagebox as caixa_de_menssagem

class SistemaDeRegistro:
    def __init__(self):
        self.conectar_banco()
        self.c = self.conn.cursor()
        self.create_tabela()

    def conectar_banco(self):
        self.conn = sqlite3.connect('Funcionario.db')

    def create_tabela(self):
        # Primeiro, vamos dropar a tabela se ela existir para garantir a estrutura correta
        self.c.execute('DROP TABLE IF EXISTS Funcionarios')
        
        # Agora criamos a tabela com a estrutura atualizada
        self.c.execute('''CREATE TABLE IF NOT EXISTS Funcionarios ( 
                         id INTEGER PRIMARY KEY AUTOINCREMENT,
                         nome TEXT NOT NULL,
                         email TEXT NOT NULL,
                         telefone TEXT NOT NULL,
                         Sexo TEXT NOT NULL,     
                         data_nascimento TEXT NOT NULL,                      
                         endereco TEXT NOT NULL,
                         loja TEXT NOT NULL,
                         endereco_loja TEXT NOT NULL,
                         Data_admissao DATE NOT NULL,
                         fim_contrato DATE NOT NULL,
                         cargo TEXT NOT NULL,
                         salario REAL NOT NULL,
                         foto TEXT NOT NULL)''')

    def registro_Funcionarios(self, funcionarios):
        self.c.execute("""
            INSERT INTO Funcionarios (
                nome, email, telefone, sexo, data_nascimento,
                endereco, loja, endereco_loja, Data_admissao,
                fim_contrato, cargo, salario, foto
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, funcionarios)
        self.conn.commit()
        caixa_de_menssagem.showinfo('Sucesso', 'Funcionário registrado com sucesso!')

    def view_all_Funcionarios(self):
        self.c.execute("SELECT * FROM Funcionarios")
        dados = self.c.fetchall()

        if not dados:
            print("Nenhum funcionário cadastrado.")
            return

        for i in dados:
            print(f'ID: {i[0]} │ Nome: {i[1]} │ E-mail: {i[2]} │ Telefone: {i[3]} │ Sexo: {i[4]} │ '
                  f'Data de Nascimento: {i[5]} │ Endereço: {i[6]} │ Loja: {i[7]} │ Endereço da Loja: {i[8]} │ '
                  f'Início da Admissão: {i[9]} │ Fim da Admissão: {i[10]} │ Cargo: {i[11]} │ '
                  f'Salário: R${i[12]:.2f} │ Foto: {i[13]}')

    def search_Funcionarios(self, ID):
        self.c.execute("SELECT * FROM Funcionarios WHERE id=?", (ID,))
        dados = self.c.fetchone()

        if dados:
            print(f'ID: {dados[0]} │ Nome: {dados[1]} │ E-mail: {dados[2]} │ Telefone: {dados[3]} │ '
                  f'Sexo: {dados[4]} │ Data de Nascimento: {dados[5]} │ Endereço: {dados[6]} │ '
                  f'Loja: {dados[7]} │ Endereço da Loja: {dados[8]} │ Início da Admissão: {dados[9]} │ '
                  f'Fim da Contrato: {dados[10]} │ Cargo: {dados[11]} │ Salário: R${dados[12]:.2f} │ '
                  f'Foto: {dados[13]}')
        else:
            print("Funcionário não encontrado.")

    def update_Funcionarios(self, ID, novos_dados):
        self.c.execute("""
            UPDATE Funcionarios SET 
                nome=?, email=?, telefone=?, sexo=?, data_nascimento=?,
                endereco=?, loja=?, endereco_loja=?, inicio_contrato=?,
                fim_contrato=?, cargo=?, salario=?, foto=?
            WHERE id=?
        """, (*novos_dados, ID))
        self.conn.commit()
        caixa_de_menssagem.showinfo('Sucesso', 'Dados do funcionário atualizados com sucesso!')

    def delete_Funcionarios(self, ID):
        self.c.execute("DELETE FROM Funcionarios WHERE id=?", (ID,))
        self.conn.commit()
        caixa_de_menssagem.showinfo('Sucesso', 'Funcionário removido com sucesso!')

if __name__ == '__main__':
    # Criando uma instância para testar o sistema
    sistema = SistemaDeRegistro()
    
    print("\n=== Testando o Sistema de Registro de Funcionários ===\n")
    
    # Exemplo de registro de funcionário
    funcionario = (
        'Guilherme P',
        'guilherme.pereira@email.com',
        '1234-5678',
        'Masculino',
        '01/01/1992',
        'Rua A, 123',
        'Loja A',
        'Rua B, 456',
        '01/01/2020',
        '01/01/2021',
        'Desenvolvedor',
        3000.00,
        'foto.jpg'
    )
    
    try:
        # Registrando o funcionário
        print("1. Registrando novo funcionário...")
        sistema.registro_Funcionarios(funcionario)
        
        # Visualizando todos os funcionários
        print("\n2. Visualizando todos os funcionários:")
        sistema.view_all_Funcionarios()
        
        # Pesquisando funcionário por ID
        print("\n3. Pesquisando funcionário com ID 1:")
        sistema.search_Funcionarios(1)
        
        # Atualizando dados do funcionário
        print("\n4. Atualizando dados do funcionário...")
        novos_dados = (
            'Guilherme Pereira',  # nome atualizado
            'guilherme.p@email.com',  # email atualizado
            '9876-5432',  # telefone atualizado
            'Masculino',
            '01/01/1992',
            'Rua X, 789',  # endereço atualizado
            'Loja B',  # loja atualizada
            'Rua Y, 321',  # endereço da loja atualizado
            '01/01/2020',
            '01/01/2023',  # fim do contrato atualizado
            'Desenvolvedor Senior',  # cargo atualizado
            5000.00,  # salário atualizado
            'nova_foto.jpg'  # foto atualizada
        )
        sistema.update_Funcionarios(1, novos_dados)
        
        # Visualizando funcionário atualizado
        print("\n5. Visualizando dados atualizados:")
        sistema.search_Funcionarios(1)
        
        print("\n=== Teste concluído com sucesso! ===\n")
    except Exception as e:
        print(f"\nErro durante a execução: {str(e)}")







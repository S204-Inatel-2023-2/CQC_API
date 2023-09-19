
class EventDatabase:
    def __init__(self, database):
        self.db = database

    def create_usuario(self, nome,sobrenome, mail, senha):
        query = "CREATE(:usuario {nome: $nome, sobrenome: $sobrenome, mail: $mail, senha: $senha})"
        parameters = {"nome": nome,'sobrenome': sobrenome, "mail": mail, "senha": senha}
        self.db.execute_query(query, parameters)

    def create_administrador(self, nome, mail, senha):
        query = "CREATE(:administrador {nome: $nome, mail: $mail, senha: $senha})"
        parameters = {"nome": nome, "mail": mail, "senha": senha}
        self.db.execute_query(query, parameters)

    def create_evento(self, nome, local, administrador):
        query = "CREATE(:evento {nome: $nome, local: $local, administrador: $administrador})"
        parameters = {"nome": nome, "local": local, "administrador": administrador}
        self.db.execute_query(query, parameters)

    def create_connection_adm_event(self, nome_adm, nome_evento):
        query = "MATCH (a:administrador {nome: $nome_adm}), (e:evento {nome: $nome_evento}) CREATE (a)-[:ADMINISTRA]->(e);"
        parameters = {"nome_adm": nome_adm, "nome_evento": nome_evento}
        self.db.execute_query(query, parameters)

    def insert_usuario_evento(self, usuario_nome, evento_nome):
        query = "MATCH (a:usuario {nome: $usuario_nome}) MATCH (b:evento {nome: $evento_nome}) CREATE (a)-[:PARTICIPA]->(b);"
        parameters = {"usuario_nome": usuario_nome, "evento_nome": evento_nome}
        self.db.execute_query(query, parameters)

    def get_usuario(self):
        query = "MATCH (u:usuario) RETURN u.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_evento(self):
        query = "MATCH (e:evento) RETURN e.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def delete_usuario(self, nome):
        query = "MATCH (u:usuario {nome: $nome}) DETATCH DELETE u"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def delete_evento(self, nome):
        query = "MATCH (e:evento {nome: $nome}) DETATCH DELETE e"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def delete_adm(self, nome):
        query = "MATCH (adm:administrador {nome: $nome}) DETATCH DELETE adm"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)



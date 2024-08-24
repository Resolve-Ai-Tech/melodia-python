## 1. Criando um Docker Container PostgreSQL

**Observação:** Certifique-se de estar no diretório `docker/`.

### Configurações Iniciais (TESTE!)
Antes de criar o container, saiba que seguintes parâmetros são apenas testes:
```json
{
  "docker-name": "melodia_sql",
  "database_name": "melodia",
  "password": "melodia",
  "user": "melodia",
  "port": 5444
}
```
Siga os passos abaixo em seu terminal para criar um container PostgreSQL:
```bash
docker create --name melodia_sql -e POSTGRES_USER=melodia -e POSTGRES_PASSWORD=melodia -e POSTGRES_DB=melodia -p 5444:5432 -v $(pwd)/data:/var/lib/postgresql/data postgres:16
```

Pronto! Seu container PostgreSQL foi criado com sucesso.

## 2. Inicializando o Container PostgreSQL
**Para a inicialização, caso não tenha um container PostgreSQL, crie um container PostgreSQL seguindo [a primeira instrução.](#1-Criando-Um-Docker-Container-PostgreSQL)**
```bash
docker start melodia_sql
```
**Para se conectar diretamente ao PostgreSQL, utilize o comando abaixo:**
```bash
docker exec -it melodia_sql psql -U melodia -d melodia
```

sudo docker create --name melodia_database -e POSTGRES_USER=melodia -e POSTGRES_PASSWORD=melodia -e POSTGRES_DB=melodia -p 5444:5432 -v $(pwd)/docker/data:/var/lib/postgresql/data postgres:16

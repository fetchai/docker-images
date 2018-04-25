./scripts/docker-delete-img-from-cache.sh
./scripts/docker-build-img.sh --no-cache --
mkdir ~/.docker
echo "{
  \"credHelpers\": {
    \"gcr.io\": \"gcloud\",
    \"us.gcr.io\": \"gcloud\",
    \"eu.gcr.io\": \"gcloud\",
    \"asia.gcr.io\": \"gcloud\",
    \"staging-k8s.gcr.io\": \"gcloud\"
  }
}" >> ~/.docker/config.json
cat ~/.docker/config.json
./scripts/docker-deploy-img.sh
./scripts/docker-delete-img-from-cache.sh


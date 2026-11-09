# Security Log Analyser — Docker and GitHub Actions

Small educational Python project detecting IPs with at least three failed logins in sample CSV data. Not a production intrusion detection system.

## Run locally

```bash
python analyser.py
python -m unittest discover -s tests -v
```

## Docker

Install Docker Desktop, start Docker, then run from this directory:

```bash
docker build -t security-log-analyser:local .
docker run --rm security-log-analyser:local
```

The container entrypoint runs four unit tests and then the analyser.

## Custom GitHub Action and CI

`.github/actions/security-check/action.yml` defines a **local composite custom action** which builds and runs the Docker image. `.github/workflows/tests.yml` calls that action on pushes and pull requests. This demonstrates a custom action that uses Docker commands, **not** a Docker-container action (`runs.using: docker`).

To collect evidence, upload the project to GitHub, create a branch, make a meaningful change and open a pull request. Capture the repository, action definition, Docker run output, successful GitHub Actions run, and merged pull request. Only claim actions you actually performed; disclose AI assistance according to course policy.

## Limitations and future learning

The detector has no time window, user correlation, or false-positive suppression. GitHub Projects automation and a Docker-container custom action are not included.

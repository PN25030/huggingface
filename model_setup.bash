#!/usr/bin/env bash

MODEL="google/tapas-small-finetuned-tabfact"

# Check cache for the model (search by repo id) and use --repo-type model when
# removing or downloading to avoid passing a 'model/...' prefixed id.
if uvx hf cache list | grep -q "$MODEL"; then
  uvx hf cache rm --repo-type model "$MODEL"
else
  uvx hf download --repo-type model "$MODEL"
fi
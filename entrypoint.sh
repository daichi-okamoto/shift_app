#!/bin/bash
set -e

# Remove a potentially pre-existing server.pid for Rails.
rm -f /sample-app/tmp/pids/server.pid

# データベースの作成とマイグレーションの実行
bundle exec rails db:create db:migrate

# アセットのビルド
yarn build:css

# Then exec the container's main process (what's set as CMD in the Dockerfile).
exec "$@"

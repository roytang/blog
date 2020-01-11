d:
cd D:\repos\blog

git pull
hugo --config config.toml,backup.toml -d d:\repos\roytang.github.io --gc --minify

cd d:\repos\roytang.github.io

git add .
git commit -m "Backup.bat"
git push
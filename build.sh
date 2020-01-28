hugo --gc --minify --templateMetrics > log.txt
mkdir public/build
mv log.txt public/build/log.txt
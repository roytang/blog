date >> log.txt
hugo version >> log.txt
hugo --gc --templateMetrics >> log.txt
mkdir public/build
mv log.txt public/build/log.txt
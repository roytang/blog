echo "### Root"
/home/roy/hugo --contentDir collections_root --config collections.toml --destination /var/www/html/collections/ 
echo "### Lyrics"
/home/roy/hugo --contentDir collections/lyrics --config collections.toml,collections/lyrics/lyrics.toml --destination /var/www/html/collections/lyrics
echo "### Quotes"
/home/roy/hugo --contentDir collections/quotes --config collections.toml,collections/quotes/quotes.toml --destination /var/www/html/collections/quotes
echo "### Comics"
/home/roy/hugo --contentDir collections/comics --config collections.toml,collections/comics/comics.toml --destination /var/www/html/collections/comics
echo "### Albums"
/home/roy/hugo --contentDir collections/albums --config collections.toml,collections/albums/albums.toml --destination /var/www/html/collections/albums
echo "### Stackexchange"
/home/roy/hugo --contentDir collections/stackexchange --config collections.toml,collections/stackexchange/stackexchange.toml --destination /var/www/html/collections/stackexchange
echo "### Webcomics"
/home/roy/hugo --contentDir collections/webcomics --config collections.toml,collections/webcomics/webcomics.toml --destination /var/www/html/collections/webcomics
echo "### Quora"
/home/roy/hugo --contentDir collections/quora --config collections.toml,collections/quora/quora.toml --destination /var/www/html/collections/quora
echo "### Sketchbook"
/home/roy/hugo --contentDir collections/sketchbook --config collections.toml,collections/sketchbook/sketchbook.toml --destination /var/www/html/collections/sketchbook
echo "### Threads"
/home/roy/hugo --contentDir collections/threads --config collections.toml,collections/threads/threads.toml --destination /var/www/html/collections/threads
echo "### Surveys"
/home/roy/hugo --contentDir collections/surveys --config collections.toml,collections/surveys/surveys.toml --destination /var/www/html/collections/surveys
echo "### Jokes"
/home/roy/hugo --contentDir collections/jokes --config collections.toml,collections/jokes/jokes.toml --destination /var/www/html/collections/jokes
echo "### MiiVerse"
/home/roy/hugo --contentDir collections/miiverse --config collections.toml,collections/miiverse/miiverse.toml --destination /var/www/html/collections/miiverse
echo "### Quiz Nights"
/home/roy/hugo --contentDir collections/quiznights --config collections.toml,collections/quiznights/quiznights.toml --destination /var/www/html/collections/quiznights
echo "### Fiction"
/home/roy/hugo --contentDir collections/fiction --config collections.toml,collections/fiction/fiction.toml --destination /var/www/html/collections/fiction
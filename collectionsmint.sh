echo "### Root"
hugo --contentDir collections_root --config collections.toml --destination /var/www/html/collections/ 
echo "### Lyrics"
hugo --contentDir collections/lyrics --config collections.toml,collections/lyrics/lyrics.toml --destination /var/www/html/collections/lyrics
echo "### Quotes"
hugo --contentDir collections/quotes --config collections.toml,collections/quotes/quotes.toml --destination /var/www/html/collections/quotes
echo "### Comics"
hugo --contentDir collections/comics --config collections.toml,collections/comics/comics.toml --destination /var/www/html/collections/comics
echo "### Albums"
hugo --contentDir collections/albums --config collections.toml,collections/albums/albums.toml --destination /var/www/html/collections/albums
echo "### Stackexchange"
hugo --contentDir collections/stackexchange --config collections.toml,collections/stackexchange/stackexchange.toml --destination /var/www/html/collections/stackexchange
echo "### Webcomics"
hugo --contentDir collections/webcomics --config collections.toml,collections/webcomics/webcomics.toml --destination /var/www/html/collections/webcomics
echo "### Quora"
hugo --contentDir collections/quora --config collections.toml,collections/quora/quora.toml --destination /var/www/html/collections/quora
echo "### Sketchbook"
hugo --contentDir collections/sketchbook --config collections.toml,collections/sketchbook/sketchbook.toml --destination /var/www/html/collections/sketchbook
echo "### Threads"
hugo --contentDir collections/threads --config collections.toml,collections/threads/threads.toml --destination /var/www/html/collections/threads
echo "### Surveys"
hugo --contentDir collections/surveys --config collections.toml,collections/surveys/surveys.toml --destination /var/www/html/collections/surveys
echo "### Jokes"
hugo --contentDir collections/jokes --config collections.toml,collections/jokes/jokes.toml --destination /var/www/html/collections/jokes
echo "### MiiVerse"
hugo --contentDir collections/miiverse --config collections.toml,collections/miiverse/miiverse.toml --destination /var/www/html/collections/miiverse
echo "### Quiz Nights"
hugo --contentDir collections/quiznights --config collections.toml,collections/quiznights/quiznights.toml --destination /var/www/html/collections/quiznights
echo "### Fiction"
hugo --contentDir collections/fiction --config collections.toml,collections/fiction/fiction.toml --destination /var/www/html/collections/fiction
hugo --contentDir collections_root --config collections.toml --destination /var/www/collections/ 
hugo --contentDir collections/lyrics --config collections.toml,collections/lyrics/lyrics.toml --destination /var/www/collections/lyrics
hugo --contentDir collections/quotes --config collections.toml,collections/quotes/quotes.toml --destination /var/www/collections/quotes
hugo --contentDir collections/comics --config collections.toml,collections/comics/comics.toml --destination /var/www/collections/comics
hugo --contentDir collections/albums --config collections.toml,collections/albums/albums.toml --destination /var/www/collections/albums
hugo --contentDir collections/stackexchange --config collections.toml,collections/stackexchange/stackexchange.toml --destination /var/www/collections/stackexchange
